def OCOG(w, n1=0, n2=0):
    import numpy as np
    w = w[n1:len(w)-n2]
    mini = np.min(w)
    maxi = np.max(w)
    w = (w - mini)/(maxi-mini)
    P_4 = np.sum(w**4)
    P_2 = np.sum(w**2)
    A = np.sqrt(P_4/P_2)
    W = (P_2**2)/P_4
    COG = np.dot(np.arange(n1,len(w) - n2, 1),w**2)/P_2
    LEP = COG - (W/2)
    return A*(maxi-mini)+mini, W, COG, LEP
