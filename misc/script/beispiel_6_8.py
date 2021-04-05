import numpy as np

x = np.array([0,1,2,3,4])
y = np.array([3,1,.5,.2,.05])

A = np.zeros((5,2))
A[:,0] = 1
A[:,1] = x

Q,R = np.linalg.qr(A)

# beim ausrechnen müssen die y-Werte logarithmiert werden
lamda = np.linalg.solve(R,np.matmul(Q.T, np.log(y)))

print(lamda)