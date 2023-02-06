# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:43:05 2022

@author: marco
"""

# =============================================================================
# Valor medio
# =============================================================================

def vm(X):
    N = len(X) # Longitud en muestras de la señal
    x1 = 0 # Inicia en 0 
    for n in range(N):
        x1 = x1+X[n]
        x = x1/N
        return x