import numpy as np

def rudinleo_S11_Aufg3(f,a,b,n,y0):
    x,h = np.linspace(a,b,n+1,retstep=True,endpoint=True)
    
    y_euler = np.zeros(np.shape(x)[0])
    y_mittelpunkt = np.zeros(np.shape(x)[0])
    y_modeuler = np.zeros(np.shape(x)[0])
    
    y_euler[0]=y0
    y_mittelpunkt[0]=y0
    y_modeuler[0]=y0
    
    for i in range(0,len(x)-1):
        # Euler-Verfahren
        y_euler[i+1]=y_euler[i]+h*f(x[i],y_euler[i])
        
        # Mittelpunkt-Verfahren
        x_half=x[i]+h/2
        y_half=y_mittelpunkt[i]+h/2*f(x[i],y_mittelpunkt[i])
        y_mittelpunkt[i+1]=y_mittelpunkt[i]+h*f(x_half,y_half)
        
        # Modifiziertes Euler-Verfahren
        y_eul=y_modeuler[i]+h*f(x[i],y_modeuler[i])
        k1=f(x[i],y_modeuler[i])
        k2=f(x[i+1],y_eul)
        y_modeuler[i+1]=y_modeuler[i]+h*(k1+k2)/2
        
    return x,y_euler,y_mittelpunkt,y_modeuler