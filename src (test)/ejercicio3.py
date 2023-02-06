# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:07:22 2022

@author: marco
"""

import scipy as sp
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from Desvio_estandar import de 

# =============================================================================
# Construcción de la señal limpia 
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
# Construccion de señales con ruido
# =============================================================================

tiempo_ruido = np.linspace(0,2,N) # Vector tiempo para plotear

x01_r = np.random.normal(0,0.1,len(n)) # Señales random

x1_r = np.random.normal(0,1,len(n))

x3_r = np.random.normal(0,3,len(n))

x01 = x01_r + A # Ruido sumado a la señal creada por broadcasting

x1 = x1_r + A

x3 = x3_r + A

x_rc = 10*np.ones((len(A))) # Señal constante de valor 1 y de igual longitud

x_c = x_rc + A

# =============================================================================
# Transformadas
# =============================================================================

espectro1 = sp.fftpack.fft(x01) # Transformadas rapidas de Fourier

espectro2 = sp.fftpack.fft(x1)

espectro3 = sp.fftpack.fft(x3)

eje_frec = sp.fftpack.fftfreq(len(A))*fs # Eje horizontal de frecuencias

espectro1 /= max(espectro1) # Normalizacion de la señal

espectro2 /= max(espectro2)

espectro3 /= max(espectro3)

# =============================================================================
# Calculo de relacion señal-ruido
# =============================================================================

# Se calcula la potencia de ambas señales para luego calcular el logaritmo del
# cociente y obtener SNR. Ambas señales tienen la misma duracion en muestras y 
# con valores reales. Las señales de ruido y las sumadas se pueden medir 
# por separadas.

# Calculo tipo 1: SNR=10Log10(Pseñal-Pruido/Pruido)

x01_r_pot = np.mean(x01_r**2) # Potencia señal ruido 

x01_pot = np.mean(x01**2) # Potencia señal + ruido

snr_01 = np.log10(((x01_pot)-(x01_r_pot))/x01_r_pot)*10 # SNR (dB)

x1_r_pot = np.mean(x1_r**2) # Potencia señal ruido 

x1_pot = np.mean(x1**2) # Potencia señal + ruido

snr_1 = np.log10(((x1_pot)-(x1_r_pot))/x1_r_pot)*10 # SNR (dB)

x3_r_pot = np.mean(x3_r**2) # Potencia señal ruido 

x3_pot = np.mean(x3**2) # Potencia señal + ruido

snr_3 = np.log10(((x3_pot)-(x3_r_pot))/x3_r_pot)*10 # SNR (dB)

xrc_pot = np.mean(x_rc**2) # Potencia señal ruido 

xc_pot = np.mean(x_c**2) # Potencial señal + ruido

snr_c = np.log10(((xc_pot)-(xrc_pot))/xrc_pot)*10 # SNR (dB)

print('Cálculo de relación señal-ruido tipo 1')
print('La relacion señal-ruido con sigma = 0.1 es:',round(snr_01,1),' dB')
print('La relacion señal-ruido con sigma = 1 es:',round(snr_1,1),' dB')
print('La relacion señal-ruido con sigma = 3 es:',round(snr_3,1),' dB')
print('La relacion señal-ruido con constante agregada:',round(snr_c,1),' dB')

# Calculo tipo 2: AmpMax/DesvEstandar(ruido)

amp_01 = max(x01)

snr_01 = amp_01/de(x01_r)

amp_1= max(x1)

snr_1 = amp_1/de(x1_r)

amp_3 = max(x3)

snr_3 = amp_1/de(x3_r)

amp_c = max(x_c)

snr_c = amp_c/de(x_rc)

print('')
print('Cálculo de relación señal-ruido tipo 2')
print('La relacion señal-ruido con sigma = 0.1 es:',round(snr_01,3))
print('La relacion señal-ruido con sigma = 1 es:',round(snr_1,3))
print('La relacion señal-ruido con sigma = 3 es:',round(snr_3,3))
print('La relacion señal-ruido con constante agregada:',round(snr_c,3))

# =============================================================================
# Figuras
# =============================================================================

# plt.figure(1)

# ax1 = plt.subplot(311)
# plt.tick_params('x', labelbottom=False)
# plt.xlim(0,2/f0) # Muestra solo 2 periodos
# plt.plot(tiempo_ruido,x01,linewidth=1.3)
# plt.grid()

# ax2 = plt.subplot(312)
# plt.tick_params('x', labelbottom=False)
# plt.ylabel('Amplitud')
# plt.xlim(0,2/f0) # Muestra solo 2 periodos
# plt.plot(tiempo_ruido,x1,linewidth=1.3)
# plt.grid()

# ax3 = plt.subplot(313)
# plt.xlim(0,2/f0) # Muestra solo 2 periodos
# plt.plot(tiempo_ruido,x3,linewidth=1.3)
# plt.xlabel('Tiempo [s]')
# plt.grid()

# plt.figure(2)
# plt.plot(eje_frec,abs(espectro1))
# plt.xlabel('Frecuencia [Hz]')
# plt.ylabel('Amplitud')
# plt.xlim(f0-100,f0*6)
# plt.title('Sigma = 0.1')
# plt.grid()

# plt.figure(3)
# plt.plot(eje_frec,abs(espectro2))
# plt.xlabel('Frecuencia [Hz]')
# plt.ylabel('Amplitud')
# plt.xlim(f0-100,f0*6)
# plt.title('Sigma = 1')
# plt.grid()

# plt.figure(4)
# plt.plot(eje_frec,abs(espectro3))
# plt.xlim(f0-100,f0*6)
# plt.xlabel('Frecuencia [Hz]')
# plt.ylabel('Amplitud')
# plt.title('Sigma = 3')
# plt.grid()

# plt.figure(5)

# plt.xlim(0,2/f0) # Muestra solo 2 periodos
# plt.plot(tiempo_ruido,x_c,linewidth=1.3)
# plt.xlabel('Tiempo [s]')
# plt.plot(tiempo_ruido,A,linewidth=1.3)
# plt.grid()

# plt.legend(['Tono + constante','Tono 440 Hz + 4 armonicos'])

# Al agregar un valor unitario constante al tono, se obtiene una relacion 
# señal ruido menor a 3. A medida que aumente el valor de esa constante, la
# SNR aumenta, es decir, mejora. 
# Lo que ocurre estadísticamente es que el desvío estandar crece menos rapido
# por ser un ruido "menos disperso", que la amplitud máxima de la señal.