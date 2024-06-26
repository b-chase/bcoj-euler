# https://projecteuler.net/problem=89
"""<p>For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.</p>
<p>For example, it would appear that there are at least six ways of writing the number sixteen:</p>
<p class="margin_left monospace">IIIIIIIIIIIIIIII<br>
VIIIIIIIIIII<br>
VVIIIIII<br>
XIIIIII<br>
VVVI<br>
XVI</p>
<p>However, according to the rules only <span class="monospace">XIIIIII</span> and <span class="monospace">XVI</span> are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.</p>
<p>The 11K text file, <a href="resources/documents/0089_roman.txt">roman.txt</a> (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see <a href="about=roman_numerals">About... Roman Numerals</a> for the definitive rules for this problem.</p>
<p>Find the number of characters saved by writing each of these in their minimal form.</p>
<p class="smaller">Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.</p>

"""

import euler_math as em
from euler_tools.math import roman_numeral_to_int, int_to_roman_numeral


def solve(debug=False):
    # print(inv_roman_numerals)
    with open('solutions/problem89.txt') as f:
        roman_nums = [x.strip() for x in f.readlines()]
    
    res = 0
    
    for rn in roman_nums:
        num_val = roman_numeral_to_int(rn)
        fixed_rn = int_to_roman_numeral(num_val)
        if fixed_rn != rn:
            res += (len(rn) - len(fixed_rn))
        # print(rn, num_val, fixed_rn, rn==fixed_rn)
    
    
    print(f'*** Answer: {res} ***')