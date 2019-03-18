import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-10,10,0.05)
y = 1/(1+math.e**(-x))
plt.xlim(-10,10)
plt.plot(x,y,label='picture')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()