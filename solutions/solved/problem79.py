# https://projecteuler.net/problem=79
"""<p>A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.</p>
<p>The text file, <a href="resources/documents/0079_keylog.txt">keylog.txt</a>, contains fifty successful login attempts.</p>
<p>Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.</p>

"""

import euler_math as em
from itertools import pairwise
import multiprocessing as mp



def solve(debug=False):
    
    res=None
    
    with open('solutions/problem79_keylog.txt') as keylog:
        keys = [x.strip() for x in keylog.readlines()]
    
    def key_match(full_code:str, key:str) -> bool:
        indices = []
        code_min_index = 0
        for k in key:
            tmp_i = full_code[code_min_index:].find(k)
            if tmp_i == -1:
                return False
            indices.append(tmp_i + code_min_index)
            code_min_index += tmp_i
        
        return all(ka < kb for ka,kb in pairwise(indices))
    
    z = 1
    
    must_have_digits = set()
    for k in keys:
        must_have_digits.update(set(k))
    
    test_keys = keys[0:20]
    while True:
        sz = str(z)
        if len(must_have_digits.difference(set(sz))) == 0:
            if all(key_match(sz, k) for k in test_keys):
                break
            
        z += 1
        
    print(f"MATCH FOUND: Code '{z}' with keys={test_keys}")
    
    print(f"*** Answer: {res} ***")