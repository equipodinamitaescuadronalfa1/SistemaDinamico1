import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab

def f(x):
    return (x**2)+1

def main():
    conditions=[0.1,1,3]
    
    
    vector=[]
    for w in range(len(conditions)):
        #print(len(conditions))
        vec=[]
        auxiar=conditions[w]
        for d in range(10):
            vec.append(auxiar)
            auxiar=f(auxiar)
        vector.append(vec)
        
    fig, ax = plt.subplots()
    ax.plot(vector[0], label="x=0.1")
    ax.plot(vector[1], label="x=1")
    ax.plot(vector[2], label="x=10")
    ax.set_yscale("log")
    ax.set(xlabel='i', ylabel='$x_i$',
           title="(x**2)+1")
    ax.grid()
    pylab.legend(loc='upper left')
    fig.savefig("test.png")
    plt.show()
    
    
main()
    
            
    
    
    
