import numpy as np
import matplotlib.pyplot as plt

''' nur punkte '''
x = np.arange(0,10,1)
y = x**2
plt.plot(x,y,'ro')
plt.show()

''' punkte werden zusätzlich verbunden '''
plt.plot(x,y,'ro-')
plt.show()

''' dreidimensionale plots '''
def f(x,y):
    return np.sin(x+1*y)

# erzeugt ein grid mit allen punkte kombiniert aus den beiden argumenten
x,y = np.meshgrid(np.linspace(0,2*np.pi),np.linspace(0,10))
z = f(x,y)

# normaler plot
fig = plt.figure() # erzeuge fig objekt
subplt = fig.add_subplot(111,projection='3d') # erzeuge subplot
subplt.plot_surface(x,y,z) # plotte daten
plt.title('Normaler Plot')
subplt.set_xlabel('x')
subplt.set_ylabel('y')
subplt.set_zlabel('z')
plt.show()

# wireframe plot
fig = plt.figure() # erzeuge fig objekt
subplt = fig.add_subplot(111,projection='3d') # erzeuge subplot
subplt.plot_wireframe(x,y,z) # plotte daten
plt.title('Wireframe Plot')
subplt.set_xlabel('x')
subplt.set_ylabel('y')
subplt.set_zlabel('z')
plt.show()

# colormap plot
import matplotlib.cm as cm
fig = plt.figure() # erzeuge fig objekt
subplt = fig.add_subplot(111,projection='3d') # erzeuge subplot
# erzeuge surface plot mit zusätzlichen argumenten für color
surface_plot = subplt.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# gib diesen surface plot der funktion colorbar auf der fig
fig.colorbar(surface_plot, shrink=0.5, aspect=5)
plt.title('Colormap Plot')
subplt.set_xlabel('x')
subplt.set_ylabel('y')
subplt.set_zlabel('z')
plt.show()

''' plot implicit '''
import sympy as sp
x,y = sp.symbols('x y')
f1 = x**2/186**2 - y**2/(300**2-186**2) - 1
f2 = (y-500)**2/279**2 - (x-300)**2/(500**2-279**2) - 1

# plotting
p1 = sp.plot_implicit(sp.Eq(f1,0),(x,-2000,2000),(y,-2000,2000))
p2 = sp.plot_implicit(sp.Eq(f2,0),(x,-2000,2000),(y,-2000,2000))
p1.append(p2[0])
p1.show()