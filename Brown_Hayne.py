# -*- coding: utf-8 -*-
"""
Brown Hayne model

@author: Shubhi Kant
"""

import numpy as np
from scipy.special import erf


def Brown_Hayne(SWH,tau,P_n,t,ep):
    gamma = np.sin(1.29*np.pi/180)*np.sin(1.29*np.pi/180)*0.721
#    print(gamma)
    a_e = np.exp(-4*np.sin(ep*np.pi/180)*np.sin(ep*np.pi/180)/gamma)
#    print(a_e)
    sigma_s = SWH/(2*2.99792e8)
#    print(sigma_s)
    sigma_c = np.sqrt((1.65e-9*1.65e-9 + sigma_s*sigma_s))
#    print(sigma_c)
    b_e = np.cos(2*ep*np.pi/180)- (np.sin(2*ep*np.pi/180)*np.sin(2*ep*np.pi/180)/gamma)
#    print(b_e)
    a = 4*2.99792e8/(gamma*815000*(1 + 815000/6371000))
#    print(a)
    c_e = b_e * a
#    print(c_e)
    u = (t - tau- sigma_c*sigma_c*c_e)/(1.414*sigma_c)
#    print(u)
    v = c_e*(t - tau - (c_e*sigma_c*sigma_c/2))
#    print(v)
    V_m = a_e*P_n*((1+erf(u))/2)*np.exp(-v)
    return V_m

