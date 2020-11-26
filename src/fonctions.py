import numpy as np
import matplotlib.pyplot as plt
import time
from .Drawer import Drawer

def my_gcd(a, b):
	"""
	int*int -> int
	"""
	while b != 0:
		tempo = b
		b = a % b
		a = tempo
	return a

def my_gcd_etendu(a, b):
    """
    int*int-> int*int*int
    return pgcd + u, v
    """
    a, b = max(a, b), min(a, b)
    u = np.array([a, 1, 0])
    v = np.array([b, 0, 1])

    while(v[0] != 0):
        q = u[0]//v[0]
        temp = v
        v = u - q*v
        u = temp

    return tuple(u)

def my_inverse(a, N):
    """
    int*int->int
    retourner inverse de a modulo N
    """
    # tester tout les nombres
    for b in range(N):
        if(((a*b) % N) == 1):
            return b
    # si on trouve pas d'inverse
    print("a n'a pas d'inverse modulo N")

def my_inverse_bezout(a, N):
    """
    calcul pgcd etendu, ou remonté
    """
    u0, u1, u2 = my_gcd_etendu(a, N)
    print(my_gcd_etendu(a, N))
    if(u0 == 1):
        return u1

    # si on trouve pas d'inverse
    print("a n'a pas d'inverse modulo N")


