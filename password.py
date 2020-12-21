# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:19:27 2020

@author: Nacho
"""

class PasswordValidar():
    
    __errors = []
    
    def showErrors(self):
        for error in self.__errors:
            print (error)
        self.__errors = []
    
    def valLong(self, passw):
        if len(passw) < 8:
            self.__errors.append('Contraseña debe contener al menos 8 caracteres')
            return False
        else:
            return True

    def valMinus(self, passw):
        hayMinus = any(c.islower() for c in passw)
        if not hayMinus:
            self.__errors.append('Contraseña debe contener al menos 1 carácter en minúscula')
            return False
        else:
            return True

    def valMayus(self, passw):
        hayMayus = any(c.isupper() for c in passw)
        if not hayMayus:
            self.__errors.append('Contraseña debe contener al menos 1 carácter en mayúscula')
            return False
        else:
            return True

    def valNum(self, passw):
        hayNum = any(c.isdigit() for c in passw)
        if not hayNum:
            self.__errors.append('Contraseña debe contener al menos 1 carácter numérico')
            return False
        else:
            return True

    def valSpecial(self, passw):
        if passw.isalnum():
            self.__errors.append('Contraseña debe contener al menos 1 carácter especial')
            return False
        else:
            return True

    def valSpace(self, passw):
        if passw.count(" ") > 0:
            self.__errors.append('Contraseña no puede contener espacios en blanco')
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
    
    def validar(self,passw):
        # return self.valLong(passw) and self.valMinus(passw) and self.valMayus(passw) and self.valNum(passw) and self.valSpecial(passw) and self.valSpace(passw)
        isValLong = self.valLong(passw)
        isValMinus = self.valMinus(passw)
        isValMayus = self.valMayus(passw)
        isValNum = self.valNum(passw)
        isValSpe = self.valSpecial(passw)
        isValSpa = self.valSpace(passw)
        return isValLong and isValMinus and isValMayus and isValNum and isValSpe and isValSpa