import numpy as np
from rudinleo_S5_Aufg2 import rudinleo_S5_Aufg2

# aufgabe a

x = np.array([1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],dtype=np.float)
y = np.array([75.995,91.972,105.711,123.203,131.669,150.697,179.323,203.212,226.505,249.633,281.422,308.745],dtype=np.float)
xx = np.array([1945,1965,2005])

yy = rudinleo_S5_Aufg2(x, y, xx)

# aufgabe b

from scipy import interpolate
import matplotlib.pyplot as plt

S = interpolate.CubicSpline(x, y)

x_values = np.arange(1900,2010,1)
plt.plot(x_values,S(x_values),label='Interpolation with CubicSpine()')
plt.show()

# aufgabe c

x = np.array([0,10,20,30,40,50,60,70,80,90,100,110],dtype=np.float)

P = np.polyfit(x,y,11)

x_values = np.arange(0,110,1)
plt.plot(x_values, np.polyval(P, x_values))
plt.show()

'''
Da das Problem schlecht konditioniert ist, wirken sich grosse x-Werte
negativ auf die Fehlerentwicklung aus, was das Resultat ungenauer werden
lässt.
'''