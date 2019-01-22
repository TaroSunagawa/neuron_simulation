import math
import numpy as np
import matplotlib.pyplot as plt

#parameters
dt = 0.01#ms
C = 1.0#uF/cm^2
g_L = 0.3#mS/cm^2
g_K = 36.0#mS/cm^2
g_Na = 120.0#mS/cm^2
E_L = 10.6#mV
E_K = -12.0#mV
E_Na = 115.0#mV

#buffer for plot 
v_plot = []
t_plot = []
n_plot = []
m_plot = []
h_plot = []

#alpha
def alpha_n(v):
    return (0.1-0.01*v)/(math.exp(1.0-0.1*v)-1.0)
def alpha_m(v):
    return (2.5-0.1*v)/(math.exp(2.5-0.1*v)-1.0)
def alpha_h(v):
    return 0.07*math.exp(-v/20.0)

#beta
def beta_n(v):
    return 0.125*math.exp(-v/80.0)
def beta_m(v):
    return 4.0*math.exp(-v/18.0)
def beta_h(v):
    return 1.0/(math.exp(3.0-0.1*v)+1.0)

#initial n,m,h
def n_0(v):
    return alpha_n(v)/(alpha_n(v)+beta_n(v))
def m_0(v):
    return alpha_m(v)/(alpha_m(v)+beta_m(v))
def h_0(v):
    return alpha_h(v)/(alpha_h(v)+beta_h(v))

#calculate each step
def dndt(v):
    return alpha_n(v)*(1-n) - beta_n(v)*n
def dmdt(v):
    return alpha_m(v)*(1-m) - beta_m(v)*m
def dhdt(v):
    return alpha_h(v)*(1-h) - beta_h(v)*h
def dvdt(v, n, m, h, I):
    return (1.0/C)*( -g_L*(v-E_L) -g_K*n**4*(v-E_K) -g_Na*m**3*h*(v-E_Na) +I)

#start step current
def step(t):
    if t<=0.0:
        return 1.0
    else: return 0.0

#euler method 
def euler(v,n,m,h,I):
    v = v + dvdt(v, n, m, h, I)*dt
    n = n + dndt(v)*dt
    m = m + dmdt(v)*dt
    h = h + dhdt(v)*dt
    return v,n,m,h


if __name__ == '__main__':
    #initialization
    t = -100.0 #ms
    v = 0.0#mV
    n = n_0(v)
    m = m_0(v)
    h = h_0(v)
    
    I1 = 7.0 #uA/cm^2
    dI = 4.0 #uA/cm^2
    
    
    while(t<100):
        I = I1 - dI*step(t)
        v,n,m,h = euler(v,n,m,h,I)
        v_plot = np.append(v_plot, v)
        n_plot = np.append(n_plot, n)
        m_plot = np.append(m_plot, m)
        h_plot = np.append(h_plot, h)
        t_plot = np.append(t_plot, t)
        t += dt
        
    fig = plt.figure(figsize=(10,5),dpi=200)
    plt.xlabel('t (ms)')
    plt.ylabel('V (mV)')
    plt.ylim([-20,100])
    plt.xlim([-10,100])
    plt.plot(t_plot, v_plot)
    #ax0 = fig.add_subplot(1,1,1)
    #ax0.set_xlabel('t (ms)')
    #ax0.set_ylabel('V (mV)')
    #ax0.set_xlim([-10,100])
    ##ax0.set_ylim([0,6])
    #ax0.plot(t_plot, v_plot)
    #ax0.grid()
    ##plt.savefig('fig.png')
    plt.show()
    
    #fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(4,10))
