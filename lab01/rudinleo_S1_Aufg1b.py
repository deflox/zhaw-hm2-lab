import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# aufgabe 1b

def create_plots(x,y,z,x_label,y_label,z_label,f_name):
    # höhenlinien
    plt.contour(x, y, z)
    plt.title('Höhenlinien {}'.format(f_name))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    
    # plot mit plot_surface() mit colormap
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(111, projection='3d')
    surface_plot = ax2.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig1.colorbar(surface_plot, shrink=0.5, aspect=5)
    plt.title('Fläche mit Colormap {}'.format(f_name))
    ax2.set_xlabel(x_label)
    ax2.set_ylabel(y_label)
    ax2.set_zlabel(z_label)
    plt.show()
    
    # plot mit plot_wireframe()
    fig2 = plt.figure()
    ax3 = fig2.add_subplot(111, projection='3d')
    ax3.plot_wireframe(x,y,z)
    plt.title('Gitterplot {}'.format(f_name))
    ax3.set_xlabel(x_label)
    ax3.set_ylabel(y_label)
    ax3.set_zlabel(z_label)
    plt.show()
    
R = 8.31

def p(V,T):
    return (R*T)/V

V,T = np.meshgrid(np.linspace(0.004,0.2),np.linspace(0,1e4))
z = p(V,T)
create_plots(V,T,z,'V','T','z','p(V,T)')

def V(p,T):
    return (R*T)/p

p,T = np.meshgrid(np.linspace(1e4,1e5),np.linspace(0,1e4))
z = V(p,T)
create_plots(p,T,z,'p','T','z','V(p,T)')

def T(p,V):
    return (p*V)/R

p,V = np.meshgrid(np.linspace(1e4,1e6),np.linspace(0,10))
z = T(p,V)
create_plots(p,V,z,'p','V','z','T(p,V)')