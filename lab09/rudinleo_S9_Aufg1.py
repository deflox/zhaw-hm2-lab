import numpy as np
import matplotlib.pyplot as plt

def second_diff(x):
    return -2./x**2

x_values = np.arange(1,2,0.001)
plt.plot(x_values,second_diff(x_values),label='2te Ableitung ln(x**2)')
plt.legend()
plt.grid()
plt.show()

def fourth_diff(x):
    return -12./x**4

plt.plot(x_values,fourth_diff(x_values),label='4te Ableitung ln(x**2)')
plt.legend()
plt.grid()
plt.show()