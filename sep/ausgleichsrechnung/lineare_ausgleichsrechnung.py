import numpy as np
import matplotlib.pyplot as plt

# datenpunkte die angenähert werden sollen
x = np.array([0,10,20,30,40,50,60,70,80,90,100],dtype=float)
y = np.array([999.9,999.7,998.7,995.7,992.2,988.1,983.2,977.8,971.8,965.3,958.4],dtype=float)

# ansatzfunktion
# basisfunktionen hier:
# f_1(x) = x**2
# f_2(x) = x
# f_3(x) = 1
def F(x,lamda):
    return lamda[0]*x**2+lamda[1]*x+lamda[2]

# erstellen der A matrix für alle x punkte
# f_1(x1) f_2(x1) f_3(x1)
# f_1(x2) f_2(x2) f_3(x2)
# ...
basicFunctionsCount = 3
A = np.zeros((len(x), basicFunctionsCount))
A[:,0] = x**2
A[:,1] = x
A[:,2] = 1

# LR-Verfahren:
lambda1 = np.linalg.solve(np.matmul(A.T,A), np.matmul(A.T,np.atleast_2d(y).T))
print('Resultat für lamda mit LR-Verfahren: \n', lambda1)
print()

# QR-Verfahren:
Q,R = np.linalg.qr(A)
lambda2 = np.linalg.solve(R,np.matmul(Q.T, y))
print('Resultat für lamda mit QR-Verfahren: \n', lambda2)

plt.plot(x,y,'ro')
plt.plot(x,F(x,lambda1),label='LR-Verfahren')
plt.plot(x,F(x,lambda2),label='QR-Verfahren')