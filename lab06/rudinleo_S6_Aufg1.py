import numpy as np
import matplotlib.pyplot as plt

# aufgabe 1a

T_i = np.array([0,10,20,30,40,50,60,70,80,90,100],dtype=np.float)
Phi_i = np.array([999.9,999.7,998.7,995.7,992.2,988.1,983.2,977.8,971.8,965.3,958.4],dtype=np.float)

def F(T,lamda):
    return lamda[0]*T**2+lamda[1]*T+lamda[2]

A = np.zeros((len(T_i),3))
A[:,0] = T_i**2
A[:,1] = T_i
A[:,2] = 1

# LR-Verfahren:
lamda1 = np.linalg.solve(np.matmul(A.T,A), np.matmul(A.T,np.atleast_2d(Phi_i).T))
print('Resultat für lamda mit LR-Verfahren: \n', lamda1)

# QR-Verfahren:
Q,R = np.linalg.qr(A)
lamda2 = np.linalg.solve(R,np.matmul(Q.T, Phi_i))
print('Resultat für lamda mit QR-Verfahren: \n', lamda2)

plt.plot(T_i,Phi_i,'ro')
plt.plot(T_i,F(T_i,lamda1),label='LR-Verfahren')
plt.plot(T_i,F(T_i,lamda2),label='QR-Verfahren')

# aufgabe 1b

print()
print('Konditionszahl A^T:', np.linalg.cond(A.T))
print('Konditionszahl A:', np.linalg.cond(A))
print('Konditionszahl R:', np.linalg.cond(R))

'''
Konditionszahlen sind alle drei gleich.
'''

# aufgabe 1c

polyfit = np.polyfit(T_i, Phi_i, 2)
plt.plot(T_i, np.polyval(polyfit, T_i), label='polyfit')
plt.legend()
plt.show()

# aufgabe 1d

print()
print('Fehlerfunktional für LR:', np.linalg.norm((Phi_i - np.matmul(A,lamda1)),2)**2)
print('Fehlerfunktional für QR:', np.linalg.norm((Phi_i - np.matmul(A,lamda2)),2)**2)
print('Fehlerfunktional für Polyfit:', np.linalg.norm((Phi_i - np.matmul(A,polyfit)),2)**2)

'''
Fehlerfunktional ist grösser für die LR-Zerlegung.
'''