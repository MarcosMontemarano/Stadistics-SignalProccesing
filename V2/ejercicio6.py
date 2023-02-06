# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:42:40 2022

@author: marco
"""

import numpy as np
from Mediamovild import mediamovild 
import scipy as sp
from scipy import signal
from ejercicio5 import xfd_A , M
from ejercicio1 import A
import matplotlib.pyplot as plt

# =============================================================================
# Respuesta en frecuencia de Moving Average h[n]
# =============================================================================

fs = 44100

N = np.linspace(0,2,2*fs) # Vector tiempo en funcion de Fs

n = len(A)


r_impulso=[1]*(M+1) 
H=np.zeros(len(r_impulso))  
for i in range(len(r_impulso)):
    H[i]=r_impulso[i]/(M+1)
                            
convolve = np.convolve(A,H,'same')

convolve /= max(convolve)

plt.figure(1)
plt.subplot(2,1,1)
plt.title('Señal filtrada por convolución lineal')
plt.xlabel('Muestras [n]')
plt.ylabel('Magnitud')
plt.xlim(0,(3*fs)/440)
plt.plot(abs(convolve))
plt.grid()
plt.subplot(2,1,2)
plt.title('Señal filtrada en punto anterior')
plt.xlabel('Muestras [n]')
plt.ylabel('Magnitud')
plt.xlim(0,(3*fs)/440)
plt.plot(abs(xfd_A))
plt.grid()
plt.tight_layout()
