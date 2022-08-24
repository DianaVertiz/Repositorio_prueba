# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:04:06 2021

@author: je_su
"""

import unittest
from modulos.producto import Producto
from modulos.excepciones_producto import QuantityValueError, DiscountValueError, PriceValueError

class TestProducto(unittest.TestCase):
    
    def setUp(self):
        print()
        print('método setUp')
        self.producto1 = Producto('Celular', 5, 50000)
        
    def tearDown(self):
        print('metodo tearDown')
    
    def test_cantidad(self):
        print('test cantidad')
        
        self.producto1.set_cantidad(20)
        self.assertEqual( self.producto1.get_cantidad() , 20 )
        #primer método para testear el lanzamiento de la excepción
        #self.assertRaises( QuantityValueError, self.producto1.set_cantidad, -10 )
        
        #segundo método
        with self.assertRaises(QuantityValueError):
            self.producto1.set_cantidad(-10)
    
    def test_precio(self):
        print('test precio')
        
        self.producto1.set_precio(30000)
        self.assertEqual( self.producto1.get_precio() , 30000 )
        self.assertRaises(PriceValueError, self.producto1.set_precio, -50000)        
        
        
    def test_descuento(self):
        print('test descuento')
        
        self.producto1.aplicar_descuento(20)
        self.assertEqual( self.producto1.get_precio() , 40000 )
        self.assertRaises(DiscountValueError, self.producto1.aplicar_descuento, -10 )
        self.assertRaises(DiscountValueError, self.producto1.aplicar_descuento, 120 )
        
        
if __name__ == '__main__':
    unittest.main()