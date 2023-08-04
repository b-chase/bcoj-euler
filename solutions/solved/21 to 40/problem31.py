"""<p>In the United Kingdom the currency is made up of pound (�) and pence (p). There are eight coins in general circulation:</p>
<blockquote>1p, 2p, 5p, 10p, 20p, 50p, �1 (100p), and �2 (200p).</blockquote>
<p>It is possible to make �2 in the following way:</p>
<blockquote>1ף1 + 1�50p + 2�20p + 1�5p + 1�2p + 3�1p</blockquote>
<p>How many different ways can �2 be made using any number of coins?</p>

"""

import euler_math as em

def solve(debug=False):
    
    # dict with tuple keys: (largest_coin, remainder)
    pre_solved = {}
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_set = set(coins)
    
    total = 200
    
    def count_ways(rem, coins_left):
        next_coin = coins_left[-1]
        
        key = (rem, next_coin)
        
        if key in pre_solved:
            return pre_solved[key]
        
        res = 0
        
        if next_coin == 1:
            res = 1
            
        elif next_coin > rem:
            res = count_ways(rem, coins_left[:-1])
        
        elif rem == next_coin:
            res = 1 + count_ways(rem, coins_left[:-1])
        
        else:
            new_rem = rem - next_coin
            rem_ways = count_ways(new_rem, coins_left)
            if len(coins_left) > 1:
                rem_ways += count_ways(rem, coins_left[:-1])
            res = rem_ways

        if debug:
            print(rem, coins_left, res)
        
        pre_solved[key] = res
        
        return res
    
    
    final = count_ways(total, coins)
    print(final)
        
        
        
    