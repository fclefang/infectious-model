import scipy.integrate as spi  
import numpy as np  
import pylab as pl  
  
beta=0.003
# gamma=0.1  
TS=1.0  
ND=50.0  
S0=99  
I0=1
INPUT = (S0, I0)  
  
def diff_eqs(INP,t):  
    '''''The main set of equations'''  
    Y=np.zeros((2))  
    V = INP  
    Y[0] = - beta * V[0] * V[1]  
    Y[1] = beta * V[0] * V[1] 
    # Y[2] = gamma * V[1]  
    return Y   # For odeint  
  
t_start = 0.0; t_end = ND; t_inc = TS  
t_range = np.arange(t_start, t_end+t_inc, t_inc)  
RES = spi.odeint(diff_eqs,INPUT,t_range)  
  
print RES  
  
#Ploting  
pl.subplot(111)  
pl.plot(RES[:,1], '-r', label='Infectious')  
pl.plot(RES[:,0], '-g', label='Susceptibles')  
# pl.plot(RES[:,2], '-k', label='Recovereds')  
pl.legend(loc=0)  
pl.title('SIR_Model.py')  
pl.xlabel('Time')  
# pl.ylabel('Infectious Susceptibles and Recovereds')  
pl.xlabel('Time')  
pl.show()  