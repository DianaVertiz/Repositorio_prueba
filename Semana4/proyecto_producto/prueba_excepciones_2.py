# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:15:36 2022

@author: je_su
"""
import math

def calculo_raiz(num):
    
    if not isinstance(num, (int, float)):        
        raise TypeError('Debe ingresar un valor numérico')        
    elif num < 0:
        raise ValueError('No puede ingresar un valor negativo')
    
    return math.sqrt(num)



    
