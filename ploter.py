import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab

def plotting(y1,y2,y3,title):
    fig, ax = plt.subplots()
    ax.plot(y1, label="x=0.1")
    ax.plot(y2, label="x=1")
    ax.plot(y3, label="x=10")
    ax.set_yscale("log")
    ax.set(xlabel='i', ylabel='$x_i$',
           title="(x**2)+1")
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig(title+".png")
    #plt.show()
