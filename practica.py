import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature as quad
from math import fmod

def fun (x): #test function
    x = fmod(x+np.pi,2*np.pi)
    x -= np.pi
    if (-np.pi < x <= 0):
        return -1
    return 1
        
f = lambda x: fun(x)

print "please enter the function, for special numbers and functions prefix them with np, e.g. np.pi, np.cos(..),"
#f_string = raw_input()
#f = lambda x: eval(f_string)

print "please enter the iterations quantity"
n = input()

def ath_aux (n):
    return lambda x : map(lambda y: f(y)*np.cos(n*y), x)

def bth_aux (n):
    return lambda x : map(lambda y: f(y)*np.sin(n*y), x)

def ath (n):
    (y,_) = quad(ath_aux(n),-np.pi,np.pi)
    if (n == 0):
        return y/(2*np.pi)
    return y/(np.pi)

def bth (n):
    (y,_) = quad(bth_aux(n),-np.pi,np.pi)
    return y/np.pi

a = [ath(i) for i in range(n)]
b = [0.0]+[bth(i) for i in range(1,n)]

def fou (x):
    res = 0
    for i in range(0,len(a)-1):
        res += a[i]*np.cos(i*x)
    for i in range(0,len(b)-1):
        res += b[i]*np.sin(i*x)
    return res


x = np.linspace(-2*np.pi, 2*np.pi,500)
y = map(fou,x)

#print a
#print b

plt.plot(x,y,'r')
plt.show()

