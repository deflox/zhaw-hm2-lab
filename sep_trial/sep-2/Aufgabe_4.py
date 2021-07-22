import numpy as np
import matplotlib.pyplot as plt

# aufgabe a

# datenpunkte die angenähert werden sollen
t = np.array([0,1,2,3,4,5],dtype=float)
y = np.array([0.54,0.44,0.28,0.18,0.12,0.08],dtype=float)

# ansatzfunktionen
def p(x,lam):
    return lam[0]*x**4+lam[1]*x**3+lam[2]*x**2+lam[3]*x+lam[4]

# lösung für p1
basicFunctionsCount = 5
A = np.zeros((len(t), basicFunctionsCount))
A[:,0] = t**4
A[:,1] = t**3
A[:,2] = t**2
A[:,3] = t
A[:,4] = 1
Q,R = np.linalg.qr(A)
lam_p = np.linalg.solve(R,np.matmul(Q.T, y))
print('Resultat lam für p(t): \n', lam_p)

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