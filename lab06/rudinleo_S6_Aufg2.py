import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [33.00, 53.00, 3.32, 3.42, 29.00],
    [31.00, 36.00, 3.10, 3.26, 24.00],
    [33.00, 51.00, 3.18, 3.18, 26.00],
    [37.00, 51.00, 3.39, 3.08, 22.00],
    [36.00, 54.00, 3.20, 3.41, 27.00],
    [35.00, 35.00, 3.03, 3.03, 21.00],
    [59.00, 56.00, 4.78, 4.57, 33.00],
    [60.00, 60.00, 4.72, 4.72, 34.00],
    [59.00, 60.00, 4.60, 4.41, 32.00],
    [60.00, 60.00, 4.53, 4.53, 34.00],
    [34.00, 35.00, 2.90, 2.95, 20.00],
    [60.00, 59.00, 4.40, 4.36, 36.00],
    [60.00, 62.00, 4.31, 4.42, 34.00],
    [60.00, 36.00, 4.27, 3.94, 23.00],
    [62.00, 38.00, 4.41, 3.49, 24.00],
    [62.00, 61.00, 4.39, 4.39, 32.00],
    [90.00, 64.00, 7.32, 6.70, 40.00],
    [90.00, 60.00, 7.32, 7.20, 46.00],
    [92.00, 92.00, 7.45, 7.45, 55.00],
    [91.00, 92.00, 7.27, 7.26, 52.00],
    [61.00, 62.00, 3.91, 4.08, 29.00],
    [59.00, 42.00, 3.75, 3.45, 22.00],
    [88.00, 65.00, 6.48, 5.80, 31.00],
    [91.00, 89.00, 6.70, 6.60, 45.00],
    [63.00, 62.00, 4.30, 4.30, 37.00],
    [60.00, 61.00, 4.02, 4.10, 37.00],
    [60.00, 62.00, 4.02, 3.89, 33.00],
    [59.00, 62.00, 3.98, 4.02, 27.00],
    [59.00, 62.00, 4.39, 4.53, 34.00],
    [37.00, 35.00, 2.75, 2.64, 19.00],
    [35.00, 35.00, 2.59, 2.59, 16.00],
    [37.00, 37.00, 2.73, 2.59, 22.00]
])

A = np.zeros((len(data),5))

A[:,0] = data[:,0]
A[:,1] = data[:,1]
A[:,2] = data[:,2]
A[:,3] = data[:,3]
A[:,4] = 1.

Q,R = np.linalg.qr(A)
lamda = np.linalg.solve(R,np.matmul(Q.T, data[:,4]))

'''
Es ist nicht möglich, hier die x-Werte in eine Funktion als Parameter zu übergeben, da
x dazu benutzt wird, das Messresultat als Ganzes zu identifizieren. Beispielsweise
x = 1 stünde für folgendes Resultat:
33,53,3.32,3.43 -> 29    

Man multipliziert daher die gesamte A-Matrix (welche alle Parameter auf einmal erhält)
mit dem lamda Vektor, welche die ausgerechneten Koeffizienten enthält. Wenn nun
ein Interesse besteht, zustäzliche Werte zu berechnen, kann wieder eine neue Matrix A
mit den Parametern gebaut werden und diese kann mit dem lamda-Vektor multiplizieren werden, 
um die entsprechenden Werte zu erhalten.
'''

#def F(x, lamda):
#    return lamda[0] * x + lamda[1] * x + lamda[2] * x + lamda[3] * x + lamda[4]

messungsnummern = np.arange(1,33,1)
messungsresultate = np.matmul(A,lamda)

plt.plot(messungsnummern, data[:,4],'ro')
plt.plot(messungsnummern, messungsresultate)

plt.xlabel('Nummer der Messung')
plt.grid()