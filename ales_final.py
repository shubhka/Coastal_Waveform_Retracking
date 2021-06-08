# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:38:03 2021

@author: Omen
"""
import numpy as np
from scipy.optimize import minimize
from scipy.special import erf
from scipy.constants import speed_of_light

def normalize(obj,a):
    o = []
    for i in range(len(obj)):
        o.append((obj[i] - min(obj))/(a - min(obj)))
    return o

def eight_point_moving_average(waveform):
    w = []
    for i in range(4,len(waveform)-4):
        w.append(sum(waveform[i-4:i+4])/8)
    w = np.array(w)
    return w

def detect_edge_foot(Dwf):
    for i in range(len(Dwf)):
        if (Dwf[i] > 0.01) and (Dwf[i+1] > 0):
            return i - 1
    raise ValueError('LeadingEdgeNotDetected')
    
def detect_edge_top(dwf):
    for i in range(len(dwf)):
        if dwf[i] < 0:
            return i
    raise ValueError('LeadingEdgeNotDetected')
    
def check(p):
    for i in range(len(p)):
        if p[i] < 0.10:
            return False
    return True
    
def lead_edge_detection(waveform):
    T_n = sum(waveform[0:6])/6
    waveform = waveform - T_n
    Dwf = []
    for i in range(1,len(waveform)):
        Dwf.append(waveform[i]-waveform[i-1])
    i = 0
    while(i < len(Dwf)):
        edge_foot = detect_edge_foot(Dwf[i:])
        stopgate = detect_edge_top(Dwf[edge_foot+1:len(Dwf)]) + 1 + edge_foot
        if check(waveform[stopgate-1:stopgate+3]):
            return edge_foot,stopgate,T_n
        i = edge_foot + 1
    raise ValueError('LeadingEdgeNotDetected')
    
def Brown_Hayne(t,ep,SWH,tau,P_n,T_n):
    gamma = np.sin(1.29)*np.sin(1.29)*0.721
    a_e = np.exp(-4*np.sin(ep)*np.sin(ep)/gamma)
    sigma_s = SWH/2*3e8
    sigma_c = np.sqrt((1.65e-9*1.65e-9 + sigma_s*sigma_s))
    b_e = np.cos(2*ep)- np.sin(2*ep)*np.sin(2*ep)/gamma
    a = 4*3e8/(gamma*815000*(1 + 815000/6400000))
    c_e = b_e * a
    u = (t - tau- sigma_c*sigma_c*c_e)/1.414*sigma_c
    v = c_e*(t - tau - c_e*sigma_c*sigma_c/2)
    V_m = T_n + a_e*P_n*((1+erf(u))/2)*np.exp(-v)
    return V_m

def residual(t,ep,sigma_p,h,R_e,T_n,SWH,tau,P_n,y):
    return Brown_Hayne(t,ep,SWH,sigma_p,h,R_e,tau,P_n,T_n) - y
    
def fit(t,SWH,tau,P_n,ep,T_n):
    fit = minimize(residual(t,ep,T_n),[SWH,tau,P_n],method='Nelder-Mead',tol = 1e-10,options={'maxiter':600})

def ALES(waveform):
    avg_waveform = (waveform,max(eight_point_moving_average(waveform)))
    avg_waveform = avg_waveform[5:len(avg_waveform)-5]
    edge_foot, stopgate, T_n = lead_edge_detection(avg_waveform)
     
k = Brown_Hayne(3.125, 0.1, 1, 1, 1, 0.0005)
print(k)