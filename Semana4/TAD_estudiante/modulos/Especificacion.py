# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:56:59 2021

@author: je_su
"""

class Estudiante:
    
    def __init__(self, legajo, documento, nombre, promedio):
        """
        inicializa el estudiante con los datos pasador por parámetro
        legajo (int): número único positivo que identifica al estudiante en la institución
        documento (str): representa el documento de identidad del estudiante
        nombre (str): apellido y nombre del estudiante
        promedio (float): número positivo que representa el promedio del estudiante en la institución
        """

    def verNombreEstudiante(self):
        """
        devuelve un string representando el nombre del estudiante
        """
    
    def verLegajo(self):
        """
        devuelve un entero positivo que representa el legajo único del estudiante
        """
    
    def verPromedioEstudiante(self):
        """
        devuelve un float representando el promedio del estudiante
        """

    def verDocumento(self):
        """
        devuelve un string representando el Documento de identidad del estudiante
        """
    
    def modificarPromedio(self, promedio):
        """
        modifica el valor promedio del estudiante
        promedio (float): número positivo que representa el nuevo promedio del estudiante
        """
    
    def modificarLegajo(self, legajo):
        """
        modifica el legajo del estudiante
        """
    