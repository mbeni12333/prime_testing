from Drawer import Drawer
import numpy as np
import matplotlib.pyplot as plt
import time
from fonctions import *
import random

def timeit(method, *args):
    """
    function->int
    return runtime in seconds
    """
    start_time = time.time()
    method(*args)
    return time.time() - start_time

def experience_euclide(n_digit_max=128, step_size=2, n_exp=10):
    """
    dessiner le temps d'execution d'euclide
    par rapport à la taille des nombres
    """
    drawer = Drawer()
    
    # pour chaque taille de nombre
    for i in range(1,n_digit_max,step_size):
        # faire la moyenne des n_exp lancé
        mean_exec = 0
        for exp in range(n_exp):
            #a = np.random.randint(10**i, 100**i, dtype=np.ulonglong)
            #b = np.random.randint(10**i, 100**i, dtype=np.ulonglong)
            a = random.getrandbits(i+1)
            b = random.getrandbits(i)
            mean_exec += timeit(my_gcd_etendu, a, b)/n_exp
        drawer.add(name="my_gcd", time=mean_exec, size=i)
    drawer.draw()

def experience_comptage_premier_naiif(N=1e5):
    """
    int->int
    nombre de nombre premier inferieur à N
    """
    cpt = 0
    for i in range(N):
        if first_test(i):
            cpt += 1
    return cpt


if __name__ == "__main__":
    experience_euclide(4086, 32, 10)