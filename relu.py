import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

#  x = np.array([-5.0, 5.0, 0.1])
#  print(y)

x = np.arange(-6.0, 6.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1, 6)
plt.show()



