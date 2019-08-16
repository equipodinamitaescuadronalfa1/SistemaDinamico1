import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
from sympy import *
#from readcol import fgetcols


def plotting(y1,y2,y3):
    fig, ax = plt.subplots()
    ax.plot(y1, label="x=0.1")
    ax.plot(y2, label="x=1")
    ax.plot(y3, label="x=10")
    ax.set_yscale("log")
    ax.set(xlabel='i', ylabel='$x_i$',
           title="(x**2)+1")
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig("test.png")
    plt.show()
    
x=Symbol("x")

with open ('formulae.dat') as f:
    formulae=f.readlines()
formulaestr=formulae[0]


#formulae=fgetcols('formulae.dat')
#strformulae=(formulae[0])[0]
y=sympify(formulaestr)
yprime=y.diff(x)
f=lambdify(x,y,"numpy")





range=range(7)
z=0.1
y1=[]
y2=[]
y3=[]
for i in range:
    z=f(z)
    y1.append(z)
z=1
for i in range:
    z=f(z)
    y2.append(z)
z=3
for i in range:
    z=f(z)
    y3.append(z)
    
plotting(y1,y2,y3)

    
    
    


