
def my_gcd(a, b):
	"""
	int*int -> int
	"""

	while b != 0:
		tempo = b

		b = a % b

		a = tempo

	return a
