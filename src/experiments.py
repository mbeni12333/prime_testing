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
    for i in range(2, int(N)):
        if first_test(i):
            cpt += 1
    return cpt


def experience_carmichael(N=1e5):
    """
    int
    """
    cpt = 0
    for i in range(int(N)):
        if isCarmichael(i):
            print(i)
            cpt += 1
    return cpt
    
def experience_carmichael_t(tmax=5*60*60):
    start_time = time.time()
    i = 0

    while(time.time() - start_time < tmax):
        i += 1
        if isCarmichael(i):
            print(i)

def experience_gen_carmichael_3(N=10000):
    """
    """
    premiers = [i for i in range(3, N, 2) if first_test(i)]
    maxn = (0, [])

    for i in range(len(premiers)):
        for j in range(i+1, len(premiers)):
            for k in range(j+1, len(premiers)):
                n = premiers[i]*premiers[j]*premiers[k]
                if(isCarmichael_facteurs(n, [premiers[i], premiers[j], premiers[k]])):
                    if(n > maxn[0] ):
                        maxn = (n, [premiers[i], premiers[j], premiers[k]])
                        print(n ," = ", "x".join(map(str, [premiers[i], premiers[j], premiers[k]])))
    return maxn


def estimate_proba_test_fermat(n, maxSize=100000, mode=0):
	"""
	Entrées:
		n : Nombre de test
		maxSize : Taille maximum des valeurs testés
		mode:
			0 = Nombre généré par gen_carmichael
			1 = Nombre composé
			2 = Aléatoire

		Ne retourne rien mais print la probabilité de succes estimé.
	"""
	error_counter = 0
		
	for i in range(n):

		if mode == 0:
			prime = gen_carmichael(maxSize)
			#Random a ou bien un autre nombre de carmichael ?
		elif mode == 1:
			prime = generateRandomComposite(maxSize)
			#Si celle là, que faire dans le cas de prime = 4 ?
		elif mode == 2:
			#n impair et supérieur a 2
			prime = random.randrange(3, maxSize, 2)


		a = random.randrange(2, prime)
		mayPrime = test_fermat(prime, a)

		isPrime  = first_test(prime)

		if mayPrime != isPrime:
			#print(f"Error on {prime} with a = {a}")
			error_counter += 1

	error_pourcent = error_counter/n

	print(f"{error_counter} erreurs rencontrées sur {n} valeurs, soit une probabilité d'erreur de {round(error_pourcent*100, 3)}% ({round(error_pourcent, 6)})")

if __name__ == "__main__":
    # experience_euclide(4086, 32, 10)
    c = experience_comptage_premier_naiif()
    # c = experience_carmichael(10000)
    print("cpt = ", c)
    # experience_carmichael()
    #maxn = experience_gen_carmichael_3(1000)
    #print(maxn)