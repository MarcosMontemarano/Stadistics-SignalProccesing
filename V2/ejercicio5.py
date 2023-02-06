# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:08:46 2022

@author: marco
"""

import numpy as np
from ejercicio1 import A
import matplotlib.pyplot as plt
import scipy as sp
from scipy.fftpack import fft
from Mediamovild import mediamovild
from Mediamovilr import mediamovildr
from timeit import default_timer

# =============================================================================
# FFT de la señal 
# =============================================================================

fs = 44100

N = np.linspace(0,2,2*fs) # Vector tiempo en funcion de Fs

A_fft = sp.fftpack.fft(A)

A_fftfreq = sp.fftpack.fftfreq(len(A)) * fs

A_fftabs = abs(A_fft)

A_fft /= max(A_fft)

# =============================================================================
# Selección del tamaño de la ventana de filtrado M
# =============================================================================

# Para hallar el largo en muestras del filtro, tomando la expresión de la 
# respuesta en frecuencia del MA, el cual se ajusta al valor 
# correspondiente que se desea en la frecuencia de corte. Luego, se halla
# el valor de omega (2*pi*440/44100) y se prueba con valores de N que 
# proporcionen la mejor concordancia entre ambos lados de la ecuación.  

M = 70 # Prueba

Resp_frec = (1/M)*abs(np.sin((2*np.pi*440/fs)*M/2)/np.sin((2*np.pi*440/fs)/2))

w = 2*np.pi*440/fs

# =============================================================================
# Filtrado de señales y calculo de tiempo de ejecución
# =============================================================================

xfd_A = mediamovild(A,M)

inicio_1 = default_timer()
xfd_A = mediamovild(A,M) # Filtro media movil directo
fin_1 = default_timer()
Tiempo_1 = fin_1-inicio_1
Tiempo_1 = round(Tiempo_1,6)

xfr_A = mediamovildr(A,M)

inicio_2 = default_timer()
xfr_A = mediamovildr(A,M) # Filtro media movil recursivo
fin_2 = default_timer()
Tiempo_2 = fin_2-inicio_2
Tiempo_2 = round(Tiempo_2,6)

xfd_A = np.hstack([np.zeros(M//2),xfd_A,np.zeros(M//2)]) 

xfr_A = np.hstack([np.zeros(M//2),xfr_A,np.zeros(M//2)])

# =============================================================================
# FFT de señales filtradas
# =============================================================================

xfd_fft = sp.fftpack.fft(xfd_A) # Transformada rápida de Fourier

xfdA_fftfreq = sp.fftpack.fftfreq(len(xfd_A)) * fs 

xdfA_fftabs = abs(xfd_fft)

xdfA_fftabs /= max(xdfA_fftabs)

xfd_fft /= max(xfd_fft)

xfr_fft = sp.fftpack.fft(xfr_A) # Transformada rápida de Fourier

xfrA_fftfreq = sp.fftpack.fftfreq(len(xfr_A)) * fs

xfrA_fftabs = abs(xfr_fft)

xfrA_fftabs /= max(xfrA_fftabs)

xfr_fft /= max(xfr_fft)

A_fft /= max(A_fft)

# =============================================================================
# Ploteos
# =============================================================================
if __name__ == '__main__':
    plt.figure(1)
    plt.subplot(3,1,1)
    plt.plot(N,A)
    plt.xlim(0,3/440)
    plt.title('Señal original')
    plt.grid()
    plt.subplot(3,1,2)
    plt.plot(N,xfd_A)
    plt.xlim(0 + len(np.zeros(M//2))/fs,3/440)
    plt.title('Señal filtrada')
    plt.grid()
    plt.subplot(3,1,3)
    plt.plot(N,xfr_A)
    plt.xlim(0 + len(np.zeros(M//2))/fs,3/440)
    plt.title('Señal filtrada con metodo recursivo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Magnitud')
    plt.grid()
    plt.tight_layout()
    plt.figure(2)
    plt.subplot(3,1,1)
    plt.plot(A_fftfreq,abs(A_fft))
    plt.xlim(0,2700)
    plt.title('Espectro señal original')
    plt.grid()
    plt.subplot(3,1,2)
    plt.plot(xfdA_fftfreq,abs(xdfA_fftabs))
    plt.xlim(0,2700)
    plt.title('Espectro señal filtrada')
    plt.grid()
    plt.subplot(3,1,3)
    plt.plot(xfrA_fftfreq,abs(xfrA_fftabs))
    plt.xlim(0,2700)
    plt.title('Espectro señal filtrada met. recursivo')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid()
    plt.tight_layout()
    
    print('Tiempo de ejecución filtro directo: ',Tiempo_1,' s')
    print('')
    print('Tiempo de ejecución filtro recursivo: ',Tiempo_2,' s')
    print('')
    print('Para una magnitud de 0.4 en la frecuencia de corte')
    print('')
    print('Con un valor de M de:' , M,)
    print('')
    print('Se obtiene del otro lado de la igualdad un valor de:',round(Resp_frec,1))
    print('')