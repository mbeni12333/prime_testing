import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
fp = os.path.abspath("rapport/graphs")

class Drawer(object):

    def __init__(self, save_path=fp, title="Temps en fonction de N"):
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
        #plt.xlabel("N")
        plt.xlabel("nombre de bits dans N")
        plt.ylabel("Temps (en secondes)")


        if mode =="linear":
            plt.title(self.title)
        else:
            plt.title(self.title + "-" + mode)

        plt.yscale(mode)

        for key, value in self.times.items():
            plt.plot(value[0], value[1], label=key)

        #plt.plot(value[0], np.sqrt(value[0])/100000, label="sqrt(N)")

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
        plt.savefig(os.path.join(fp, self.title+".png").replace("\\","/"))
        plt.show()

def drawConfusionMatrix(confusion, title="confusion_matrix"):
    """
    Array -> None
    """

    ax= plt.subplot()
    sns.heatmap(confusion, annot=True, ax = ax,fmt=".4f", cmap="viridis", annot_kws={"fontsize":15}, cbar=False);
    ax.set_xlabel('True labels');
    ax.set_ylabel('Predicted labels'); 
    ax.set_title(title); 
    ax.xaxis.set_ticklabels(['prime', 'notprime']);
    ax.yaxis.set_ticklabels(['prime', 'notprime']);
    plt.savefig(os.path.join(fp, title+".png").replace("\\","/"))
    plt.show()

