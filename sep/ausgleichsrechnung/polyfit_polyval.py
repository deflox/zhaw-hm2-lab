import numpy as np
import matplotlib.pyplot as plt

x = np.array([1981,1984,1989,1993,1997,2000,2001,2003,2004,2010])
y = np.array([0.5,8.2,15.,22.9,36.6,51.,56.3,61.8,65.,76.7])

# polyfit erzeugt ein polynom vom grad n für die gegebenen punkte
# in diesem fall wird ein polynom vom grad np.shape(x)-1 also 9 erzeugt
polynom_coefficients = np.polyfit(x,y,np.shape(x)-1)

# np polyval wertet ein polynom an der gegebenen stelle aus indem die funktion
# diese auf die liste der koeffizienten anwenden
# z.B. np.polyval([3,0,1], 5) -> 3 * 5**2 + 0 * 5**1 + 1
# daher wird nun hier eine funktion definiert, die für ein gegebenes x
# den funktionswert für das polynom das von polyfit gerechnet wurde, ausgibt
def f(x):
    return np.polyval(polynom_coefficients, x)

# erzeuge plot des interolierten polynoms
x_values = np.arange(1975,2020,0.1)
plt.plot(x_values,f(x_values),label='polyfit')
plt.ylim(-100,250)
plt.grid()