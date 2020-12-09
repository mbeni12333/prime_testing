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

