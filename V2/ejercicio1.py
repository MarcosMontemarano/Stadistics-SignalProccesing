# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:21:31 2022

@author: marco
"""
# =============================================================================
# Importar librerías
# =============================================================================

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# =============================================================================
# Construcción de la señal completa 
# =============================================================================

K = 5 # Número de armónicos
f0 = 440 # Frecuencia fundamental (ciclos/muestra)
fs = 44100 # Frecuencia de muestreo
N = 2 * fs # Longitud de la señal (segundos)
n = np.arange(N) # Tiempo discreto
A = np.zeros(N).astype(float) # Vector de float's donde se almacenaran los valores de la señal
for k in range(1, K + 1): # Bucle que crea la señal con sus armonicos (Broadcasting)
    ck = (1/k) # Decaimiento de armonicos
    A += ck * np.sin(2*n*k*np.pi*f0/fs) # Señal
    
# =============================================================================
# Construccion de cada tono por separado (armonicos y fundamental)
# =============================================================================

tiempo_tono = np.linspace(0, 2, N)
tono1 = 1 * np.sin(2*np.pi*440*tiempo_tono)
tono2 = 1/2 * np.sin(2*np.pi*(2*440)*tiempo_tono)
tono3 = 1/3 * np.sin(2*np.pi*(3*440)*tiempo_tono)
tono4 = 1/4 * np.sin(2*np.pi*(4*440)*tiempo_tono)
tono5 = 1/5 * np.sin(2*np.pi*(5*440)*tiempo_tono)

# =============================================================================
# Transformada rapida de Fourier
# =============================================================================

espectro1 = sp.fftpack.fft(A) # Transformada rapida de Fourier a la señal
eje_frec = sp.fftpack.fftfreq(len(A)) * fs # Almacenar en un array desde 0 Hz hasta fs/2 Hz 
espectro1 /= max(espectro1) # Aplica modulo a la transformada para plotear magnitud

# =============================================================================
# Figuras
# =============================================================================

# Evitar que al llamar a este archivo desde 
# ejercicio4.py no se plotee, sino que solo llamará a las variables

if __name__ == '__main__': 
    plt.figure(1)    
    plt.plot(eje_frec,abs(espectro1))
    plt.title('Espectro LA440 con 4 armonicos')
    plt.xlim(f0-100,f0*6) # Limites considerables para visualizar los armonicos
    plt.xlabel('Frecuencia [Hz]') 
    plt.ylabel('Amplitud')
    plt.grid()
    plt.figure(2)
    plt.xlim(0,2/f0) # Muestra solo 2 periodos
    plt.plot(tiempo_tono, tono1, linewidth=1.3, label='440 Hz',
    color='blue')
    plt.plot(tiempo_tono, tono2, linewidth=1.3, label='880 Hz',
    color='orange')
    plt.plot(tiempo_tono, tono3, linewidth=1.3, label='1320 Hz',
    color='yellow')
    plt.plot(tiempo_tono, tono4, linewidth=1.3, label='1760 Hz',
    color='red')
    plt.plot(tiempo_tono, tono5, linewidth=1.3, label='2200 Hz',
    color='black')
    plt.title('Fundamental y sus armonicos')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.legend(fontsize='medium')
    plt.figure(3)
    plt.xlim(0,2/f0)
    plt.title('Señal total')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.plot(tiempo_tono,A,linewidth=1.3,color='blue')
