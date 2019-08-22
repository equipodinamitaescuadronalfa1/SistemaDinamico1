import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
from sympy import *
import sys
import ploter
#from readcol import fgetcols


'''def plotting(y1,y2,y3,title):
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
    plt.show()'''


n=len(sys.argv)

ecuation_flag=False

if n > 1:
    if sys.argv[1] == '-f':
        if n>2:
            
            filename=sys.argv[2]
            
            with open (filename) as f:
                formulae=f.readlines()
                formulaestr=formulae[0]
            print("using file mode")
        else:
            print("No filename given check main.py -help for more information")
            exit()
           
    elif sys.argv[1] == '-e':
        if n>2:
            ecuation_flag=True
            print("using ecuation mode")
            formulaestr= sys.argv[2]
        else:
            print("No ecuation given check main.py -help for more information")
            exit()
   
    elif sys.argv[1] == '-help':
        print("") #insertar aqui*******************************************************************************************************
        exit()
    else:
        print("No method found check main.py -help for more information")
        exit()
    
    
else:
    print("No parameters given check main.py -help for more information")
    exit()

'''
with open ('formulae.dat') as f:
    formulae=f.readlines()
formulaestr=formulae[0]
'''

#formulae=fgetcols('formulae.dat')
#strformulae=(formulae[0])[0]
x=Symbol("x")
y=sympify(formulaestr)
#yprime=y.diff(x)
f=lambdify(x,y,"numpy")


range=range(7)
y1=[]
y2=[]
y3=[]
try:
    with open('values.txt') as g:
        v = g.readlines()
        v = str(v[0]).split()
except:
    print("No values found")
    exit()
    
z = float(v[0])
for i in range:
    z=f(z)
    y1.append(z)
z = float(v[1])
for i in range:
    z=f(z)
    y2.append(z)
z = float(v[2])
for i in range:
    z=f(z)
    y3.append(z)
    
ploter.plotting(y1,y2,y3,formulaestr)
