import math
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01#ms
C = 1.0#uF/cm^2
E_L = 10.6#mV
t_plot = []
pre_v_plot = []
post_v_plot = []
#---------------------------------------------------------------------------------------------------------------

def calc_v(P_s, v):
    #dvdt = (1.0/tau_m)*(E_L - v - r_mg_s*P_s*(v-E_s) + R_mI_e )
    dvdt = (1.0/tau_m)*(E_L - v - r_mg_s*(v-E_s) + R_mI_e )
    v = v + dvdt*dt
    return v

def P_syn(ft, t):
    return (P_max)*math.exp((ft-t)/tau_s)

if __name__ == '__main__':
    #initialization
    E_L = -70#mV
    E_s = 0.0#mV
    v_th = -54#mV
    v_reset = -80#mV
    tau_m = 20#ms
    tau_s = 10#ms
    P_max = 1.0
    r_mg_s = 0.05
    R_mI_e = 20
    pre_v = -65.0 #mV
    post_v = -70.0#mV
    P_s_pre = 0.0
    P_s_post = 0.0
    pspre_plot = []
    pspost_plot = []
    ft_pre = float('-inf')
    ft_post = float('-inf')
    
    t = -10.0 #ms
    
    while(t<500):
        R_mI_e = R_mI_e

        pre_v = calc_v(P_s_pre, pre_v)
        pre_v_plot = np.append(pre_v_plot, pre_v)
        
        if pre_v > v_th:
            pre_v = v_reset
            ft_pre = t
            
        t_plot = np.append(t_plot, t)
        t += dt
  
    fig = plt.figure(figsize=(10,5),dpi=200)
    plt.xlabel('t (ms)')
    plt.ylabel('V (mV)')
    plt.plot(t_plot, pre_v_plot)#, color='blue')
    plt.legend()
    #plt.savefig('fig.png')
    plt.show()
    
