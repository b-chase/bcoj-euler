"""<p>An irrational decimal fraction is created by concatenating the positive integers:
$$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$</p>
<p>It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.</p>
<p>If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
$$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$</p>
"""

import euler_math as em

def solve(debug=False):
    # 1-digit numbers: 9  (1-9)
    # 2-digit numbers: 90  (10-99)
    # 3-digit numbers: 900 (100-999)

    res=0

    def chap_digit(d):
        digit_count = 0
        digits_per = 0
        num_to = 0
        added_nums = 0

        while digit_count < d:
            digits_per += 1
            added_nums = 9 * 10**(digits_per-1)
            num_to += added_nums
            digit_count += added_nums * digits_per
            
        extra_digits = digit_count - d  # 189 - 12 = 177
        nums_back = extra_digits // digits_per  # 177 // 2 == 88
        check_num = num_to - nums_back  # 99 - 88 == 11
        digit_of_checked = 1 + extra_digits % digits_per  # 177 % 2 == 1

        answer = str(check_num)[-digit_of_checked]  # '11'[-1] = 1

        if debug:
            print(d, extra_digits, nums_back, check_num, digit_of_checked, answer)

        return int(answer)
    
    res = 1
    for dpot in range(0, 7):
        res *= chap_digit(10**dpot)

    
    
    print(f"*** Answer: {res} ***")