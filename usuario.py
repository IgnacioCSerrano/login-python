# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:00:53 2020

@author: Nacho
"""

class UsuarioValidar():
    
    __errors = []
    
    def showErrors(self):
        for error in self.__errors:
            print (error)
        self.__errors = []
    
    def valLong(self, username):
        if len(username) < 6:
            self.__errors.append('Nombre de usuario debe contener al menos 6 caracteres')
            return False
        elif len(username) > 12:
            self.__errors.append('Nombre de usuario no debe sobrepasar 12 caracteres')
            return False
        else:
            return True
        
    def valAlfanum(self, username):
        if not username.isalnum():
            self.__errors.append('Nombre de usuario debe contener solo letras y números')
            return False
        else:
            return True
        
    # Es importante almacenar primero el resultado de cada función en variables
    # separadas y retornar la composición AND de estas en lugar de retornar 
    # la composición AND de las funciones directamente porque de esta manera
    # se construye el array errors[] con todos los errores que haya para cada 
    # validación en lugar de agregarse solo el primero que retorne FALSE 
    # (operador AND deja de evaluar sentencias a partir del primer valor 
    # falso detectado)
        
    def validar(self, username):
        # return self.valLong(username) and self.valAlfanum(username)
        isValLong = self.valLong(username)
        isValAlfanum = self.valAlfanum(username)
        return isValLong and isValAlfanum
