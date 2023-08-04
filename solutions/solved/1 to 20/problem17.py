"""<p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
<p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? </p>
<br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.</p>
"""

import euler_math as em

def solve(debug=False):
    
    # nums_to_19 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    nums_to_19_txt = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    nums_to_19_lens = [len(s) for s in nums_to_19_txt]
    
    # nums_by_10 = [20, 30, 40, 50, 60, 70, 80, 90]
    nums_by_10_txt = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    nums_by_10_lens = [len(s) for s in nums_by_10_txt]
    
    hundred_len = len('hundred')
    thousand_len = len('thousand')
    
    max_n = 1000
    
    def letter_count_sub_100(n):
        if n < 20:
            return nums_to_19_lens[n]
        elif n < 100:
            ones = n % 10
            tens = n // 10
            return nums_by_10_lens[tens] + nums_to_19_lens[ones]
        elif n == 1000:
            return 3+thousand_len
        elif n % 100 == 0:
            h = n // 100
            return nums_to_19_lens[h] + hundred_len
        else:
            # x hundred something
            h = n // 100
            m = n % 100
            tot = nums_to_19_lens[h] + hundred_len + 3 + letter_count_sub_100(m)
            if debug:
                if m < 20:
                    m_txt = nums_to_19_txt[m]
                else:
                    m_txt = nums_by_10_txt[m//10]
                    if m % 10 > 0:
                        m_txt += nums_to_19_txt[m % 10]
                ntxt = f"{nums_to_19_txt[h]} hundred and {m_txt}"
                nlen = len(ntxt.replace(' ', ''))
                assert(tot == nlen)
                print(f'{n} ({tot}) = {ntxt} ({nlen})')
            return tot
    
    try:
        assert(letter_count_sub_100(342)==23)
        assert(letter_count_sub_100(115)==20)
    except AssertionError as e:
        print(342, letter_count_sub_100(342))
        print(115, letter_count_sub_100(115))
        raise e
    
    res = sum(letter_count_sub_100(x) for x in range(1,max_n+1))
    print(res)