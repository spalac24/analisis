import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

print "please enter the function, remember to use ** for exponentiation, and for mathematical functions, prefixthem with np (e.g. np.cos(x) instead of cos(x)"
fun = raw_input()
print "please enter lower and upper bound for graphics"
lo = float(input())
hi = float(input())
x = np.linspace(lo,hi,500)
y = eval(fun)

plt.plot(x,y,'k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('hola')
plt.show()

