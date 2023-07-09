"""<p>The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
<p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.</p>
<p>Using <a href="resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p>
"""

import euler_math as em


def is_tri(tn: int) -> bool:
    n = em.int_sqrt(2*tn)
    numer = (n**2 + n)
    return numer % 2 == 0 and numer // 2 == tn 


def solve(debug=False):
    
    res=None

    with open("solutions/problem42.txt") as f:
        wordlist = [w.strip(' "') for w in f.read().split(',')]

    def word_value(w:str) -> int :
        return sum(ord(c)-64 for c in w)

    res = 0
    tns = set()
    for w in wordlist:
        v = word_value(w)
        if v in tns:
            res += 1
        elif is_tri(v):
            tns.add(v)
            res += 1

    print(f"*** Answer: {res} ***")