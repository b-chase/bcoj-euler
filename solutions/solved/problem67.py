# https://projecteuler.net/problem=67
"""<p>By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.</p>
<p class="monospace center"><span class="red"><b>3</b></span><br><span class="red"><b>7</b></span> 4<br>
2 <span class="red"><b>4</b></span> 6<br>
8 5 <span class="red"><b>9</b></span> 3</p>
<p>That is, 3 + 7 + 4 + 9 = 23.</p>
<p>Find the maximum total from top to bottom in <a href="resources/documents/0067_triangle.txt">triangle.txt</a> (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.</p>
<p class="smaller"><b>NOTE:</b> This is a much more difficult version of <a href="problem=18">Problem 18</a>. It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)</p>

"""

import euler_math as em

def solve(debug=False):
    
    with open("solutions/problem67.txt") as f:
        triangle_rows = [[int(x.strip()) for x in l.split(' ')] for l in f.readlines()]

    res = triangle_rows[-1]
    for row in triangle_rows[-2::-1]:
        if debug:
            print(res)
        res = [x+max(res[i], res[i+1]) for i,x in enumerate(row)]
    
    
    print(f"*** Answer: {res} ***")