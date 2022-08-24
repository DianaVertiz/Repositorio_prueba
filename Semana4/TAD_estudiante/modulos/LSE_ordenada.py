# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:20:29 2021

@author: je_su
"""

class Nodo:
    
    def __init__(self, dato=None):
        self.__dato = dato
        self.__siguiente = None
        
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
                
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def __str__(self):
        return f'{self.__dato}'

class LSE_ordenada:
    
    def __init__(self):
        self.__cabeza = None
    
    def __iter__(self):
        #make SLL iterable
        nodo = self.__cabeza
        while nodo:
            yield nodo
            nodo = nodo.getSiguiente()        
        
    def esta_vacia(self):
        return self.__cabeza is None
        
    def tamano(self):
        """
        devuelve el número de ítems de la lista
        """
        nodo_temp = self.__cabeza
        contador = 0
        while nodo_temp:
            contador += 1
            nodo_temp = nodo_temp.getSiguiente()
            
        return contador      
        
    def agregar(self, item):
        """
        agrega un nuevo ítem a la lista, asegurando que el orden se preserve.
        item: ítem a agregar.
        ------------------
        pre: se asume que el ítem aún no está en la lista.
        pos: modifica la lista con el ítem agregado      
        
        """
        nodo_actual = self.__cabeza
        nodo_anterior = None
        detenerse = False
        
        while nodo_actual and not detenerse:
            if nodo_actual.getDato() > item:
                detenerse = True
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente() 
        
        nodo_temp = Nodo(item)
        if nodo_anterior == None:
            nodo_temp.setSiguiente(nodo_actual)
            self.__cabeza = nodo_temp
        else:
            nodo_temp.setSiguiente(nodo_actual)
            nodo_anterior.setSiguiente(nodo_temp)          
    
    
   
    def buscar(self, item):
        """
         busca el ítem en la lista
         item: ítem a buscar
         return: booleano, True si es encontrado sino False
        """  
        encontrado = False
        nodo_actual = self.__cabeza
        detenerse = False
        while nodo_actual and not encontrado and not detenerse:
            if nodo_actual.getDato() == item:
                encontrado = True
            else:
                if nodo_actual.getDato() > item:
                    detenerse = True
                else:
                    nodo_actual = nodo_actual.getSiguiente()
        
        return encontrado
    
    def remover(self, item):
        """
        elimina el ítem de la lista. 
        item: ítem a remover.
        ------------------
        pre: se asume que el ítem está presente en la lista.
        pos: se modifica la lista eliminando el ítem 
        """
        encontrado = False
        nodo_actual = self.__cabeza
        nodo_anterior = None
        
        while not encontrado:
            if nodo_actual.getDato() == item:
                encontrado = True
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
        
        if nodo_anterior == None:
            self.__cabeza = nodo_actual.getSiguiente()
        else:
            nodo_anterior.setSiguiente(nodo_actual.getSiguiente())
       
    def extraer_al_final(self):
        """
        elimina y devuelve el último ítem de la lista. 
        pre: asume que la lista tiene al menos un ítem.
        pos: se modifica la lista y se devuelve el valor eliminado
        """
        nodo_temp = self.__cabeza
        nodo_anterior = None
        
        while nodo_temp.getSiguiente():
            nodo_anterior = nodo_temp
            nodo_temp = nodo_temp.getSiguiente()
        # la lista tiene un solo elemento
        if nodo_anterior == None:
            self.__cabeza = None
        else:
            nodo_anterior.setSiguiente(None)
            
        return nodo_temp         
                
        
    def extraer(self, posicion=-1):
        """
        elimina y devuelve el ítem en la "posición"
        si no se indica el parámetro posición o este es -1, 
        se elimina y devuelve el último elemento de la lista
        pre: se asume que el ítem está presente en la lista.
        pos: modifica la lista y devuelve el ítem eliminado
        """
        nodo_eliminado = None
        nodo_actual = self.__cabeza
        eliminado = False
        if posicion < -1 or posicion >= self.tamano():
            raise Exception("posición no válida para extraer")    
        
        if posicion == -1:
            return self.extraer_al_final()
        else:
            if posicion == 0:
                nodo_eliminado = nodo_actual
                self.__cabeza = nodo_actual.getSiguiente()
                return nodo_eliminado
            else:
                nodo_anterior = self.__cabeza
                indice = 0
                
                while nodo_anterior and not eliminado:
                    if indice == posicion -1:
                        nodo_eliminado = nodo_anterior.getSiguiente()
                        nodo_siguiente = nodo_eliminado.getSiguiente()
                        nodo_anterior.setSiguiente(nodo_siguiente)
                        eliminado = True
                    else:
                        nodo_anterior = nodo_anterior.getSiguiente()
                        indice += 1
                
                return nodo_eliminado
                      
        
    
    def indice(self, item):
        """
        devuelve el índice correspondiente al ítem en la lista
        ----------------
        pre: asume que el ítem está presente en la lista
        pos: retorna la posición del ítem en la lista
        """
            
                        
            