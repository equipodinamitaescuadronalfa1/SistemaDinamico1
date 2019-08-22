import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab

def plotting(y1,y2,y3,title,v1,v2,v3):
    fig, ax = plt.subplots()
    s1 = 'x=%s'%(v1)
    s2 = 'x=%s'%(v2)
    s3 = 'x=%s'%(v3)
    ax.plot(y1, label=s1)
    ax.plot(y2, label=s2)
    ax.plot(y3, label=s3)
    ax.set_yscale("log")
    ax.set(xlabel='i', ylabel='$x_i$',
           title="(x**2)+1")
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig(title+".png")
    #plt.show()
