import numpy as np

def rudinleo_S8_Aufg3a(x, y):
    Tf = 0
    for i in range(0, x.size-1):
        Tf = Tf + (y[i]+y[i+1])/2 * (x[i+1]-x[i])
    
    return Tf

r = np.array([0.,800.,1200.,1400.,2000.,3000.,3400.,3600.,4000.,5000.,5500.,6370.],dtype = "float" ) # Erdradius in km
rho = np.array([13000.,12900.,12700.,12000.,11650.,10600.,9900.,5500.,5300.,4750.,4500.,3300.],dtype = "float") # Spez. Dichte Erde in kg/m**3
r_scaled = 1000.*r

f=rho*4.*np.pi*r_scaled**2

Tf_neq = rudinleo_S8_Aufg3a(r_scaled, f)
Tf_neq_lit = 5.976e24

f_abs = np.abs(Tf_neq-Tf_neq_lit)
f_rel = f_abs / Tf_neq_lit

print('Berechnete Erdmasse: ', Tf_neq)
print('Absoluter Fehler: ', f_abs)
print('Relativer Fehler: ', f_rel)

#Berechnete Erdmasse:  6.02609577351443e+24
#Absoluter Fehler:  5.009577351442909e+22
#Relativer Fehler:  0.008382826893311428