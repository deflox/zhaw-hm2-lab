import numpy as np
import matplotlib.pyplot as plt

# aufgabe a

# datenpunkte die angenähert werden sollen
t = np.array([0,10,20,30,40,50,60,70,80,90,100,110],dtype=float)
y = np.array([76,92,106,123,137,151,179,203,227,250,281,309],dtype=float)

# ansatzfunktionen
def p1(t,lam):
    return lam[0]*t**3+lam[1]*t**2+lam[2]*t+lam[3]
def p2(t,lam):
    return lam[0]*t**2+lam[1]*t+lam[2]

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

# lösung für p2
basicFunctionsCount = 3
A = np.zeros((len(t), basicFunctionsCount))
A[:,0] = t**2
A[:,1] = t
A[:,2] = 1
Q,R = np.linalg.qr(A)
lam_p2 = np.linalg.solve(R,np.matmul(Q.T, y))
print('Resultat lam für p2(t): \n', lam_p2)

plt.plot(t,y,'ro')
plt.plot(t,p1(t,lam_p1),label='p1(t)')
plt.plot(t,p2(t,lam_p2),label='p2(t)')
plt.legend()
plt.grid()
plt.show()

# aufgabe b
e_p1 = np.linalg.norm(np.abs(y-p1(t,lam_p1)),2)**2
e_p2 = np.linalg.norm(np.abs(y-p2(t,lam_p2)),2)**2

print()
print('E(p1()):', e_p1)
print('E(p2()):', e_p2)

'''
Das Fehlerfunktional für p1 ist besser als das von p2.
'''