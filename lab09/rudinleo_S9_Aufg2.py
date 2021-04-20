import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x**2)

x_values = np.arange(0,np.pi,0.001)
plt.plot(x_values, f(x_values))