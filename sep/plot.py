import numpy as np
import matplotlib.pyplot as plt

# nur punkte
x = np.arange(0,10,1)
y = x**2
plt.plot(x,y,'ro')
plt.show()

# punkte mit linien
plt.plot(x,y,'ro-')
plt.show()