# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:37:33 2021

@author: je_su
"""

class QuantityValueError(Exception):
    """Error al ingresar cantidades negativas de productos"""
    
class PriceValueError(Exception):
    """Error al ingresar precios con valores negativos"""
    
class DiscountValueError(Exception):
    """Error al ingresar descuento"""
    
    msg = "El descuento no está en el rango (0 , 100) aceptable"
    
    def __init__(self, descuento, mensaje = msg):
        self.descuento = descuento
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
    def __str__(self):
        return f'{self.descuento} -> {self.mensaje}'
        