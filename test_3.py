import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def f(x):
    return np.cos(x)

def g(y):
    return np.sin(y)


t = np.linspace(0,np.pi*2.0,500)
x = f(t)
y = g(t)

plt.plot(x,y,'k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('hola')
plt.show()

