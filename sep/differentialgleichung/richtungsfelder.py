import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def plot_richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):
    
    # take x,ymax + hx,y so that the endpoint is included
    x_arange = np.arange(xmin, xmax + hx, hx)
    y_arange = np.arange(ymin, ymax + hy, hy)

    # erzeugt eine gatterlinie welche alle x und y punkte enthält
    X,Y = np.meshgrid(x_arange,y_arange)
    
    # steigungen bei allen punkten eingesetzt in die differntialgleichung
    slopes = f(X,Y)
    
    # damit plt.quiver funktioniert, braucht die funktion für jeden punkt
    # den jeweiligen x und y wert des vektors. für den x wert nehmen wir
    # hier 1 der y wert ergibt sich dann aus der steigungsfunktion, also
    # aus allen errechnet steigungen in slopes. da wir für x 1 nehmen, können
    # wir einfach den ganzen slopes array nehmen für die y werte
    x = np.ones(np.shape(slopes))
    
    plt.quiver(X,Y,x,slopes)
    plt.show()

def plotField(f, a, b, n, y0, plt, yEndOffset= 5, arrowsX= 10, arrowsY= 10, num_lines=0):

    # PLOT SETTINGS
    xmin = float(a)
    xmax = float(b)
    ymin = min(float(y0), float(y0) + yEndOffset)
    ymax = max(float(y0), float(y0) + yEndOffset)
    hx = (xmax-xmin)/n
    hy = (ymax-ymin)/n

    # Vector field
    x_range = np.linspace(xmin, xmax, int(arrowsX))
    y_range = np.linspace(ymin, ymax, int(arrowsY))
    X, Y = np.meshgrid(x_range, y_range)
    V = f(X,Y)
    U = np.ones(np.shape(V))

    # Normalize arrows
    N = np.sqrt(U ** 2 + V ** 2)
    U = U / N
    V = V / N

    plt.title("DLG Field")
    #plt.xlim([xmin-hx, xmax+hx])
    #plt.ylim([ymin-hy, ymax+hy])
    plt.xlim([xmin-(hx/2.), xmax+(hx/2.)])
    plt.ylim([ymin-(hy/2.), ymax+(hy/2.)])
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid()

    # Plot field
    plt.quiver(X, Y, U, V, angles="xy")

    # Plot lines
    if (num_lines):
        # Plot function lines
        def f_special(x, y):
            dx = np.ones(2)
            dx[1] = f(x[0],x[1])
            return dx

        x = np.linspace(xmin, xmax, 1000)

        for x0 in np.linspace(xmin, xmax, num_lines):
            y_initial = [x0, y0]
            y = odeint(f_special, y_initial , x)
            plt.plot(y[:, 0], y[:, 1], "-", label="("+str(x0)+","+str(y0)+") exakt")

    #Return plt
    return plt
    
# differentialgleichungsfunktion
def f(x,y):
    return x**2 + 0.1*y

# parameter
xmin = -2
xmax = 2
ymin = -0.5
ymax = 3.5

# abstand
hx = 0.25
hy = 0.25

plot_richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy)
#plotField(f, xmin, xmax, 32, 3, plt)