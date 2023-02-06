# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:09:14 2022

@author: marco
"""

import numpy as np 

# =============================================================================
# Funcion filtro media movil recursivo, devuelve señal filtrada xdr
# =============================================================================

def mediamovildr(x,M):  # x: señal a filtrar
                        # M: tamaño de ventana del filtro
    N = len(x)
    y = np.zeros(N-M)
    for i in range((N-M)):
        if (i==0):
            suma = sum(x[i:i+M+1])
            y[i] = suma/(M+1)
        else:
            suma_2 = y[i-1] -(x[i-1]/(M+1)) +(x[i+M]/(M+1))
            y[i] = suma_2
    return(y)                  
    