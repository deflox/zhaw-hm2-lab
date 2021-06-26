import numpy as np

# aufgabe a

def klassisches_runge_kutta_verfahren(f,a,b,n,y0):    
    x,h = np.linspace(a,b,n+1,retstep=True,endpoint=True)
    y = np.zeros(np.shape(x)[0])
    y[0] = y0
    
    for i in range(0,len(x)-1):
        k1=f(x[i],y[i])
        k2=f(x[i]+h/2,y[i]+(h/2)*k1)
        k3=f(x[i]+h/2,y[i]+(h/2)*k2)
        k4=f(x[i]+h,y[i]+h*k3)
        
        y[i+1]=y[i]+(h*(1./6.)*(k1+2*k2+2*k3+k4))
    
    return x,y

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

# differentialgleichung
def f(t,y):
    return 1-(y/t)

def f_exakt(t):
    return (t/2.)+(9/(2*t))

# interval dem gefolgt werden soll und anzahl subintervalle
a = 1
b = 6
h = 0.01
n = int((b-a)/h)

# anfangswert
y0 = 5

t,y = klassisches_runge_kutta_verfahren(f, a, b, n, y0)

import matplotlib.pyplot as plt

t_values = np.arange(a,b,h)
y_values = f_exakt(t_values)

plt.plot(t_values, y_values, label='Exakte Lösung')
plt.plot(t, y, label='Nummerische Lösung')
plot_richtungsfeld(f, a, b, 3, 5, 0.25, 0.25)

# aufgabe b

def neues_runge_kutta_verfahren(f,a,b,n,y0):
    x,h = np.linspace(a,b,n+1,retstep=True,endpoint=True)
    y = np.zeros(np.shape(x)[0])
    y[0] = y0
    
    for i in range(0,len(x)-1):
        k1=f(x[i],y[i])
        k2=f(x[i]+h,y[i]+h*k1*0.75)
        k3=f(x[i]+h/2,y[i]+h*(0.5*k1+0.75*k2))
        k4=f(x[i]+h/4,y[i]+h*(1*k1+0.5*k2+0.75*k3))
        
        y[i+1]=y[i]+(h*(1./10.)*(k1+4*k2+4*k3+k4))
    
    return x,y

# aufgabe c

t_neu,y_neu = neues_runge_kutta_verfahren(f, a, b, n, y0)

plt.plot(t_neu, y_neu, label='Neues Verfahren')
plt.legend()
plt.grid()
plt.show()

abs_fehler = np.abs(y_neu-y)
plt.semilogy(t,abs_fehler,label="Absoluter Fehler")
plt.grid()
plt.legend()
plt.show()