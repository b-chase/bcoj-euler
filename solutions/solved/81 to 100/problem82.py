# https://projecteuler.net/problem=82
"""<p class="small_notice">NOTE: This problem is a more challenging version of <a href="problem=81">Problem 81</a>.</p>
<p>The minimal path sum in the $5$ by $5$ matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to $994$.</p>
<div class="center">
$$
\begin{pmatrix}
131 &amp; 673 &amp; \color{red}{234} &amp; \color{red}{103} &amp; \color{red}{18}\\
\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; 150\\
630 &amp; 803 &amp; 746 &amp; 422 &amp; 111\\
537 &amp; 699 &amp; 497 &amp; 121 &amp; 956\\
805 &amp; 732 &amp; 524 &amp; 37 &amp; 331
\end{pmatrix}
$$
</div>
<p>Find the minimal path sum from the left column to the right column in <a href="resources/documents/0082_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.</p>
"""

import euler_math as em
from math import inf

def solve(debug=False):
    
    with open('solutions/problem82.txt') as f:
        matrix = [[int(x) for x in row.strip().split(',')] for row in f.readlines()]
    
    N = len(matrix)

    saved_paths = dict()

    def get_cell(row,col):
        try:
            val = matrix[row][col]
        except IndexError as e:
            val = inf
        return val
    

    for j in range(1,N):
        # first get paths from left
        col_vals = [row[j] for row in matrix]  # original values
        for i in range(0,N):
            cell_value = col_vals[i]
            new_value = get_cell(i, j-1) + cell_value
            matrix[i][j] = new_value

        # then check paths above/below for faster numbers
        moved = True
        while moved:
            # loop until no more optimization to be done
            moved = False
            for i in range(0,N):
                cell_value = col_vals[i]  # original value
                cell_new_value = get_cell(i,j)
                val_up = get_cell(i-1,j) + cell_value  # using matrix value from above plus current
                val_down = get_cell(i+1,j) + cell_value  # using matrix value from below plus current

                # replace with above/below value and loop again until nothing gets changed
                min_vert_val = min(val_up, val_down)
                if min_vert_val < cell_new_value:
                    moved = True
                    matrix[i][j] = min_vert_val
        
    
    res = min(row[-1] for row in matrix)
    
    print(f'*** Answer: {res} ***')