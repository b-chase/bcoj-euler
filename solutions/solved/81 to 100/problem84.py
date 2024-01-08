# https://projecteuler.net/problem=84
"""<p>In the game, <strong>Monopoly</strong>, the standard board is set up in the following way:</p>
<div class="center">
<img src="resources/images/0084_monopoly_board.png?1678992052" alt="0084_monopoly_board.png">
</div>
<p>A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.</p>
<p>In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.</p>
<p>At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.</p>
<ul><li>Community Chest (2/16 cards):
<ol><li>Advance to GO</li>
<li>Go to JAIL</li>
</ol></li>
<li>Chance (10/16 cards):
<ol><li>Advance to GO</li>
<li>Go to JAIL</li>
<li>Go to C1</li>
<li>Go to E3</li>
<li>Go to H2</li>
<li>Go to R1</li>
<li>Go to next R (railway company)</li>
<li>Go to next R</li>
<li>Go to next U (utility company)</li>
<li>Go back 3 squares.</li>
</ol></li>
</ul><p>The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.</p>
<p>By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.</p>
<p>Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.</p>
<p>If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.</p>

"""
from euler_tools.math import roll_dice_combos
import euler_math as em
import itertools
import numpy as np # will need to do some matrix math!
import os

import random

spaces_list = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 
                   'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 
                   'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 
                   'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

def solve(debug=False):
    
    jail_index = spaces_list.index('JAIL')
    
    chance_cards = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', 'back3'] + [None]*6
    ch_iter = itertools.cycle(chance_cards)
    cc_cards = ['GO', 'JAIL'] + [None]*14
    cc_iter = itertools.cycle(cc_cards)
    
    def move_to_space(start_pos:int, dest_name:str) -> int:
        pos = (start_pos+1) % 40
        while not spaces_list[pos].startswith(dest_name):
            pos = (pos+1) % 40
            
            if pos == start_pos:
                raise Exception('infinite loop')
        return pos
    
    # drawing cards from both decks, default to not random
    
    
    random_draws = False
    
    def draw_chance(cards=chance_cards) -> str:
        # draw a chance card
        if random_draws:
            return np.random.choice(chance_cards)
        else:
            return next(ch_iter)
        
    def draw_community_chest(cards=cc_cards) -> str:
        # draw a community chest card
        if random_draws:
            return np.random.choice(cc_cards)
        else:
            return next(cc_iter)
    
    if False:
        ch = draw_chance()
        for _ in range(20):
            print(next(ch))
        print('\n')
        cc = draw_community_chest()
        for _ in range(20):
            print(next(cc))
        quit()
        
    def get_next_rr_index(space_index:int) -> int:
        # takes a space index and returns the next railroad from available spaces
        return move_to_space(space_index, 'R')
        
    
    def get_next_uu_index(space_index:int) -> int:
        # takes a space index and returns the next utility from available spaces
        return move_to_space(space_index, 'U')
        
        
    # debug rr and uu functions
    if False:
        for i in range(40):
            # test which railroad returns for each chance space:
            if spaces_list[i].startswith('CH'):
                print('next rr:', spaces_list[i], spaces_list[get_next_rr_index(i)])
            # test which utility returns for each community chest square:
            if spaces_list[i].startswith('CH'):
                print('next uu:', spaces_list[i], spaces_list[get_next_uu_index(i)])
            
            # test back3 for chance squares
            if spaces_list[i].startswith('CH'):
                print('back -3:', spaces_list[i], spaces_list[i-3])
        quit()
    
    def roll_dice(pips=6):
        d1 = np.random.randint(1, pips+1)
        d2 = np.random.randint(1, pips+1)
        return d1+d2, d1==d2
    
    
    # trying a new tack, going to run parallel simulations and merge outputs to get frequencies
    def simulate_game(dice_pips=6, max_rolls=10000, debug=debug, jail_clears_doubles=True) -> np.ndarray[int]:
        # simulate a game of monopoly
        space_landings = np.zeros(40, dtype=int)

        def move_spaces(old_space, roll_total):
            new_space = (old_space + roll_total) % 40
            if spaces_list[new_space] == 'G2J':
                return jail_index
            
            elif spaces_list[new_space].startswith('CC'):
                cc_card = draw_community_chest()
                if cc_card is None:
                    return new_space
                else:
                    assert isinstance(cc_card, str)
                    return move_to_space(new_space, cc_card)

            elif spaces_list[new_space].startswith('CH'):
                ch_card = draw_chance()
                if ch_card is None:
                    return new_space
                elif ch_card == 'back3':
                    # chance spaces are always greater than 3
                    return move_spaces(new_space, -3)
                else:
                    assert isinstance(ch_card, str)
                    return move_to_space(new_space, ch_card)
                                    
            return new_space
        
        # iterate until reaching max rolls
        doubles_ct = 0
        current_space = 0
        for _ in range(max_rolls):
            roll, is_doubles = roll_dice(dice_pips)
            # check for doubles
            if is_doubles:
                doubles_ct += 1
            else:
                doubles_ct = 0
            
            if doubles_ct >= 3:
                next_space = jail_index
            else:
                next_space = move_spaces(current_space, roll)
            
            if next_space == jail_index and jail_clears_doubles:
                doubles_ct = 0
            
            current_space = next_space
            space_landings[current_space] += 1
        assert np.sum(space_landings) == max_rolls, f"Resulted in {np.sum(space_landings)} total rolls"
        return space_landings
    
    # run simulations
    random_draws = False
    sim_res = np.zeros(40, float)
    trials = 20
    max_rolls = 50000
    for _ in range(trials):    
        test_sim = simulate_game(4, max_rolls=max_rolls, debug=debug, jail_clears_doubles=False)
        sim_res += (test_sim / max_rolls)
    probs = sim_res / trials
    # print a line ranking output spaces by likelihood
    rankings = np.argsort(probs)[::-1]
    for i in range(10):
        print(f"{rankings[i]} {spaces_list[rankings[i]]}: {probs[rankings[i]]:.6f}")
    
    # return string of indicies for top 3 locations
    res = f"{rankings[0]:02d}{rankings[1]:02d}{rankings[2]:02d}"
    
    print(f'*** Answer: {res} ***')