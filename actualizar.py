import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
from sympy import *
import sys 
#from readcol import fgetcols


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
    plt.show()
    
x=Symbol("x")


n=len(sys.argv)
file_flag=False
ecuation_flag=False

for i in range(n):
    if '-f' in sys.argv[i]:
        file_flag=True
        filename=sys.argv[i+1]
        
    if '-e' in sys.argv[i]:
        ecuation_flag=True
        formulaestr= sys.argv[i+1]
    
if file_flag:
    with open (filename) as f:
        formulae=f.readlines()
        formulaestr=formulae[0]
        print("using file mode")
elif ecuation_flag:
    print("using ecuation mode")



'''
with open ('formulae.dat') as f:
    formulae=f.readlines()
formulaestr=formulae[0]
'''

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
    
plotting(y1,y2,y3,formulaestr)

    
    
