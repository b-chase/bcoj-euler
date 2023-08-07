# https://projecteuler.net/problem=83
"""<p class="small_notice">NOTE: This problem is a significantly more challenging version of <a href="problem=81">Problem 81</a>.</p>
<p>In the $5$ by $5$ matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to $2297$.</p>
<div class="center">
$$
\begin{pmatrix}
\color{red}{131} &amp; 673 &amp; \color{red}{234} &amp; \color{red}{103} &amp; \color{red}{18}\\
\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; \color{red}{150}\\
630 &amp; 803 &amp; 746 &amp; \color{red}{422} &amp; \color{red}{111}\\
537 &amp; 699 &amp; 497 &amp; \color{red}{121} &amp; 956\\
805 &amp; 732 &amp; 524 &amp; \color{red}{37} &amp; \color{red}{331}
\end{pmatrix}
$$
</div>
<p>Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in <a href="resources/documents/0083_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.</p>
"""

import euler_math as em
from math import inf

def solve(debug=False):
    
    with open('solutions/problem83.txt') as f:
        matrix = [[int(x) for x in row.strip().split(',')] for row in f.readlines()]
    
    N = len(matrix)

    # initiate scores with matrix of infinities
    scored_matrix = [[inf for _c in range(N)] for _r in range(N)]
    scored_matrix[0][0] = matrix[0][0]

    # working matrix, will adjust then write to scored matrix
    tmp_matrix = [[*row] for row in scored_matrix]

    def get_cell(coord: tuple, from_vals=matrix):
        row, col = coord
        if row < 0 or row >= N or col < 0 or col >= N:
            return inf
        else:
            return from_vals[row][col]

    def set_cell(coord: tuple, new_value, target_matrix=tmp_matrix):
        row, col = coord
        if row < 0 or row >= N or col < 0 or col >= N:
            pass
        else:
            target_matrix[row][col] = new_value


    def optimize_path(coord) -> list:
        # replaces the value of the given cell in the working matrix if it is 
        row, col = coord
        cell_val = get_cell(coord, matrix)
        current_score = get_cell(coord, scored_matrix)

        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        neighbor_scores = [get_cell(nb_coord, scored_matrix) for nb_coord in neighbors]
        new_score = min(neighbor_scores) + cell_val

        if new_score < current_score:
            set_cell(coord, new_score, tmp_matrix)
            return neighbors
        else:
            return []
        
    
    check_cells = [(0,0), (0,1), (1,0)]
    round = 0

    while len(check_cells) > 0:
        new_to_check = []
        # tmp_matrix = [[*row] for row in scored_matrix]
        round += 1
        for check_coord in check_cells:
            opt_result = optimize_path(check_coord)
            new_to_check.extend(opt_result)

        check_cells = set(new_to_check)
        scored_matrix = [[*row] for row in tmp_matrix]
        if debug:
            count_inf = sum(sum(1 for x in row if x==inf) for row in scored_matrix)
            print(f"Round {round}: min path score is {scored_matrix[-1][-1]}  ({count_inf} total unreached)")
            # for i in range(0,5):
            #     print(f">>  {scored_matrix[i][0:5]}")


    res = scored_matrix[-1][-1]
    
    print(f'*** Answer: {res} ***')