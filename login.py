# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:04:41 2020

@author: Nacho
"""

import usuario  as uv
import password as pv

user_validator = uv.UsuarioValidar()
pass_validator = pv.PasswordValidar()

correcto = False

while not correcto:
    if not user_validator.validar(input('Escriba su nombre de usuario: ')):
        user_validator.showErrors()
    else:
        correcto = True
        
correcto = False
            
while not correcto:        
    if not pass_validator.validar(input('Escriba su contraseña: ')):
        pass_validator.showErrors()
    else:
        correcto = True
        
print("\n¡Validación correcta!")