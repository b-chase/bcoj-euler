# https://projecteuler.net/problem=68
"""<p>Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.</p>
<div class="center">
<img src="resources/images/0068_1.png?1678992052" class="dark_img" alt=""><br></div>
<p>Working <b>clockwise</b>, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.</p>
<p>It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.</p>
<div class="center">
<table width="400" cellspacing="0" cellpadding="0"><tr><td width="100"><b>Total</b></td><td width="300"><b>Solution Set</b></td>
</tr><tr><td>9</td><td>4,2,3; 5,3,1; 6,1,2</td>
</tr><tr><td>9</td><td>4,3,2; 6,2,1; 5,1,3</td>
</tr><tr><td>10</td><td>2,3,5; 4,5,1; 6,1,3</td>
</tr><tr><td>10</td><td>2,5,3; 6,3,1; 4,1,5</td>
</tr><tr><td>11</td><td>1,4,6; 3,6,2; 5,2,4</td>
</tr><tr><td>11</td><td>1,6,4; 5,4,2; 3,2,6</td>
</tr><tr><td>12</td><td>1,5,6; 2,6,4; 3,4,5</td>
</tr><tr><td>12</td><td>1,6,5; 3,5,4; 2,4,6</td>
</tr></table></div>
<p>By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.</p>
<p>Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum <b>16-digit</b> string for a "magic" 5-gon ring?</p>
<div class="center">
<img src="resources/images/0068_2.png?1678992052" class="dark_img" alt=""><br></div>

"""

import euler_math as em
from euler_tools.math import permute_down

def solve(debug=False):
    
    def is_magic3(seq) -> bool:
        b1 = [0, 1, 2]
        b2 = [3, 2, 4]
        b3 = [5, 4, 1]
        branches = [b1, b2, b3]
        
        fix_seq = seq
        
        if seq[0] > min(fix_seq[b[0]] for b in branches):
            return None
        
        sums = [sum(fix_seq[i] for i in branch) for branch in branches]
        
        if all(s == sums[0] for s in sums[1:]):
            str_rep = ''.join(''.join(str(fix_seq[i]) for i in b) for b in branches)
            return str_rep
        else:
            return None
        
    # nums3 = [4, 6, 5, 3, 2, 1]
    
    # t = True
    # high = 0
    # while t:
    #     tmp = is_magic3(nums3)
    #     if tmp:
    #         print(nums3)
    #         high = max(high, int(tmp))
    #     if not permute_down(nums3):
    #         break
    
    # print(high)

    nums = [6, 9, 8, 7, 5, 4, 3, 2, 1, 0]
    
    def is_magic5(seq):
        b1 = [0, 1, 2]
        b2 = [3, 2, 4]
        b3 = [5, 4, 6]
        b4 = [7, 6, 8]
        b5 = [9, 8, 1]
        branches = [b1, b2, b3, b4, b5]
        
        fix_seq = [10 if x == 0 else x for x in seq]
        # for 16-digits, 10 needs to be in an outer node
        if not any(fix_seq[b[0]]==10 for b in branches):
            return None
        
        if seq[0] > min(fix_seq[b[0]] for b in branches):
            return None

        sums = [sum(fix_seq[i] for i in branch) for branch in branches]
        
        if all(s == sums[0] for s in sums[1:]):
            str_rep = ''.join(''.join(str(fix_seq[i]) for i in b) for b in branches)
            return str_rep
        else:
            return None
    
    t = True
    res = 0
    while t:
        tmp = is_magic5(nums)
        if tmp:
            res = max(int(tmp), res)
            break
        
        if not permute_down([*nums[1:]]) and res > 0:
            break
            
        t = permute_down(nums)
        if not t:
            print("Error, couldn't permute any further")
            break
            
        if debug:
            print(nums)
    
    
    
    print(f"*** Answer: {res} ***")