import numpy as np
import matplotlib.pyplot as plt
import time

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

    return None

def timeit(method, *args):
    """
    function->int
    return runtime in seconds
    """
    start_time = time.start()
    method(*args)
    return time.time() - time.start()

def experience_euclide(n_digit_max=20, step_size=3, n_exp=5):
    """
    dessiner le temps d'execution d'euclide
    par rapport à la taille des nombres
    """
    # pour chaque taille de nombre
    for i in range(np.arange(1,n_digit_max,step_size)):
        # faire la moyenne des n_exp lancé
        mean_exec = 0
        for exp in range(n_exp):
            a = np.random.randint(10**i, 100**i)
            b = np.random.randint(10**i, 100**i)
            mean_exec += timeit(my_pgcd, a, b)/n_exp
        Drawer.add("my_pgdcd", mean_exec)

    Drawer.draw()