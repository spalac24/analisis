import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math

def f(x):
    if ((math.floor(2*x)%2) == 0):
        return -1
    return 1


lo = -1.0
hi = 2.0
x = np.linspace(lo,hi,500)
y = map(f,x)
plt.plot(x,y,'k')
plt.ylim([-2,2])
plt.show()
