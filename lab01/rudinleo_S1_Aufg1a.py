import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# aufgabe 1a

def W(v0,a):
    return (v0**2*np.sin(2*a))/g

g = 9.81
v0,a = np.meshgrid(np.arange(0,100), np.arange(0,1.55,0.01))
z = W(v0,a)

# höhenlinien
plt.contour(v0, a, z)
plt.title('Höhenlinien')
plt.xlabel('v0')
plt.ylabel('a')
plt.show()

# plot mit plot_surface() mit colormap
fig1 = plt.figure(1)
ax2 = fig1.add_subplot(111, projection='3d')
surface_plot = ax2.plot_surface(v0,a,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig1.colorbar(surface_plot, shrink=0.5, aspect=5)
plt.title('Fläche mit Colormap')
ax2.set_xlabel('v0')
ax2.set_ylabel('a')
ax2.set_zlabel('Wurfweite')
plt.show()

# plot mit plot_wireframe()
fig2 = plt.figure(2)
ax3 = fig2.add_subplot(111, projection='3d')
ax3.plot_wireframe(v0,a,z)
plt.title('Gitterplot')
ax3.set_xlabel('v0')
ax3.set_ylabel('a')
ax3.set_zlabel('Wurfweite')
plt.show()