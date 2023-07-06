"""<p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
<div class="center">
<img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
<p>How many such routes are there through a $20 \times 20$ grid?</p>

"""

import euler_math as em

def solve(debug=False):
    
    paths = {(0,0): 1, (1,0): 1, (0,1): 1}
    
    def find_paths(h,w):
        # determine number of paths in square grid of dimensions h (rows) by w (cols)
        # there's a faster way to do this using symmetry, but would be complex to code
        if h == 0 or w == 0:
            return 1
        
        if (h,w) in paths:
            return paths[(h,w)]
        
        res = find_paths(h-1, w) + find_paths(h, w-1)
        paths[(h,w)] = res
        return res
        
    print(find_paths(20,20))
    