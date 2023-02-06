# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:53:04 2022

@author: marco
"""

# =============================================================================
#  Tiempo de ejecución de las funciones del Filtro de media movil #
# =============================================================================

import numpy as np
from timeit import default_timer    # Importa la funcion que permite calcular
                                    # tiempo de ejecución 
from Mediamovild import mediamovild
from Mediamovilr import mediamovildr

# =============================================================================
# Señal "test" para calcular tiempo de ejecucion
# =============================================================================

def tiempo_ej(x,M):
    # x = np.array([0,1,2,3,4,5,6,7,8,9,10])   # Valores utilizado como señal
    # M = 5                                    # ancho de la ventana
    
    inicio_1 = default_timer()
    a = mediamovild(x,M)
    fin_1 = default_timer()
    Tiempo_1 = fin_1-inicio_1
    Tiempo_1 = round(Tiempo_1,6)
    
    inicio_2 = default_timer()
    b = mediamovildr(x,M)
    fin_2 = default_timer()
    Tiempo_2 = fin_2-inicio_2
    Tiempo_2 = round(Tiempo_2,6)

# if __name__  == '__main__':
# =============================================================================
# Ploteo de informacion
# =============================================================================

        # print (" ")
        
        # print ("El tiempo de ejecución del filtro de Media Movil es de ", Tiempo_1," seg.")
        

        
        
        # print (" ")
        
        # print("El tiempo de ejecución del Filtro de Media Movil Recursivo es de ", Tiempo_2," seg.")