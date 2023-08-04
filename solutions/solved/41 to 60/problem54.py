"""<p>In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:</p>
<ul><li><b>High Card</b>: Highest value card.</li>
<li><b>One Pair</b>: Two cards of the same value.</li>
<li><b>Two Pairs</b>: Two different pairs.</li>
<li><b>Three of a Kind</b>: Three cards of the same value.</li>
<li><b>Straight</b>: All cards are consecutive values.</li>
<li><b>Flush</b>: All cards of the same suit.</li>
<li><b>Full House</b>: Three of a kind and a pair.</li>
<li><b>Four of a Kind</b>: Four cards of the same value.</li>
<li><b>Straight Flush</b>: All cards are consecutive values of same suit.</li>
<li><b>Royal Flush</b>: Ten, Jack, Queen, King, Ace, in same suit.</li>
</ul><p>The cards are valued in the order:<br>2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.</p>
<p>If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.</p>
<p>Consider the following five hands dealt to two players:</p>
<div class="center">
<table><tr><td><b>Hand</b></td><td>�</td><td><b>Player 1</b></td><td>�</td><td><b>Player 2</b></td><td>�</td><td><b>Winner</b></td>
</tr><tr><td><b>1</b></td><td>�</td><td>5H 5C 6S 7S KD<br><div class="smaller">Pair of Fives</div></td><td>�</td><td>2C 3S 8S 8D TD<br><div class="smaller">Pair of Eights</div></td><td>�</td><td>Player 2</td>
</tr><tr><td><b>2</b></td><td>�</td><td>5D 8C 9S JS AC<br><div class="smaller">Highest card Ace</div></td><td>�</td><td>2C 5C 7D 8S QH<br><div class="smaller">Highest card Queen</div></td><td>�</td><td>Player 1</td>
</tr><tr><td><b>3</b></td><td>�</td><td>2D 9C AS AH AC<br><div class="smaller">Three Aces</div></td><td>�</td><td>3D 6D 7D TD QD<br><div class="smaller">Flush  with Diamonds</div></td><td>�</td><td>Player 2</td>
</tr><tr><td><b>4</b></td><td>�</td><td>4D 6S 9H QH QC<br><div class="smaller">Pair of Queens<br>Highest card Nine</div></td><td>�</td><td>3D 6D 7H QD QS<br><div class="smaller">Pair of Queens<br>Highest card Seven</div></td><td>�</td><td>Player 1</td>
</tr><tr><td><b>5</b></td><td>�</td><td>2H 2D 4C 4D 4S<br><div class="smaller">Full House<br>With Three Fours</div></td><td>�</td><td>3C 3D 3S 9S 9D<br><div class="smaller">Full House<br>with Three Threes</div></td><td>�</td><td>Player 1</td>
</tr></table></div>
<p>The file, <a href="resources/documents/0054_poker.txt">poker.txt</a>, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.</p>
<p>How many hands does Player 1 win?</p>
"""

import euler_math as em
from collections import Counter

card_list = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

cards = {card_list[i]: i for i in range(1, len(card_list))}

