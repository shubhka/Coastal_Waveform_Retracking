# -*- coding: utf-8 -*-
"""
Beta 5 Retracker

@author: Shubhi Kant
"""
# Give t input as 0 to 128
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize
from OCOG import OCOG
from Plotter import plotter
            
def beta5 (t,b1,b2,b3,b4,b5):
    def Q(t):
        if t < b3 - b4*2:
            return 0
        else:
            return t - b3 - 0.5*b4
    
    def P(x):
        return quad(lambda q : (1/np.sqrt(2*np.pi))*np.exp(-0.5*q**2), -np.inf, x)[1]
    
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = b1 + b2*np.exp((-1)*b5*Q(t[i]))*P((t[i]-b3)/b4)
    return y

def residual(x,P,t,A):
    return np.dot((P-beta5(t, 0, A, x[0], x[1], 0)),(P-beta5(t, 0, A, x[0], x[1], 0)))

class beta5_Re():
    
    def __init__(self,P,n1):
        t = np.arange(n1,n1+len(P),1)
        O = OCOG(P)
        res = minimize(residual,[O.LEP,O.W],args=(P,t,O.A),method='Nelder-Mead',tol = 10e-8, options={'maxiter':600})
        print(res)
'''       if res.success:
            self.b1 = 0
            self.b2 = O.A
            self.b3 = res.x[0]
            self.b4 = res.x[1]
            self.b5 = 0
            self.y = beta5(t, self.b1, self.b2, self.b3, self.b4, self.b5)
        else:
            print('Convergence Failed')
'''            
def beta_r(P,n1,display = False, fig = True):
    B = beta5_Re(P, n1)
    if display:
        print('beta 1 :',B.b1)
        print('beta 2 :',B.b2)
        print('beta 3 :',B.b3)
        print('beta 4 :',B.b4)
        print('beta 5 :',B.b5)
        if fig:
            plotter(P,method = 'Beta5', y = B.y)
    return B

def residual1(b,P,t,A):
    return np.dot((P-beta5(t, 0, A, b[0], b[1], b[2])),(P-beta5(t, 0, A, b[0], b[1], b[2])))

class beta5_Re1():
    
    def __init__(self,P,n1):
        t = np.arange(n1,n1+len(P),1)
        O = OCOG(P)
        res = minimize(residual,[O.LEP,O.W,0],args=(P,t,O.A),method='Nelder-Mead',tol = 10e-8, options={'maxiter':600})
        if res.success:
            self.b1 = 0
            self.b2 = O.A
            self.b3 = res.x[0]
            self.b4 = res.x[1]
            self.b5 = res.x[2]
            self.y = beta5(t, self.b1, self.b2, self.b3, self.b4, self.b5)
        else:
            print('Convergence Failed')

def beta_r1(P,n1,display = False, fig = True):
    B = beta5_Re1(P, n1)
    if display:
        print('beta 1 :',B.b1)
        print('beta 2 :',B.b2)
        print('beta 3 :',B.b3)
        print('beta 4 :',B.b4)
        print('beta 5 :',B.b5)
        if fig:
            plotter(P,method = 'Beta5', y = B.y)
    return B


