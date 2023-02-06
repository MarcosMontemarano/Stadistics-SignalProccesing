# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:24:14 2022

@author: marco
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Desvio_estandar import de

# =============================================================================
# Ruido aleatorio tipo Gaussiano con valor medio 0 y desv estandar 1
# =============================================================================

# Crear 6 ruidos aleatorios con 6 longitudes distintas

L = [5,10,100,1000,10000,100000]

r1 = np.random.normal(0,1,5)
r2 = np.random.normal(0,1,10)
r3 = np.random.normal(0,1,100)
r4 = np.random.normal(0,1,1000)
r5 = np.random.normal(0,1,10000)
r6 = np.random.normal(0,1,100000)

# =============================================================================
# Calcular desvio estandar a cada ruido a traves de la funcion creada anteriormente
# =============================================================================

r1_de = de(r1)
r2_de = de(r2)
r3_de = de(r3)
r4_de = de(r4)
r5_de = de(r5)
r6_de = de(r6)

Desvios_a = [r1_de,r2_de,r3_de,r4_de,r5_de,r6_de] # Vector util para ploteo resultados finales

# =============================================================================
# Diferencia porcentual entre el desvio estandar teorico y el calculado
# =============================================================================

dif_r1 = abs(1-(r1_de))*100
dif_r2 = abs(1-(r2_de))*100
dif_r3 = abs(1-(r3_de))*100
dif_r4 = abs(1-(r4_de))*100
dif_r5 = abs(1-(r5_de))*100
dif_r6 = abs(1-(r6_de))*100

Porcentajes_red = [round(dif_r1,3),round(dif_r2,3),round(dif_r3,3),
                   round(dif_r4,3),round(dif_r5,3),round(dif_r6,3)]
# Vector util para ploteo resultados finales

# =============================================================================
# Print de valores 
# =============================================================================
 
print('')
print('Resultados obtenidos:')
print('')
print('{:^6}{:^6}{:^6}{:^6}{:^6}'.format('N',' |','Sigma',' |','%'));
print('------------------------------')
for i in range(len(L)):
    print('{:^6}{:^6}{:^6}{:^6}{:^6}'.format(L[i],' |',round(Desvios_a[i],3),' |',Porcentajes_red[i]));
 