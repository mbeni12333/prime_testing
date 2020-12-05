import numpy as np
import matplotlib.pyplot as plt

class Drawer(object):

    def __init__(self, save_path="../rapport/graphs", title="Temps en fonction du nombre d'objets"):
        self.title = title
        self.times = {}
        self.save_path = save_path

    def add(self, name, time, size):
        if name not in self.times.keys():
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

    def draw(self, mode="linear"):
        plt.figure("Temps")
        plt.xlabel("nombre de bits dans N")
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
        plt.savefig( self.title + ".jpg")
        plt.show()
