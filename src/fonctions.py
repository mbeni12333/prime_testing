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

    if n < 0:
        # puissance negative
        gcd, _, v = my_gcd_etendu(N, g)
        g = v
        n = -n

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

    return tuple(map(int, u))

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
    print(f"{a} n'a pas d'inverse modulo {N}")

def my_inverse_bezout(a, N):
    """
    calcul pgcd etendu, ou remonté
    """
    u0, u1, u2 = my_gcd_etendu(a, N)
    if(u0 == 1):
        return u2 if a<N else u1

    # si on trouve pas d'inverse
    print(f"{a} n'a pas d'inverse modulo {N}")
from math import sqrt
def first_test(N):
    """
    int -> boolean
    test naiif de primalité
    complexité en O(sqrt(n))
    """
    for i in range(2, int(sqrt(N))+1):
    #for i in range(2, int(np.sqrt(N))+1):
        if(N%i == 0):
            return False
    return True

#critére korselt
def isCarmichael_facteurs(n, facteurs):
    """
    int*list->boolean
    tester si n est un nombre de carmichael, etant donné ses facteurs
    """
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
    n_divisors = 0
    for i in range(2, n):
        # (i premier avec n => i**(n-1) = 1[n])
        gcd = my_gcd(i, n)
        if (gcd == 1) and (my_expo_mod(i, n-1, n) != 1):
            return False

        if n%i == 0:
            n_divisors += 1

    if n_divisors == 0:
        # n est premier 
        return False
    
    return True


def gen_carmichael(N=1e5):
    """
    int->int
    nombre de nombre premier inferieur à N
    """
    acc = []
    for i in range(int(N)):
        if isCarmichael(i):
            acc.append(i)

    return acc


def gen_carmichael3(N=1e5, n_facteur_max=5):
    """
    int->int
    """
    premiers = [i for i in range(3, int(N), 2) if first_test(i)]
    nb_facteur = 3

    while True:
        acc = [premiers[np.random.randint(0, len(premiers)-1)] for i in range(nb_facteur)]
        # n = np.prod(acc, dtype=np.int64)
        n = 1
        for a in acc:
            n*=a
        if isCarmichael_facteurs(n, acc):
            return n

def gen_carmichael_3_list(N=1e5, n_elements=10):
    """
    int->int
    """
    premiers = [i for i in range(3, int(N), 2) if first_test(i)]
    nb_facteur = 3
    T = []
    cpt = 0
    while cpt < n_elements:
        acc = [premiers[np.random.randint(0, len(premiers)-1)] for i in range(nb_facteur)]
        # n = np.prod(acc, dtype=np.int64)
        n = 1
        for a in acc:
            n*=a
        if isCarmichael_facteurs(n, acc):
            T.append(n)
            cpt += 1
            print(cpt)
    
    return T
def gen_carmichael32(N=1e5, n_facteur_max=5):
    """
    int->int
    """
    premiers = [i for i in range(3, int(N), 2) if first_test(i)]
    nb_facteur = 3
    indexes = list(range(len(premiers)))

    while True:  
        np.random.shuffle(indexes)
        acc = [premiers[indexes[i]] for i in range(nb_facteur)]
        n = np.prod(acc, dtype=np.int64)
        #print(n)
        if isCarmichael_facteurs(n, acc):
            return n

def test_fermat(n, a=None):
    """
    n un entier impair

    Retourne vrai si premier possible
    faux si composé

    """
    if a == None:
        a = random.randrange(2, n)

    return my_expo_mod(a, n-1, n) == 1


def test_miller_rabin(n, T=10):
    """
    int*int->boolean
    n = 1 + 2**h * m
    """

    p_h = 1
    temp = n-1
    while(temp%2 == 0):
        temp = temp // 2
        p_h *= 2
    m = (n-1)//p_h

    inf = n-3

    for i in range(T):
        a = 2 + random.getrandbits(n.bit_length())%(n-2)
        b = my_expo_mod(a, m, n)

        if b==1 or b==(n-1):
            continue

        for j in range(1, p_h):
            if b!=(n-1) and my_expo_mod(b, 2, n)==1:
                return False
            elif  b==(n-1):
                break
            b = my_expo_mod(b, 2, n)
        
        if b != (n-1):
            return False
    
    return True

import random
def gen_rsa(t):
    """
    int: longeur en bits (doit être supérieur a 2)
    return: (e, n), (d, n)
    """

    inf = 1<<(t-1)

    while True:
        p = inf + random.getrandbits(t-1)
        if test_miller_rabin(p):
            break
    while True:
        q = inf + random.getrandbits(t-1)
        if test_miller_rabin(q) and q != p:
            break

    return p, q, p*q


def RSA(t):
    """
    return public_key, private_key
    """
    p, q, n = gen_rsa(t)

    # phi (nombre de nombres premier avec n, < n)
    phi = (p-1)*(q-1)

    while True:
        e = 2 + random.getrandbits(phi.bit_length())%(phi-3)
        gcd, _, d = my_gcd_etendu(phi, e)
        if(gcd == 1):
            break
    
    return (e, n), (d, n)

def encode(m, public_key):
    """
    (e, n)
    """

    return [my_expo_mod(ord(c), *public_key) for c in m]

def decode(m, private_key):
    """
    (d, n)
    """
    return ''.join([chr(my_expo_mod(c, *private_key)) for c in m])
    
