# https://projecteuler.net/problem=74
"""<p>The number $145$ is well known for the property that the sum of the factorial of its digits is equal to $145$:
$$1! + 4! + 5! = 1 + 24 + 120 = 145.$$</p>
<p>Perhaps less well known is $169$, in that it produces the longest chain of numbers that link back to $169$; it turns out that there are only three such loops that exist:</p>
\begin{align}
&amp;169 \to 363601 \to 1454 \to 169\\
&amp;871 \to 45361 \to 871\\
&amp;872 \to 45362 \to 872
\end{align}
<p>It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,</p>
\begin{align}
&amp;69 \to 363600 \to 1454 \to 169 \to 363601 (\to 1454)\\
&amp;78 \to 45360 \to 871 \to 45361 (\to 871)\\
&amp;540 \to 145 (\to 145)
\end{align}
<p>Starting with $69$ produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.</p>
<p>How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?</p>

"""

import euler_math as em
from solutions.euler_tools import get_digits

def solve(debug=False):
    
    res=0
    digit_factorials = [em.factorial(d) for d in range(0, 10)]
    
    def chain(x):
        return sum(digit_factorials[d] for d in get_digits(x))
    
    over_sixty = set()
    under_sixty = {
        169: 3, 363601: 3, 1454: 3, 
        871: 2, 45361: 2, 
        872: 2, 45362: 2
    }
    
    lng = 0
    
    for x in range(1, 1_000_000):
        f_chain = [x]
        
        while True:
            z = f_chain[-1]
            if len(f_chain) > 1 and z == f_chain[-2]:
                for i, c in enumerate(f_chain):
                    under_sixty[c] = len(f_chain)-i
                break
            
            if z in over_sixty:
                for c in f_chain:
                    over_sixty.add(z)
                break
            
            elif z in under_sixty:
                rem_terms = under_sixty[z]-1
                for i, c in enumerate(f_chain):
                    term_ct = len(f_chain) - i + rem_terms
                    under_sixty[c] = term_ct
                    if term_ct == 60:
                        res += 1
                break
                
            f_chain.append(chain(f_chain[-1]))
        
        try:
            if debug and under_sixty[x] > lng:
                lng = under_sixty[x]
                print(f"Chaining from {x} produces {lng} terms")
        except:
            print(x, sorted(under_sixty.keys()))
            quit()
        
    if len(over_sixty) > 0:
        raise AssertionError("Got starting terms with more than 60 symbols:\n", over_sixty)
    
    if under_sixty[69] != 5:
        raise AssertionError("Expect chain count for '69' to be 5, got", under_sixty[69],"instead")
    
    print(f"*** Answer: {res} ***")