# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:31:23 2021

@author: je_su
"""

import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError
    else:
        return math.sqrt(num1)

if __name__ == '__main__':

    op1 = int(input("Introduce un número: "))
    
    try:
        print(calculaRaiz(op1))
    except  ValueError:
        print("Ingrese valores positivos")
    
    print("Programa terminado...")