# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:38:30 2022

@author: je_su
"""

def dividir(num1, num2):
    return num1/num2


if __name__ == '__main__':
    
    resultado = 0
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = (dividir(num1 , num2))
    
    except ZeroDivisionError:
        print("No puede dividir por 0")
        
    except ValueError:
        print("Ingrese solo valores numéricos")
        
    else:
        print("Se realiza la división con éxito")
        print(resultado)
        
    finally:
        print("Esto se ejecuta siempre!!!")
    
    print()
    print("Continúa el resto del programa")
    print("...................")