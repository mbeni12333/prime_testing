
def my_gcd(a, b):
	"""
	int*int -> int
	"""

	while b != 0:
		tempo = b

		b = a % b

		a = tempo

	return a

def my_expo_mod(g, n, N):
	"""
	int*int*int -> int
	retourn (g^n) % N
	"""
	h = 1

	l = n.bit_length()

	#Note: on met la range jusqu'a -1 pour que i prenne aussi la valeur 0.
	for i in range(l - 1, -1, -1):
		h = (h**2) % N

		if (n >> i) & 1 == 1:
			h = (h * g) % N

	return h
