# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:35:54 2022

@author: marco
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# =============================================================================
# Funcion filtro media movil directo, devuelve señal filtrada xfd
# =============================================================================

def mediamovild(x,M): # x: señal a filtrar
                      # M: tamaño de ventana del filtro
    n = len(x) # Cantidad de muestras de la señal x
    xfd = np.zeros(n-M) # Vector de ceros donde se almacena la señal filtrada
    for i in range(n-M): # Ciclo de longitud nro de muestras - tamaño ventana
        sumatoria = sum(x[i:i+M+1])
        xfd[i] = sumatoria/(M+1)
    w, h = signal.freqz(xfd,x)
    if __name__ == '__main__':
        plt.figure(3)
        plt.plot(w, 20 * np.log10(abs(h)))
        # plt.xlim(-np.pi,np.pi)
        plt.title('Respuesta en frecuencia filtro')
        plt.ylabel('Magnitud [dB]')
        plt.xlabel('Frecuencia angular [rad/samples]')
        plt.grid()
    return xfd


   

