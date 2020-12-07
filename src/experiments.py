from src.Drawer import Drawer, drawConfusionMatrix
import numpy as np
import matplotlib.pyplot as plt
import time
from src.fonctions import *
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

"""
Question 1.c
"""
def experience_gcd_inverse(n, step=1, n_exp=10, inverse=True):

    drawer = Drawer(title="Temps en fonction de N")
    
    mean_exec = 0
    for i in range(3, n, step):

        
        mean_exec = 0
        gcd_time = 0
        gcd_etendu_time = 0
        inverse_bezout_time = 0

        for exp in range(n_exp):
            a = random.getrandbits(i+1)
            N = random.getrandbits(i)

            if inverse:
                mean_exec += timeit(my_inverse, a, N)


            gcd_time += timeit(my_gcd, a, N)

            gcd_etendu_time += timeit(my_gcd_etendu, a, N)

            inverse_bezout_time += timeit(my_inverse_bezout, a, N)


        drawer.add(name="my_gcd", time=gcd_time/n_exp, size=i)
        drawer.add(name="my_gcd_etendu", time=gcd_etendu_time/n_exp, size=i)

        if inverse:
            drawer.add(name="my_inverse", time=mean_exec/n_exp, size=i)

        drawer.add(name="my_inverse_bezout", time=inverse_bezout_time/n_exp, size=i)

    drawer.draw()


def experience_exp_mod(n, step=1, n_exp=10):

    drawer = Drawer(title="Temps en fonction de N")
    
    mean_exec = 0
    for i in range(3, n, step):

        
        mean_exec = 0

        for exp in range(n_exp):
            a = random.getrandbits(i+1)
            b = random.getrandbits(i+1)
            N = random.getrandbits(i) + 1

            mean_exec += timeit(my_expo_mod, a, b, N)


        drawer.add(name="my_expo_mod", time=mean_exec, size=i)

    drawer.draw()


def experience_first_test(n, step=1, n_exp=10):

    drawer = Drawer(title="Temps en fonction de N")

    for i in range(3, n, step):

        mean_exec = 0


        for exp in range(n_exp):

            n = random.getrandbits(i)

            mean_exec += timeit(first_test, n)


        drawer.add(name="first_test", time=mean_exec/n_exp, size=i)

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
    
def experience_carmichael_t(tmax=5*60):
    start_time = time.time()
    i = 1

    while time.time() - start_time < tmax:
        # +2 pour éviter de tester les paire
        i += 2
        if isCarmichael(i):
            print(i)


def experience_carmichael3_t(tmax=5*60):
    """
    int -> int
    """
    start_time = time.time()
    best = 0
    N = int(1e4)

    while time.time() - start_time < tmax:

        print("N:", N)

        for i in range(4):

            if time.time() - start_time >= tmax:
                break

            carm = gen_carmichael3(N=N)

            if carm > best:
                best = carm

            print(carm)

        N *= 2

    print("Plus grand nombre de carmicheal trouvé: ", best)


#Inutile ?
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


def generateRandomCompositeImp(maxSize=100000):

    notPrime = random.randrange(4, maxSize)

    while first_test(notPrime) or (notPrime % 2) == 0:
        notPrime = random.randrange(4, maxSize)

    return notPrime


def estimate_proba_test_primality(n, testFunction, maxSize=10000, mode=0):
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
    # error_counter = 0
    titles = ["carmichael", "aleatoire composé", "aleatoire"]
    print("Estimating proba fermat mode = ", titles[mode])

    if mode == 0:
        carmichael_list = gen_carmichael(maxSize)

    confusion = np.zeros((2,2))

    for i in range(n):

        if mode == 0:
            prime = random.choice(carmichael_list)

        elif mode == 1:
            prime = generateRandomCompositeImp(maxSize)
            #Si celle là, que faire dans le cas de prime = 4 ?
        elif mode == 2:
            #n impair et supérieur a 2
            prime = random.randrange(3, maxSize, 2)

        mayPrime = testFunction(prime)
        isPrime  = first_test(prime)

        # if mayPrime != isPrime:
            #print(f"Error on {prime} with a = {a}")
        #    error_counter += 1
        confusion[1-mayPrime, 1-isPrime] += 1

    # error_pourcent = error_counter/n
    # print(f"{error_counter} erreurs rencontrées sur {n} valeurs, soit une probabilité d'erreur de {round(error_pourcent*100, 3)}% ({round(error_pourcent, 6)})")
    confusion = confusion/confusion.sum()
    drawConfusionMatrix(confusion, "confusion_"+testFunction.__name__+"_"+titles[mode])


def estimate_proba_test_rabin(n, maxSize=100000):
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

    modeLabel = ["Carmichael", "Composé", "Aléatoire"]
    
    plt.figure("miller_rabin")
    plt.xlabel("T")
    plt.ylabel("probabilité d'erreur (entre 0 et 1)")
    plt.title("probabilité d'erreur en fonction de T du test de Miller Rabin")

    # if mode == 0:
    carmichael_list = gen_carmichael(maxSize)

    for mode in range(3):
        
        x = []
        y = []
        
        for T in range(1, 10):

            error_counter = 0

            for i in range(n):

                if mode == 0:
                    prime = random.choice(carmichael_list)

                elif mode == 1:
                    prime = generateRandomCompositeImp(maxSize)
                    #Si celle là, que faire dans le cas de prime = 4 ?
                elif mode == 2:
                    #n impair et supérieur a 2
                    prime = random.randrange(3, maxSize, 2)


                mayPrime = test_miller_rabin(prime, T)

                isPrime  = first_test(prime)

                if mayPrime != isPrime:
                    #print(f"Error on {prime} with a = {a}")
                    error_counter += 1

            error_pourcent = error_counter/n

            x.append(T)
            y.append(error_pourcent)

        plt.plot(x, y, label=modeLabel[mode])

    plt.legend(loc='best')
    plt.show()

    #print(f"{error_counter} erreurs rencontrées sur {n} valeurs, soit une probabilité d'erreur de {round(error_pourcent*100, 3)}% ({round(error_pourcent, 6)})")

# def experience_miller_rabin(N=1e5):

#     annotations = np.array([1 if first_test(i) else 0 for i in range(5, int(N), 2)])
#     predictions = np.array([1 if test_miller_rabin(i) else 0 for i in range(5, int(N), 2)])

#     confusion = np.zeros((2,2))

#     for i in range(len(annotations)):
#         confusion[1-predictions[i], 1-annotations[i]] += 1

#     drawConfusionMatrix(confusion)

if __name__ == "__main__":
    # experience_euclide(4086, 32, 10)
    # c = experience_comptage_premier_naiif()
    # c = experience_carmichael(10000)
    # print("cpt = ", c)
    # experience_carmichael()
    #maxn = experience_gen_carmichael_3(1000)
    #print(maxn)
    # print(test_miller_rabin(7))
    # experience_miller_rabin()
    # print(gen_carmichael32(1.2e4))
    # print(gen_rsa(64))
    public_key,  private_key = RSA(1024)
    # print(f"public_key:{tuple(map(hex, public_key))}")
    # print(f"private_key:{tuple(map(hex, private_key))}")
    m = "Bonjour"
    t = time.time()
    s = encode(m, public_key)
    d = decode(s, private_key)
    print(f"message envoyé: {m}, message décodé: {d}, temps encodage_decodage : {time.time() - t}")
    # print(my_expo_mod(26, -23, 77))