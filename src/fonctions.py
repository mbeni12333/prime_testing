import numpy as np
import matplotlib.pyplot as plt
import time

class Drawer(object):

    def __init__(self, title="Temps en fonction du nombre d'objets"):
        self.nameToTimeA = {}
        self.sizes = []
        self.title = title
        self.times = {}

    def add(self, name, time, size):
        if name not in self.times.keys:
            self.times[name] = [[size], [time]]
        else:
            self.times[name][0].append(size)
            self.times[name][1].append(time)

        #if name in self.nameToTimeA:
        #    self.nameToTimeA[name].append(time)
        #else:
        #    self.nameToTimeA[name] = [time]

        # on prefere tout le temps avoir [ [] ], que d'avoir tantot [] et tantot [[]]
        # if len(self.sizes) == 0 or self.sizes[-1] != size:
        #    self.sizes.append(size)

    def draw(self, mode="normal"):
        plt.figure("Temps")
        plt.xlabel("n")
        plt.ylabel("Temps (en secondes)")

        plt.title(self.title + "-" + mode)
        plt.yscale(mode)

        for key, value in self.times.items():
            plt.plot(value[0], value[1], label=key)

        # if mode == "normal":
        #    plt.title("Temps en fonction de n")

        # elif mode == "log":
        #    plt.title("log(Temps) en fonction du nombre d'objets")

        # elif mode == "2^n":
        #    plt.title("Temps/2^n en fonction du nombre d'objets")

        # for name, timeArray in self.nameToTimeA.items():

        #    if mode == "normal":
        #        plt.plot(self.sizes, timeArray, label=name)

        #    elif mode == "log":
        #        plt.plot(self.sizes, np.log(timeArray), label=name)

        #    elif mode == "2^n":
        #        plt.plot(self.sizes, timeArray/np.power(2, self.sizes), label=name)


        plt.legend(loc='best')
        plt.show()


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
            mean_exec += timeit(my_gcd, a, b)/n_exp
        Drawer.add("my_gcd", mean_exec)

    Drawer.draw()
