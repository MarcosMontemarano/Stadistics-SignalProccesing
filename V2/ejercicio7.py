# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:24:59 2022

@author: w10
"""

import numpy as np
from ejercicio5 import M
from ejercicio1 import A
import matplotlib.pyplot as plt

# =============================================================================
# Respuesta en frecuencia de Moving Average h[n]
# =============================================================================

fs = 44100

N = np.linspace(0,2,2*fs) # Vector tiempo en funcion de Fs

n = len(A)


h = 0.42 - 0.5*np.cos((2*np.pi*n)/(M-1)) + 0.08*np.cos((4*np.pi*n)/(M-1))

convolve = np.convolve(A,h,'same')

convolve /= max(convolve)

plt.figure()
plt.title('Señal filtrada por convolución lineal con V.Blackman')
plt.xlabel('Muestras [n]')
plt.ylabel('Magnitud')
plt.xlim(0,(3*fs)/440)
plt.plot(abs(convolve))
plt.grid()

