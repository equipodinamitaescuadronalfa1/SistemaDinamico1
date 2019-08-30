'''import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
from sympy import *
import sys
import ploter
#from readcol import fgetcols


#####
def plotting(y1,title):
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
###

def dynamic_system(formulae_str, a0, b0, n0, x0, N):
    x,a,b,n = Symbol("x a b n")

    y = sympify(formulae_str)
    y.subs(a,a0)
    y.subs(b,b0)
    y,subs(n,n0)
    y.subs(x,x0)

    print(y)

    #yprime = y.diff(x)
    f=lambdify(x,y,"numpy")

    # Data for plotting
    iterations = range(N)
    z = x0
    y1 = []
    for i in iterations:
        z = f(z)
        y1.append(z)

    return y1


n=len(sys.argv)

ecuation_flag=False


for i in range(n):
    if '-a' in sys.argv[i]:
        i+=1
        a0=float(sys.argv[i+1])
        i+=1
        a1=float(sys.argv[i+1])
        i+1=1
        d1=float(sys.argv[i+1])
        
    if '-b' in sys.argv[i]:
        i+=1
        b0=float(sys.argv[i])
        i+=1
        b1=float(sys.argv[i])
        i+=1
        bd=float(sys.argv[i])
        
        
        
        
        
    if '-x0' in sys.argv[i]:
        x0=float(sys.argv[i])
        i+=1
        x1=float(sys.argv[i])
        i+=1
        xd=float(sys.argv[i])
        
        
        
    if '-n' in sysargv[i]:
        n0=float(sys.argv[i])
        i+=1
        n1=float(sys.argv[i])
        i+=1
        nd=float(sys.argv[i])
        
        
    if '-i' in sys.argv[i]:
        iteracion=int(sys.argv[i+1])
    if '-f' in sys.argv[i]:
        file_flag=True
        filename=sys.argv[i+1]
    if '-e' in sys.argv[i]:
        equation_flag=True
        formulae_str=sys.argv[i+1]
        
        
        


###
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


with open ('formulae.dat') as f:
    formulae=f.readlines()
formulaestr=formulae[0]
###

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
    
    y1.append(z)
z = float(v[1])
for i in range:
    z=f(z)
    y2.append(z)
z = float(v[2])
for i in range:
    z=f(z)
    y3.append(z)
    
ploter.plotting(y1,y2,y3,formulaestr,float(v[0]),float(v[1]),float(v[2]))
z = float(v[0])
for i in range:
    z=f(z)
'''




#!/usr/bin/env python3

#from graphics import plotting
from sympy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys

#./dynamic -f formulae.dat
# USAGE
#./dynamic.py -e a*x^n+b -a 1 10 1  -b 1 5 1 -n 2 3 1 -x0 0.1 1.0 0.1 -i 6
#from readcol import fgetcols

def plotting(fig,ax,time,y1,title,filename,caption):
    ax.plot(time,y1,label=caption)
    
    
    #ax.set_yscale('log')
    ax.set(xlabel='Hours', ylabel='g',
           title=title)
    ax.grid()
    
    
    
    #plt.show()

def dynamic_system(formulae_str,a0,b0,n0,x0,N):
    x,a,b,n = symbols("x a b n")
    print(a0,b0,n0,x0,N)
    y = sympify(formulae_str)
    y = y.subs(a,a0)
    y = y.subs(b,b0)
    y = y.subs(n,n0)

    print(y)
    
    #yprime = y.diff(x)
    f=lambdify(x,y,"numpy")

    # Data for plotting
    iterations = range(N)
    z = x0
    y1 = []
    time=[]
    mitosis = 3.0 #Hours
    dtime = 0.0
    
    weight=1e-12#g
    
    for i in iterations:
        time.append(dtime)
        dtime+=mitosis
        z = f(z)
        y1.append(z*weight)
        
    return y1,time
    
    
#formulae='x^2+1.0'
#def f(x):
#    return x*x+1.0

#formulae= fgetcols('formulae.dat')
#print(formulae)
#formulae_str= (formulae[0])[0]
#print(formulae_str)

file_flag = False
equation_flag = False
formulae_str = 'x'
x0=a0=b0=n0=1.0
x1=a1=b1=n1=1.0
dx=da=db=dn=1.0
itera=5
n = len(sys.argv)




for i in range(n):
    if  '-a' in sys.argv[i]:
        #file_flag=True
        i+=1
        a0=float(sys.argv[i])
        i+=1
        a1=float(sys.argv[i])
        i+=1
        da=float(sys.argv[i])

    if  '-b' in sys.argv[i]:
        #file_flag=True
        #b0=float(sys.argv[i+1])
        i+=1
        b0=float(sys.argv[i])
        i+=1
        b1=float(sys.argv[i])
        i+=1
        db=float(sys.argv[i])
        
    if  '-n' in sys.argv[i]:
        #file_flag=True
        #n0=float(sys.argv[i+1])
        i+=1
        n0=float(sys.argv[i])
        i+=1
        n1=float(sys.argv[i])
        i+=1
        dn=float(sys.argv[i])

        
    if  '-x0' in sys.argv[i]:
        #file_flag=True
        #x0=float(sys.argv[i+1])
        i+=1
        x0=float(sys.argv[i])
        i+=1
        x1=float(sys.argv[i])
        i+=1
        dx=float(sys.argv[i])

        
    if  '-i' in sys.argv[i]:
        #file_flag=True
        itera=int(sys.argv[i+1])
        
    if  '-f' in sys.argv[i]:
        file_flag=True
        filename=sys.argv[i+1]

    if  '-e' in sys.argv[i]:
        equation_flag=True
        formulae_str=sys.argv[i+1]
       
        
if file_flag:
    with open(filename) as f:
        formulae=f.readlines()
        formulae_str=formulae[0]
        print('Using archive mode  with '+formulae_str)

if equation_flag:
    print('Using equation mode with '+formulae_str)


A = np.arange(a0,a1,da)
B = np.arange(b0,b1,db)
N = np.arange(n0,n1,dn)
X0= np.arange(x0,x1,dx)
print(A)
print(B)
print(N)
print(X0)

fig, ax = plt.subplots()

for a in A:
    for b in B:
        for n in N:
            for x0 in X0:
                y1,time = dynamic_system(formulae_str,a,b,n,x0,itera)
                filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(itera)+"_x0"+str(x0)+"_i"+str(n)+".png"
                caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x0)+" i="+str(itera)
                plotting(fig,ax,time,y1,formulae_str,filename,caption)
plt.show()
fig.savefig(filename)

#pylab.legend(loc='upper left')
#plt.show()
#fig.savefig(filename)
    
