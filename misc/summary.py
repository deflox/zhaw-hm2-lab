import numpy as np

# ersteller einer matrix:
#    15 16 17
# 18
# 19
# 20
x,y = np.meshgrid(np.array([15,16,17]), np.array([18,19,20]))
print('x: \n', x)
print('y: \n', y)

# zeige nxn dimensionen im array
print('\n np.shape(x): \n', np.shape(x))

# erstellt punkte im interval mit gleichmässigem abstand
print('\n np.linspace(-5,5): \n', np.linspace(-5,5))