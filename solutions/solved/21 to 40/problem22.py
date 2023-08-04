"""<p>Using <a href="resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
<p>For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.</p>
<p>What is the total of all the name scores in the file?</p>

"""

import euler_math as em

with open('solutions/problem22.txt', 'r') as f:
    name_list = [name.strip(' "').upper() for name in f.read().split(',')]


def solve(debug=False):
    
    name_list.sort()
    
    res = 0
    
    for i, name in enumerate(name_list):
        name_score = sum(ord(c)-64 for c in name)
        res += name_score*(i+1)
        
    print(res)