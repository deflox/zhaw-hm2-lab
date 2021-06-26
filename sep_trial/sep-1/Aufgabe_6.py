import numpy as np
import matplotlib.pyplot as plt

# aufgabe a

# N(0) = G/(2*(G-N_0))/N_0
# lim_t->inf N(t) = 0

# aufgabe b

ti = np.array([0,14,28,42,56],dtype=float)
Ni = np.array([29,2072,15798,25854,28997],dtype=float)

plt.plot(ti,Ni,'ro',label="Datenpunkte")
plt.legend()
plt.grid()
plt.show()

'''
G muss sehr gross sein, da t im Exponent steht und daher den Bruch stark
verkleinert umso grösser t ist

N sollte auch relativ gross sein um als Faktor dem Exponent t entgegenzuwirken
aber auch nicht zu gross, sonst wird das Resultat das Bruches negativ also
auf jeden Fall kleiner als G

'''

# aufgabe c

