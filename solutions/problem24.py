"""<p>A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:</p>
<p class="center">012� �021� �102� �120� �201� �210</p>
<p>What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?</p>

"""

import euler_math as em
from math import factorial

def solve(debug=False):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    perm_n = 1_000_000

    rem = perm_n

    answer = [-1]*10

    for place in range(10):
        print(answer, rem)
        for d in digits:
            answer[place] = d
            perms = factorial(10-place-1)
            if perms >= rem:
                digits.remove(d)
                # print(f"{10-place-1}! = {perms} > {rem}")
                break
            # elif rem == 0:
            #     print(''.join(str(x) for x in answer))
            #     return
            else:
                rem -= perms

    print(''.join(str(x) for x in answer))
    
