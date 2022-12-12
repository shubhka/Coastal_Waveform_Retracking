# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:38:03 2021
@title: Threshold Retracker
@author: Shubhi Kant
"""

import numpy as np

class threshold():
    def __init__(self, P, q=0.5):
        """
        P : (Double) Numpy Array, Powers in return waveform
        q : (Float) Power Ratio
        """
        
        P_4 = np.sum(P**4)
        P_2 = np.sum(P**2)
        
        #Calculating the amplitude
        self.A = (P_4/P_2)**(0.5)   
        
        #Calculating the noise
        self.Pn = np.sum(P[0:5])/5           
        
        #Calculating the Threshold
        self.Th = (self.A - self.Pn)*q + self.Pn   
        
        #For calculating the First gate of exceedence
        Gk_1 = 0
        for i in range(len(P)):   
            if P[i] > self.Th:
                Gk_1 = i - 1 
                break
                
        #For calculating the returning gate    
        self.Gr = Gk_1 + (self.Th - P[Gk_1])/(P[Gk_1 + 1] - P[Gk_1])   
        
