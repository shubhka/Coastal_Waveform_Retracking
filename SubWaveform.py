# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:38:41 2021

@author: Omen
"""

def detect_edge_foot(Dwf):
    for i in range(len(Dwf)):
        if (Dwf[i] > 0.01) and (Dwf[i+1] > 0):
            return i
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
    Dwf = []
    for i in range(1,len(waveform)):
        Dwf.append(waveform[i]-waveform[i-1])
    i = 0
    while(i < len(Dwf)):
        edge_foot = detect_edge_foot(Dwf[i:])
        stopgate = detect_edge_top(Dwf[edge_foot+1:len(Dwf)]) + 1 + edge_foot
        if check(waveform[stopgate-1:stopgate+3]):
            return edge_foot,stopgate
        i = stopgate + 1
    raise ValueError('LeadingEdgeNotDetected')