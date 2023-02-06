# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:43:47 2022

@author: marco
"""

import numpy as np
import Valor_medio

# =============================================================================
# Desvio estandar
# =============================================================================
def de(X):
    va_m = Valor_medio.vm(X) # Ingreso a al codigo el valor medio ya calculado en otra funcion    
    N = len(X) # Longitud de la señal
    resta = np.zeros(N) # En este vector se almacenara abs((x - sigma)^2)
    for i in range(N):
        resta[i] = abs(X[i]- va_m) # En este vector tengo todas las sumas del termino
    sumar_restas = 0 # En esta variable sumo todos los terminos del vector "resta" para tener un solo valor
    for n in range(N):
        sumar_restas = sumar_restas+resta[n]
        a1 = sumar_restas # Guardo en una variable mas comoda
    sigma = np.sqrt((1/(N-1))*a1)        # Sigma o Desv Estandar definitivo
    return sigma