def solve(debug=False):
    def card_nums(hand) -> list[int]:
        return sorted([cards[x[0]] for x in hand])[::-1]

    def is_flush(hand) -> bool:
        return all(x[1]==hand[0][1] for x in hand[1:])
    
    def is_straight(hand) -> bool :
        nums = card_nums(hand)
        for i in range(1, 5):
            if nums[i] != nums[i-1]-1:
                return False
        return True
    
    def find_mults(card_vals) -> dict:
        mults = Counter(card_vals)
        pairs = []
        triples = []
        quads = []
        for val, ct in mults.items():
            if ct == 2:
                pairs.append(val)
            elif ct == 3:
                triples.append(val)
            elif ct == 4:
                quads.append(val)
        return {2:pairs, 3:triples, 4:quads}
            
    def highcard(vals1, vals2):
        for i in range(5):
            if vals1[i] > vals2[i]:
                return 1
            elif vals1[i] < vals2[i]:
                return 2
        raise ValueError(f"\nNeither hand wins at highcard:\n1) {vals1}\n  vs  \n2) {vals2}")
        return None
    
    def determine_hand(hand):
        straight = is_straight(hand)
        flush = is_flush(hand)
        vals = card_nums(hand)
        mults = find_mults(vals)
        
        # if debug:
        #     print(mults)

        if straight and flush:
            return ['STRAIGHT_FLUSH', *vals]
        elif mults[4]:
            return ['4_OF_A_KIND', mults[4], *vals]
        elif mults[3] and mults[2]:
            return ['FULL_HOUSE', mults[3], mults[2]]
        elif flush:
            return ['FLUSH', *vals]
        elif straight:
            return ['STRAIGHT', *vals]
        elif mults[3]:
            return ['3_OF_A_KIND', mults[3], *vals]
        elif len(mults[2])==2:
            return ['2_PAIR', max(mults[2]), min(mults[2]), *vals]
        elif mults[2]:
            return ['PAIR', mults[2], *vals]
        else:
            return ['HIGH_CARD', *vals]

    result_order_list = ['STRAIGHT_FLUSH', '4_OF_A_KIND', 'FULL_HOUSE', 'FLUSH', 'STRAIGHT', '3_OF_A_KIND', '2_PAIR', 'PAIR', 'HIGH_CARD']
    result_order = {res:i for i, res in enumerate(result_order_list[::-1])}


    def game_result(game: list[str]):
        hand1 = game[:5]
        p1 = determine_hand(hand1)

        hand2 = game[5:]
        p2 = determine_hand(hand2)

        # print(hand1, p1)
        # print(hand2, p2)

        return p1, p2


    with open('solutions/problem54.txt', 'r') as f:
        poker_games = [x.strip().split(' ') for x in f.readlines()]


    
    
    if debug:
        test_hands = [
            '5H 5C 6S 7S KD', 
            '2C 3S 8S 8D TD', 
            '5D 8C 9S JS AC', 
            '2C 5C 7D 8S QH', 
            '2D 9C AS AH AC', 
            '3D 6D 7D TD QD', 
            '4D 6S 9H QH QC', 
            '3D 6D 7H QD QS', 
            '2H 2D 4C 4D 4S', 
            '3C 3D 3S 9S 9D', 
            'TD KD AD QD JD', 
            'KS KS KS KS 2H',
            '3C 5C AC TC JC',
            '5C 8D 6H 4C 7D'
        ]
        poker_games = [[*test_hands[i].split(' '), *test_hands[i+1].split(' ')] for i in range(0,14,2)]
        print(poker_games)
        for th in test_hands:
            test_hand = th.split(' ')
            test_res = determine_hand(test_hand)
            print(test_hand, test_res)
        


    res_list = []
    p1_wins = 0
    
    for g in poker_games:
        p1, p2 = game_result(g)
        s1 = result_order[p1[0]]
        s2 = result_order[p2[0]]

        if debug:
            print()
            print(f"Player 1: {p1} - {g[0:5]}")
            print(f"Player 2: {p2} - {g[5:10]}")
            
        if s1 > s2:
            p1_wins += 1
            if debug:
                print(f"Player 1 wins {s1} > {s2}")
        elif s2 > s1 and debug:
            print(f"Player 2 wins  {s1} < {s2}")
        elif s1 == s2:
            for j in range(1, len(p1)):
                if p1[j] > p2[j]:
                    p1_wins += 1
                    if debug:
                        print("Player 1 wins")
                    break
                elif p1[j] < p2[j]:
                    if debug:
                        print("Player 2 wins")
                    break 
        
        if p1 == p2:
            raise ValueError("Can't have equal hands!")

        res_list.append(p1[0])
        res_list.append(p2[0])



    print(Counter(res_list))

    res=p1_wins
    
    print(f"*** Answer: {res} ***")