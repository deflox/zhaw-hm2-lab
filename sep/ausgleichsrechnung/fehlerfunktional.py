import numpy as np
import matplotlib.pyplot as plt

''' fehlerfunktional für lineare ausgleichsprobleme '''

# datenpunkte die angenähert werden sollen
t = np.array([0,10,20,30,40,50,60,70,80,90,100,110],dtype=float)
y = np.array([76,92,106,123,137,151,179,203,227,250,281,309],dtype=float)

# ansatzfunktionen
def p1(t,lam):
    return lam[0]*t**3+lam[1]*t**2+lam[2]*t+lam[3]

# lösung für p1
basicFunctionsCount = 4
A = np.zeros((len(t), basicFunctionsCount))
A[:,0] = t**3
A[:,1] = t**2
A[:,2] = t
A[:,3] = 1
Q,R = np.linalg.qr(A)
lam_p1 = np.linalg.solve(R,np.matmul(Q.T, y))
print('Resultat lam für p1(t): \n', lam_p1)

plt.plot(t,y,'ro')
plt.plot(t,p1(t,lam_p1),label='p1(t)')
plt.legend()
plt.grid()
plt.show()

# fehlerfunktional berechnen mit der funktion
e_p1_1 = np.linalg.norm(np.abs(y-p1(t,lam_p1)),2)**2

# fehlerfunktional berechnen mit der A matrix
e_p1_2 = np.linalg.norm(np.abs(y-np.matmul(A,lam_p1)),2)**2

print('e_p1_1:', e_p1_1)
print('e_p1_2:', e_p1_2)

'''
Das Fehlerfunktional für nichtlineare Ausgleichsprobleme.
'''