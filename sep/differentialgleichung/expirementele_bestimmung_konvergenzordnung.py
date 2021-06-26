import numpy as np

'''
Dieses Script überprüft experimentell die Konvergenzordnung des Mittelpunkt
Verfahrens. Laut script ist diese p=2.

Die im Script aufgeführte Fehlerabschätzung verwendet Konstante C, die jedoch
nicht bekannt ist, daher hier diese nummerische Abschätzung.
'''

# mittelpunkt verfahren, dass nur am schluss den y wert nach n schritten ausgibt
def midpoint(f, a, b, y0, n):
    x = a
    y = y0
    h = (b - a)/n
    for i in range(n):
        x_half = x + h/2
        y_half = y + h/2*f(x, y)
        x = x + h
        y = y + h*f(x_half, y_half)
    return y

# differentialgleichung
def f(x,y):
    return x**2 + 0.1*y

# exakte lösung der differentialgleichung
def y_exakt(x):
    return -10*x**2 - 200*x - 2000 + 1722.5*np.exp(0.05*(2*x+3))

# von bis wert für das folgen des richtungsfeldes
a = -1.5
b = 1.5

# startwert
y0 = 0

'''
Nun wird für n=10,100,1000,10000 (Interval h wird also immer kleiner) das
Mittelwert Verfahren angewandt

Man wird sehen das für eine erhöhung der Schrittweite n um den Faktor 10
der Fehler um den Faktor 100 abnimmt was p=2 entspricht.
'''
for n in [10, 100, 1000, 10000]:
    y = midpoint(f, a, b, y0, n)
    err = np.abs(y - y_exakt(b))
    print('n =', n, 'err =', err)