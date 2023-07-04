"""<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$</p>
<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.</p>

"""

import euler_math as em


def solve():
	f = em.Fibonacci()
	even = 1
	res = 0
	while f.incr() < 4e6:
		even = (even+1) % 3
		try:
			if even == 0:
				assert f.num %2 == 0
				res += f.num
		except AssertionError:
			print("Error! F_n is not an even number!", even, f.n, f.num)	

	print(res)
	