import numpy as np

def lagrange(n,i,x,points):
    out = 1
    for j in range(0, n+1):
        if j != i:
            out *= (x-points[j][0])/(points[i][0]-points[j][0])
    return out

points = np.array([
    [1,1],
    [3,3],
    [5,1],
],dtype=np.float)

x_to_search = 2
polynom_degree = 2

result = 0
for i in range(0, len(points)):
    result += points[i][1]*lagrange(polynom_degree,i,x_to_search,points)

print(result)