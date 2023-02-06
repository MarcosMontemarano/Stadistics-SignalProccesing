# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:07:36 2022

@author: marco
"""

import numpy as np
from ejercicio1 import A
from Desvio_estandar import de
import matplotlib.pyplot as plt

# =============================================================================
# Creacion de 10 señales distintas con ruido dentro de un bucle
# para luego obtener una "señal promedio"
# =============================================================================

fs = 44100

t = np.linspace(0,2,2*fs) # Vector tiempo (2 segundos)

r_10 = np.zeros([10,len(A)]) # Matriz que almacena 10 señales

for i in range(0,10): # Bucle que crea 10 señales con ruido 
    r_10[i] = np.random.normal(0,3,len(A))

r_10_promedio = r_10.mean(axis=0) # Promedio por columna para obtener 
                                  # señal promedio

r_100 = np.zeros([100,len(A)]) # Matriz que almacena 100 señales

for i in range (0,100): # Bucle que crea 100 señales con ruido
    r_100[i] = np.random.normal(0,3,len(A))

r_100_promedio = r_100.mean(axis=0)

r_1000 = np.zeros([1000,len(A)]) # Matriz que almacena 1000 señales

for i in range (0,1000): # Bucle que crea 1000 señales con ruido
    r_1000[i] = np.random.normal(0,3,len(A))

r_1000_promedio = r_1000.mean(axis=0)
    
# =============================================================================
# Cálculo de Desvios estandar para las señales ruido promedio 
# =============================================================================

# El desvio estandar esta calculado sobre el promedio de la señal ruido,
# para el futuro calculo del SNR donde se necesitará.

de_10 = de(r_10_promedio)

de_100 = de(r_100_promedio)

de_1000 = de(r_1000_promedio)

# =============================================================================
# Suma de la señal original a las señales con ruido
# =============================================================================

cant_ruido = np.array([10,100,1000]) # Vector con cantidades de señales ruido

# Para 10 señales con ruido

s_r10 = np.zeros((cant_ruido[0],len(A))) # Matriz donde se almacenará
                                         # en cada fila, la señal original 
                                         # con ruido sumado

s_r10 = A + r_10   # Agrega a la matriz,cada señal mas su ruido

# Para 100 señales con ruido (mismo proceso)

s_r100 = np.zeros((cant_ruido[1],len(A)))

s_r100 = A + r_100
    
# Para 1000 señales con ruido (mismo proceso)

s_r1000 = np.zeros((cant_ruido[2],len(A)))

s_r1000 = A + r_1000

# Promedio de las señales + ruido ( 3 señales promedio para 10, 100 y 1000 )

s_r10_prom = s_r10.mean(axis=0)
s_r100_prom = s_r100.mean(axis=0)
s_r1000_prom = s_r1000.mean(axis=0)

# =============================================================================
# Calculo de SNR 
# =============================================================================

amp_1 = max(s_r10_prom)

snr_1 = amp_1/de_10

amp_2 = max(s_r100_prom)

snr_2 = amp_1/de_100

amp_3 = max(s_r1000_prom)

snr_3 = amp_1/de_1000

print('Relacion señal ruido para el promedio de 10 señales con ruido es',round(snr_1,3))
print('Relacion señal ruido para el promedio de 100 señales con ruido es',round(snr_2,3))
print('Relacion señal ruido para el promedio de 1000 señales con ruido es',round(snr_3,4))

# =============================================================================
# Plot
# =============================================================================

plt.figure(1)
plt.plot(s_r10_prom,'blue')
plt.plot(s_r100_prom,'red')
plt.plot(s_r1000_prom,'yellow')
plt.legend(['Señal promedio 10 ruidos','Señal promedio 100 ruidos','Señal promedio 1000 ruidos'])
plt.grid()
plt.xlabel('Muestras [n]')
plt.ylabel('Amplitud')
plt.xlim(0,(2/440)*fs) # Plot de 2 ciclos segun la señal original (LA 440)

# La relacion señal ruido respecto al ejercicio 3, mejora notablemente.
# Esto se debe a, como se ve en el gráfico, a medida que la cantidad de 
# ruidos promediados aumenta, dicha señal se vuelve "menos dispersa" o mas
# controlada y esto por ejemplo, se ve en sus picos de amplitud. Los cuales
# a medida que aumenta la cantidad de señales promediadas, dichos picos son 
# cada vez menores y por ende, la señal ruido tendrá menor energía.
