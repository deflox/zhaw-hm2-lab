import numpy as np
import matplotlib.pyplot as plt

# aufgabe a

di = np.array([500,1000,1500,2500,3500,4000,4500,5000,5250,5500],dtype=float)
Pi = np.array([10.5,49.2,72.1,85.4,113,121,112,80.2,61.1,13.8],dtype=float)

plt.plot(di,Pi,'ro',label="Datenpunkte")

#def p(x):
#    return x**2+x+1
#test_values = np.arange(-10,10)
#plt.plot(test_values,p(test_values))

# Man wählt Polynom 4ten Grades

# aufgabe b

# neue skalierung der drehzahlen
#di = np.array([5,10,15,25,35,40,45,50,52.5,55],dtype=float)
di = di/1000

# ansatzfunktion
def F(x,lam):
    return lam[0]*x**4+lam[1]*x**3+lam[2]*x**2+lam[3]*x+lam[4]

basicFunctionsCount = 5
A = np.zeros((len(di), basicFunctionsCount))
A[:,0] = di**4
A[:,1] = di**3
A[:,2] = di**2
A[:,3] = di**1
A[:,4] = 1

Q,R = np.linalg.qr(A)
lambdaa = np.linalg.solve(R,np.matmul(Q.T, Pi))
print('Resultat für lamda mit QR-Verfahren: \n', lambdaa)

di_values = np.arange(500,5500,1)
Pi_values = F(di_values/1000,lambdaa) # di_values muss hier auch skaliert werden

plt.plot(di_values,Pi_values,label='Approximierte Funktion')
plt.grid()
plt.legend()
plt.show()