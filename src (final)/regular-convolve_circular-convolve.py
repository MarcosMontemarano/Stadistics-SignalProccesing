# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:38:28 2022

@author: Usuario
"""

import soundfile as sf
import numpy as np
from broadcasting_rfft import A
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve
from conv_circular import circular_convolve

#importo la señal de audio
(h, fs) = sf.read('Resp_Imp.wav') # respuesta al impulso
L1= len(h)

#La grafico
t1 = np.linspace(0,len(h)/fs,num = len(h))
plt.figure(figsize=(9, 5), dpi=80)
plt.plot(t1,h)
plt.ylabel('Amplitud')
plt.xlabel('Tiempo [s]')
plt.title('Respuesta al impulso')

fs = 44100
N = np.linspace(0,2,2*fs) # Vector tiempo en funcion de Fs
M1 = len(A)

# %%%%%%%%%%
H=np.zeros(len(h)) 
for i in range(len(h)):
    H[i]=h[i]
                            
convolve = np.convolve(A,H,'same')

convolve /= max(convolve)

plt.figure()
plt.title('Señal filtrada por convolución lineal')
plt.xlabel('Muestras [n]')
plt.ylabel('Magnitud')
plt.xlim(0,(3*fs)/440)
plt.plot(abs(convolve))
plt.grid()
plt.show()
#%%%%

circular = circular_convolve(A, H, period)
circular /= max(circular)

plt.figure()
plt.title('Señal filtrada por convolución circular')
plt.xlabel('Muestras [n]')
plt.ylabel('Magnitud')
plt.xlim(0,(3*fs)/440)
plt.plot(abs(circular))
plt.grid()
plt.show()
# %%%%%%%%%%%%%

#Transformo la rpta al impulso y la señal

freqsH = np.fft.rfftfreq(L1, 1/fs)
TH = np.fft.rfft(h)
espectroH = np.abs(TH)
espectroH[0] = 0

plt.figure()
plt.plot(freqsH, espectroH, 'r')
plt.grid()
plt.xlim([0, 13000])
plt.title('FFT del impulso')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.show()

freqsA = np.fft.rfftfreq(M1, 1/fs)
TA = np.fft.rfft(A)
espectroA = np.abs(TA)
espectroA[0] = 0

plt.figure()
plt.plot(freqsA, espectroA, 'b')
plt.grid()
plt.xlim([0, 3000])
plt.title('FFT de la señal')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.show()

#completo con ceros

N1 = M1 + L1 - 1

zerosA=np.zeros(N1-M1)
zerosh= np.zeros(N1-L1)

TAz = np.fft.rfft(zerosA)
THz = np.fft.rfft(zerosh)

#multiplico las transformadas con ceros 
Yz = TAz * THz #!!!!

#aplico IDFT de Y[k]  para obtener y[n]
YzDFT = np.fft.irfft(Yz)

plt.figure()
plt.plot(N, YzDFT, 'b')
plt.grid()
plt.title('IFFT')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.show()

