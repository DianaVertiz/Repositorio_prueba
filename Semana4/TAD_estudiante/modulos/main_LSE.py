# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:00:45 2021

@author: je_su
"""

from modulos.Estudiante import Estudiante
from modulos.LSE import ListaSimpleEnlazada

def leer_archivo(nombre_archivo):
    
    with open(nombre_archivo, mode='r') as file:
        contenido = file.readlines()
        
    return contenido


def main():
    pass

    


if __name__ == '__main__':
    main()