"""<p>The following iterative sequence is defined for the set of positive integers:</p>
<ul style="list-style-type:none;">
<li>$n \to n/2$ ($n$ is even)</li>
<li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
<p>Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
<p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>

"""

import euler_math as em

def next_collatz(n):
    if n % 2 == 1:
        return 3*n + 1
    else:
        return n // 2
    
def solve(debug=False):
    
    chains = {1:1}
    
    res = (1,1)
    
    for n in range(1,10**6):
        t = 0
        
        x = n
        while x not in chains:
            x = next_collatz(x)
            t += 1
        
        t += chains[x]
        chains[n] = t
        
        if t > res[1]:
            res = (n, t)
            if debug:
                print(f'N={res[0]} yields {res[1]}')
    
    
    print(f'***N={res[0]} yields {res[1]}***')
        
        
        
        
    