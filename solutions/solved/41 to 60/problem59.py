# https://projecteuler.net/problem=59
"""<p>Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.</p>
<p>A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.</p>
<p>For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.</p>
<p>Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.</p>
<p>Your task has been made easy, as the encryption key consists of three lower case characters. Using <a href="resources/documents/0059_cipher.txt">0059_cipher.txt</a> (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.</p>

"""

import euler_math as em

def solve(debug=False):
    
    res=None

    with open('solutions/problem59.txt', 'r') as f:
        coded = [int(x.strip()) for x in f.read().split(',')]

    possible_codes = [[]]
    a_ord = ord('a')
    for _ in range(3):
        new_codes = []
        for i in range(26):
            new_codes += [x+[a_ord+i] for x in possible_codes]
        possible_codes = new_codes


    for try_code in possible_codes:
        deciphered_ords = [x ^ try_code[i%3] for i,x in enumerate(coded)]
        words = (''.join(chr(x) for x in deciphered_ords)).split(' ')
        if 'the' in words:
            print(try_code, words)
            check = input('Is this the answer? y/n')
            if check == 'y':
                real_key = [chr(x) for x in try_code]
                print('Key was: ', real_key)
                res = sum(ord(c) for c in ' '.join(words))
                break

    
    print(f"*** Answer: {res} ***")