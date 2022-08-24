# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:32:41 2021

@author: je_su
"""

from modulos.Estudiante import Estudiante
from modulos.LSE_ordenada import LSE_ordenada

def leer_archivo(nombre_archivo):
    
    with open(nombre_archivo, mode='r') as file:
        contenido = file.readlines()
        
    return contenido


def main():
    pass


if __name__ == '__main__':
    main()