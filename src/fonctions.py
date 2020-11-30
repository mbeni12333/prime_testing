import numpy as np
import matplotlib.pyplot as plt
import time

def my_gcd(a, b):
    """
    int*int -> int
    """
    a, b = max(a, b), min(a, b)
    while b != 0:
        tempo = b
        b = a % b
        a = tempo
    return a

def my_expo_mod(g, n, N):
    """
    int*int*int -> int
    return (g^n) % N
    """
    h = 1

    l = n.bit_length()

    #Note: on met la range jusqu'a -1 pour que i prenne aussi la valeur 0.
    for i in range(l - 1, -1, -1):
        h = (h**2) % N

        if (n >> i) & 1 == 1:
            h = (h * g) % N

    return h
    
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
    if(u0 == 1):
        return u1

    # si on trouve pas d'inverse
    print("a n'a pas d'inverse modulo N")

def first_test(N):
    """
    int*boolean
    test naiif de primalité
    complexité en O(sqrt(n))
    """

    for i in range(2, int(np.sqrt(N))+1):
        if(N%i == 0):
            return False
    return True

#critére korselt
def isCarmichael_facteurs(n, facteurs):
    """
    int*list->boolean
    tester si n est un nombre de carmichael, etant donné ses facteurs
    """
#    if n % 2 == 0:
#        return False

#    for i in range(2, int(np.sqrt(n))+1):
#        if first_test(i) and n%i == 0:
            # i est premier divise n
#            if n%(i**2) == 0:
#                return False
#            if (n-1)%(i-1) != 0:
#                return False
    for facteur in facteurs:
        # pas facteur premier carré
        if(n%(facteur**2) == 0):
            return False
        if((n-1)%(facteur-1) != 0):
            return False
    # pass le test
    return True

def isCarmichael(n):
    """
    """
    # n'est pas composé
    if(first_test(n)):
        return False
    
    for i in range(2, n):
        # (i premier avec n => i**(n-1) = 1[n])
        if (my_gcd(i, n) == 1) and (my_expo_mod(i, n-1, n) != 1):
            return False
    return True

def gen_carmichael(N=1e5, n_facteur_max=5):
    """
    int->int
    """
    premiers = [i for i in range(3, int(N), 2) if first_test(i)]
    
    nb_facteur = 3
    
    indexes = list(range(len(premiers)))
    while True:  
        np.random.shuffle(indexes)
        acc = [premiers[indexes[i]]for i in range(nb_facteur)]
        n = np.prod(acc, dtype=np.int64)
        #print(n)
        if isCarmichael_facteurs(n, acc):

            return n

def test_fermat(n, a):
	"""
	n un entier impair, a un entier entre 2 et n - 1.

	Retourne vrai si premier possible
	faux si composé

	"""
	b = my_expo_mod(a, n-1, n)

	if b != 1:
		return False

	return True

def test_miller_rabin(n, T=10):
    """
    int: n = 1 + 2**h *m
    """
    h=0
    temp = n-1
    while temp%2 == 0:
        temp = temp//2
        h += 1
    m = (n-1)//2**h

    for i in range(1, T):
        a = np.random.randint(2, n-2)
        b = my_expo_mod(a, m, n)
        if b==1 and b==(n-1):
            continue
        for j in range(h-1):
            b = my_expo_mod(b, 2, n)
            if b == (n-1): 
                break
        if b != (n-1):
            return False
    return True