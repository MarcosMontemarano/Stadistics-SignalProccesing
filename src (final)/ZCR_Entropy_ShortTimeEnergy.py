# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:04:55 2022

@author: Usuario
"""

import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import math
from math import log, e
import wave
import scipy.io.wavfile
import scipy.stats
import soundfile as sf

#importo las señales de audio
s1, fs = sf.read('Sen_al1.wav')
N1= len(s1)

s2, fs = sf.read('Sen_al2.wav') 
N2= len(s2)

s3, fs = sf.read('Sen_al3.wav') 
N3= len(s3)

#Las grafico
t1 = np.linspace(0,len(s1)/fs,num = len(s1))
plt.figure(1,figsize=(9, 5), dpi=80)
plt.plot(t1,s1)
plt.title('Señal 1')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo [s]')
plt.show()

t2 = np.linspace(0,len(s2)/fs,num = len(s2))
plt.figure(2,figsize=(9, 5), dpi=80)
plt.plot(t2,s2)
plt.title('Señal 2')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo [s]')
plt.show()

t3 = np.linspace(0,len(s3)/fs,num = len(s3))
plt.figure(3,figsize=(9, 5), dpi=80)
plt.plot(t3,s3)
plt.title('Señal 3')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo [s]')
plt.show()

# =============================================================================
# Definición de funciones 
# =============================================================================

#Energía en tiempos cortos

def fragmento(l, k): #Partes de tamaño k de una lista dada.
  for i in range(0, len(l), k):
    yield l[i:i+k]

def STE(frame): #Calcula la energía en tiempos cortos de un cuadro de audio.
  return sum( [ abs(x)**2 for x in frame ] ) / len(frame)

def rateSampleByVariation(fragmento): 
#Califica una muestra de audio utilizando el coeficiente de variación
#de su energía a corto plazo
  energ = [ STE(chunk) for chunk in fragmento ]
  return scipy.stats.variation(energ)

# Entropía de una señal

def entropy2(labels, base=None): # Calculo de la entropía, utiliza como 
                                 # variables, la señal y la Base del logaritmo 

  n_labels = len(labels)

  if n_labels <= 1:
    return 0

  value,counts = np.unique(labels, return_counts=True)
  probs = counts / n_labels
  n_classes = np.count_nonzero(probs)

  if n_classes <= 1:
    return 0

  ent = 0.

  base = e if base is None else base
  for i in probs:
    ent -= i * log(i, base)

  return ent

#Zero-Crossing Rate

def ZCR(x,w):
    wlen = len(x)
    step = w
    frameNum = round(wlen/step)
    zcr = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = x[np.arange(i*step,min(i*step+w,wlen))]
        curFrame = curFrame - np.mean(curFrame)
        
        zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<=0)
    return zcr

#pruebo en las señales
#leo la señal 1
s1 = wave.open('Sen_al1.wav','rb')
params = s1.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = s1.readframes(nframes)
señal = np.fromstring(str_data, dtype=np.short)
señal.shape = -1, 1
s1.close()

#calculo Zero Cross Rate
w = 240
zcr = ZCR(señal[11022:60785,:],w)

#grafico
tiempo = np.arange(0, len(señal[11022:60785,:])) * (1.0 / framerate) #normalización
tiempo2 = np.arange(0, len(zcr)) * (len(señal[11022:60785,:])/len(zcr) / framerate)
plt.figure(4)
plt.subplot(211)
plt.plot(tiempo, señal[11022:60785,:])
plt.ylabel("Amplitud")
plt.xlim([0,59000/fs])
plt.subplot(212)
plt.plot(tiempo2, zcr)
plt.ylabel("ZCR")
plt.xlim([0,59000/fs])
plt.ylim([0,50])
plt.xlabel("tiempo (segundos)")
plt.show()


# =============================================================================
# Calculos / Resultados a modo de ejemplo
# =============================================================================

#leo la señal 2
s2 = wave.open('sen_al2.wav','rb')
params = s2.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = s2.readframes(nframes)
señal = np.fromstring(str_data, dtype=np.short)
señal.shape = -1, 1
s2.close()

#calculo Zero Cross Rate
w = 240
zcr = ZCR(señal,w)

#grafico
tiempo = np.arange(0, len(señal)) * (1.0 / framerate) #normalización
tiempo2 = np.arange(0, len(zcr)) * (len(señal)/len(zcr) / framerate)
plt.figure(5)
plt.subplot(211)
plt.plot(tiempo, señal)
plt.ylabel("Amplitud")
plt.subplot(212)
plt.plot(tiempo2, zcr)
plt.ylabel("ZCR")
plt.xlabel("tiempo (segundos)")
plt.show()

#leo la señal 3
s3 = wave.open('sen_al3.wav','rb')
params = s3.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = s3.readframes(nframes)
señal = np.fromstring(str_data, dtype=np.short)
señal.shape = -1, 1
s3.close()

#calculo Zero Cross Rate
w = 240
zcr = ZCR(señal,w)

#grafico
tiempo = np.arange(0, len(señal)) * (1.0 / framerate) #normalización
tiempo2 = np.arange(0, len(zcr)) * (len(señal)/len(zcr) / framerate)
plt.figure(6)
plt.subplot(211)
plt.plot(tiempo, señal)
plt.ylabel("Amplitud")
plt.subplot(212)
plt.plot(tiempo2, zcr)
plt.ylabel("ZCR")
plt.xlabel("tiempo (segundos)")
plt.show()

# Tamaño del frame en ms.
tamañoframe = 50
fs = 44100
numSamplesporFrame = int(fs * tamañoframe)

leoseñal1 = scipy.io.wavfile.read( "Sen_al1.wav"  )
STE1 = STE(leoseñal1)
tiempo = np.linspace(0,len(STE1)/fs,num = len(STE1))

#grafico
plt.figure(7)
plt.subplot(211)
plt.plot(t1,leoseñal1[1])
plt.ylabel("Amplitud")
plt.xlabel("Tiempo (segundos)")
plt.subplot(212)
plt.plot(t1,STE1)
plt.ylabel("STE")
plt.xlabel("Tiempo (segundos)")
plt.tight_layout()
plt.show()

leoseñal2 = scipy.io.wavfile.read( "Sen_al2.wav"  )
STE2 = STE(leoseñal2)
tiempo2 = np.linspace(0,len(STE2)/fs,num = len(STE2))

#grafico
plt.figure(8)
plt.subplot(211)
plt.plot(t2, leoseñal2[1])
plt.ylabel("Amplitud")
plt.xlabel("Tiempo (segundos)")
plt.subplot(212)
plt.plot(t2,STE2)
plt.ylabel("STE")
plt.xlabel("Tiempo (segundos)")
plt.tight_layout()
plt.show()

leoseñal3 = scipy.io.wavfile.read( "Sen_al3.wav"  )
STE3 = STE(leoseñal3)
tiempo3 = np.linspace(0,len(STE3)/fs,num = len(STE3))

#grafico
plt.figure(9)
plt.subplot(211)
plt.plot(t3, leoseñal3[1])
plt.ylabel("Amplitud")
plt.xlabel("Tiempo (segundos)")
plt.subplot(212)
plt.plot(t3,STE3)
plt.ylabel("STE")
plt.xlabel("Tiempo (segundos)")
plt.tight_layout()
plt.show()

# Prints valores de entropía

print('')
print('El valor de Entropía de la señal 1 es:',round(entropy2(leoseñal1[1],2),2))
print('')
print('El valor de Entropía de la señal 2 es:',round(entropy2(leoseñal2[1],2),2))
print('')
print('El valor de Entropía de la señal 3 es:',round(entropy2(leoseñal3[1],2),2))
print('')
