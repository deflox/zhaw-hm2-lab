import numpy as np
import matplotlib.pyplot as plt

c = 1

def w(x,t):
    return np.sin(x+c*t)

def v(x,t):
    return np.sin(x+c*t)+np.cos(2*x+2*c*t)

x,t = np.meshgrid(np.linspace(0,2*np.pi),np.linspace(0,10))
z1 = w(x,t)
z2 = v(x,t)

fig = plt.figure()
subplt = fig.add_subplot(111,projection='3d')
subplt.plot_surface(x,t,z1)
plt.show()

fig = plt.figure()
subplt = fig.add_subplot(111,projection='3d')
subplt.plot_surface(x,t,z2)
plt.show()