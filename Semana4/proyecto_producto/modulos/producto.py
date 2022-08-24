# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:47:45 2021

@author: je_su
"""

# Modelar un "producto" que tenga como atributos su nombre, cantidad y precio.
# Estos atributos deben definir en la creación del objeto.
# La clase producto tendrá funcionalidades para modificar y devolver su cantidad y precio,
# tendrá además, una función para aplicar un descuento al precio a partir de un valor porcentual 
# Implementar adicionalmente una función para mostrar la información del objeto por consola.

from modulos.excepciones_producto import QuantityValueError, DiscountValueError, PriceValueError

class Producto:
    """Clase que representa un producto
   
    Atributos
    ----------
    nombre : str
        nombre de producto
    cantidad : int
        número de productos en stock
    precio : float
        precio del producto.
            
    """      
    def __init__(self, nombre:str, cantidad:int, precio:float):
        """Constructor de la clase producto  """
      
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        
    def set_cantidad(self, cantidad):
        """
        Función para setear la cantidad de producto

        Parameters
        ----------
        cantidad : int
            valor entero que representa la cantidad de producto.

        Raises
        ------
        QuantityValueError
            Se implementa un error en caso se ingresen cantidades negativas.

        """        
        if cantidad < 0:
            raise QuantityValueError
        else:
            self.__cantidad = cantidad
        
    def set_precio(self, precio):
        """
        Función para setear precio de producto        
        
        precio : valor flotante que representa el precio
        
        PriceValueError: excepción lanzada al ingresar valores negativos del precio
        """
        if precio < 0:
            raise PriceValueError
        else:
            self.__precio = precio
        
    def get_cantidad(self):
        """
        Función que retorna la  cantidad del producto
        """
        return self.__cantidad
    
    def get_precio(self):
        """
        Función que retorna el precio del producto
        """
        return self.__precio
    
    def aplicar_descuento(self, descuento:int):
        """
        Función que aplica un descuento al precio del producto
        
        descuento : valor entero expresado en porcentaje entre 0 y 100
        
        DiscountValueError: excepción lanzada al ingresar valores de descuento negativos o mayores a 100
        """
        if 0<= descuento <= 100:
            self.__precio = self.__precio * ( 1.0 - float(descuento/100) )
        else:
            raise DiscountValueError(descuento)
        
    def __str__(self):
        """Función para mostrar la información de producto como string"""
        
        return f'{self.__nombre}, cantidad: {self.__cantidad}, precio: {self.__precio:.2f}'
    
    

if __name__ == '__main__':
    
    producto1 = Producto('Celular', 5, 50000)
    
    print(producto1)
    
    entrada1 = int(input("Ingrese una cantidad del producto:")) 
    
    try:                
        producto1.set_cantidad(entrada1)        
        print(producto1) 
        
    except QuantityValueError:
        print("La cantidad de producto no puede ser negativa")  
        
           
    entrada2 = int(input("Ingrese un porcentaje:")) 
    
    try:
        producto1.aplicar_descuento(entrada2)    
    except DiscountValueError as msg:
        print(msg)
        
    print(producto1)
    
    
    
    
    
    
    
    
    
    