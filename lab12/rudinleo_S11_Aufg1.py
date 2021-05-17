import numpy as np
import matplotlib.pyplot as plt

def rudinleo_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    
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