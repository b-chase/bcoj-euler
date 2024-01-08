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
import numpy as np # will need to do some matrix math!
import os

def solve(debug=False):

    spaces_list = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 
                   'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 
                   'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 
                   'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
    
    jail_index = spaces_list.index('JAIL')
    
    chance_cards = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'rr', 'rr', 'uu', 'back3'] + [None]*6
    cc_cards = ['GO', 'JAIL'] + [None]*14

    def get_next_rr_index(space_index:int) -> int:
        # takes a space index and returns the next railroad from available spaces
        for space_name in spaces_list[space_index+1:]:
            if space_name.startswith('R'):
                return spaces_list.index(space_name)
        return spaces_list.index('R1')
    
    def get_next_uu_index(space_index:int) -> int:
        # takes a space index and returns the next utility from available spaces
        for space_name in spaces_list[space_index+1:]:
            if space_name.startswith('U'):
                return spaces_list.index(space_name)
        return spaces_list.index('U1')    
    
    if False:
        for i in range(40):
            # test which railroad returns for each chance space:
            if spaces_list[i].startswith('CH'):
                print(spaces_list[i], spaces_list[get_next_rr_index(i)])
            # test which utility returns for each community chest square:
            if spaces_list[i].startswith('CC'):
                print(spaces_list[i], spaces_list[get_next_uu_index(i)])
        quit()
        
    # some dice calculations
    die_roll_ways = roll_dice_combos(4, 2)
    print(die_roll_ways)
    
    
    # trying a new tack, going to run parallel simulations and merge outputs to get frequencies
    def simulate_game(die_roll_ways:dict, max_rolls=10000, debug=debug, jail_clears_doubles=True) -> np.ndarray[int]:
        # simulate a game of monopoly
        space_landings = np.zeros(40, dtype=int)
        
        # shuffle cc and chance cards:
        cc_deck = np.random.choice(cc_cards, size=len(cc_cards), replace=False)
        ch_deck = np.random.choice(chance_cards, size=len(chance_cards), replace=False)
        
        # for _ in range(10):
        #     print(ch_deck)
        #     ch_deck = np.append(ch_deck[1:],ch_deck[0])
        # quit()
        
        def move_spaces(old_space, roll_total, cc_deck=cc_deck, ch_deck=ch_deck):
            new_space = (old_space + roll_total) % 40
            if spaces_list[new_space] == 'G2J':
                current_space = jail_index
            
            elif spaces_list[new_space].startswith('CC'):
                cc_card = cc_deck[0]
                cc_deck = np.append(cc_deck[1:],cc_card)
                if cc_card is None:
                    current_space = new_space
                elif cc_card == 'GO':
                    current_space = 0
                elif cc_card == 'JAIL':
                    current_space = jail_index
                else:
                    current_space = new_space
            
            elif spaces_list[new_space].startswith('CH'):
                ch_card = ch_deck[0]
                ch_deck = np.append(ch_deck[1:],ch_card)
                if ch_card is None:
                    current_space = new_space
                elif ch_card == 'GO':
                    current_space = 0
                elif ch_card == 'JAIL':
                    current_space = jail_index
                elif ch_card == 'rr':
                    current_space = get_next_rr_index(new_space)
                elif ch_card == 'uu':
                    current_space = get_next_uu_index(new_space)
                elif ch_card == 'back3':
                    # chance spaces are always greater than 3
                    current_space, cc_deck, ch_deck = move_spaces(new_space, -3, cc_deck, ch_deck)
                else:
                    current_space = spaces_list.index(ch_card)
                
            else:
                current_space = new_space
            
            return current_space, cc_deck, ch_deck
        
        # create list of possible rolls
        roll_list = list()
        for dice_combo, cts in die_roll_ways.items():
            for _ in range(cts):
                roll_list.append(dice_combo)
        total_rolls = len(roll_list)
        # iterate until reaching max rolls
        doubles_ct = 0
        current_space = 0
        for _ in range(max_rolls):
            roll_i = np.random.randint(total_rolls)
            roll = roll_list[roll_i]
            # check for doubles
            if roll[0] == roll[1]:
                if doubles_ct == 2:
                    current_space = jail_index
                    doubles_ct = 0
                    space_landings[current_space] += 1
                    continue
                else:
                    doubles_ct += 1
                
            current_space, cc_deck, ch_deck = move_spaces(current_space, sum(roll), cc_deck, ch_deck)
            if jail_clears_doubles and current_space==jail_index:
                doubles_ct = 0
            
            space_landings[current_space] += 1
        assert np.sum(space_landings) == max_rolls, f"Resulted in {np.sum(space_landings)} total rolls"
        return space_landings
    
    # run simulations
    sim_res = np.zeros(40, int)
    for _ in range(5000):    
        test_sim = simulate_game(die_roll_ways, max_rolls=1000, debug=debug, jail_clears_doubles=True)
        sim_res += test_sim
    
    probs = sim_res / np.sum(sim_res)
    
    # print a line ranking output spaces by likelihood
    rankings = np.argsort(probs)[::-1]
    for i in range(10):
        print(f"{rankings[i]} {spaces_list[rankings[i]]}: {probs[rankings[i]]:.6f}")
    
    # 101516 -- x
    
    
    
    quit()
    # movement_freqs = dict()
    # for rolls, cts in die_roll_ways.items():
    #     movement = sum(rolls)
    #     movement_freqs[movement] = cts + movement_freqs.get(movement, 0)
    
    # get dimensions of markov matrix, 40 for the available spaces, tripled to account for potentially rolling doubles
    markov_dim = (3*len(spaces_list), 3*len(spaces_list))
    
    # create frequency matrix
    frequency_matrix = np.zeros(markov_dim)
    
    # populate matrix with number of ways each square can be reached from each
    for doubles_ct in range(3):
        for i in range(40):
            # iterate through list of die rolls
            matrix_i = doubles_ct*40 + i
            for roll, way_ct in die_roll_ways.items():
                # get next space index
                next_index = (i+sum(roll)) % 40
                adj_way_ct = 16 * way_ct  # mult by 16 for different ways community chest and chance cards work
                
                if roll[0] == roll[1]:
                    doubles_counter = doubles_ct + 1
                else:
                    doubles_counter = doubles_ct + 0
                
                if spaces_list[next_index] == 'G2J':
                    doubles_counter = 0
                    next_index = jail_index + doubles_counter*40  # in case we want to count doubles here
                    frequency_matrix[matrix_i, next_index] += adj_way_ct  # way_ct is always 1 here
                    continue
                
                # check if doubles were rolled
                elif roll[0]==roll[1] and doubles_counter==3:
                        next_index = jail_index
                        frequency_matrix[matrix_i, next_index] += adj_way_ct  # way_ct is always 1 here
                        continue
                
                # check if space is a community chest card
                elif spaces_list[next_index].startswith('CC'):
                    for destination in cc_cards:
                        if destination:
                            cc_next_index = spaces_list.index(destination)
                        else:
                            cc_next_index = next_index
                        # increment matrix by 1 for given destination
                        if cc_next_index % 40 == jail_index:
                            doubles_counter = 0
                        frequency_matrix[matrix_i, cc_next_index + 40*doubles_counter] += way_ct
                            
                # check if space is a chance card
                elif spaces_list[i].startswith('CH'):
                    for destination in chance_cards:
                        if destination:
                            if destination == 'rr':
                                ch_next_index = get_next_rr_index(next_index)
                            elif destination == 'uu':
                                ch_next_index = get_next_uu_index(next_index)
                            elif destination == 'back3':
                                ch_next_index = (40 + next_index - 3) % 40
                            else:
                                ch_next_index = spaces_list.index(destination)
                        else:
                            ch_next_index = next_index
                        if ch_next_index % 40 == jail_index:
                            doubles_counter = 0
                        frequency_matrix[matrix_i, ch_next_index + 40*doubles_counter] += way_ct
                
                else:
                    frequency_matrix[matrix_i, next_index + 40*doubles_counter] += adj_way_ct

                # if debug:
                #     print(f"\nResults for roll: {roll} - {way_ct} ways, landing on {next_index}, starting from {matrix_i}")
                #     print(way_ct, next_index)
                #     # print first row of frequency matrix
                #     # sum over columns to get total frequency of each square
                #     square_freq = frequency_matrix[0,0:40]+frequency_matrix[0,40:80]+frequency_matrix[0,80:120]
                #     print(square_freq)
                #     print(f"Total of {np.sum(square_freq)} ways  ({np.sum(square_freq)/16} originally)")
                #     # sleep(0.5)
                    
                
            # if debug:
            #     break
            
    # check all rows total to same number
    first_row_total = np.sum(frequency_matrix[0])
    print(f"First row totals to {first_row_total}")
    for i in range(frequency_matrix.shape[0]):
        assert np.sum(frequency_matrix[i])==first_row_total, f"Row {i} does not sum to {first_row_total}"
    print(f"Matrix is normalized")
    
    # convert regular frequency matrix to probability vector for each square
    def get_prob_vector(frequency_matrix: np.ndarray) -> list[float]:
        # returns tuple of (probability, square_name)
        freq_column_totals = np.sum(frequency_matrix, axis=0)
        # freq_column_totals = frequency_matrix[0]
        square_freq_totals = freq_column_totals[0:40]+freq_column_totals[40:80]+freq_column_totals[80:120]
        denom = np.sum(square_freq_totals)
        return square_freq_totals / denom
            
    
    # get stable transition matrix
    stable_frequency_matrix = frequency_matrix / first_row_total
    # prob_vals = get_prob_vector(frequency_matrix)
    epsilon = 1e-6
    converge_att = 0
    while True:
        converge_att += 1
        next_iteration_matrix = stable_frequency_matrix.dot(frequency_matrix) / first_row_total
        # compare values against original to see if any changes excide epsilon
        # cmp_prob_vals = get_prob_vector(next_iteration_matrix)
        # largest_diff = np.max(np.abs(prob_vals - cmp_prob_vals))
        largest_diff = np.max(np.abs(next_iteration_matrix - stable_frequency_matrix))
        if debug:
            print(f"[{converge_att:03d}] Largest difference: {largest_diff}")
        if largest_diff > epsilon:
            stable_frequency_matrix = next_iteration_matrix
            # prob_vals = cmp_prob_vals
        else:
            break
    
    final_probs = get_prob_vector(stable_frequency_matrix)
    print(f"Final probabilities: (summing to {np.sum(final_probs)}) \n{final_probs}")
    
    if debug:
        # write matrix to text file
        with open('markov_matrix.csv', 'w') as f:
            # matrix is large, so need to make sure numpy prints whole thing            
            np.savetxt(f, stable_frequency_matrix, fmt='%.3f', delimiter='  ')
            fname = f.name
        # os.system(f"code {fname} -r")
    
    # rank squares from most to least likely and print out the list line by line
    rank_list = np.argsort(final_probs)[::-1]
    for rank, square_index in enumerate(rank_list[0:40]):
        print(f"{square_index:02d} {spaces_list[square_index]}  {final_probs[square_index]:.4f}")
    
    
    res=None
    
    print(f'*** Answer: {res} ***')