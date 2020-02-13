# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:06:56 2020

@author: booed_000
"""
print('Tarea 2_Practica02')
class User():

    def __init__(self, first_name, last_name, username, correo, localidad):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.correo = correo
        self.localidad = localidad.title()

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Correo: " + self.correo)
        print("  Localidad: " + self.localidad)

    def greet_user(self):
        print("Hola de nuevo, " + self.username + "!")
        
    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts = h

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
        
    def secure_account(self):
        self.login_attempts = z + h
        
h=input()
Goku = User('Goku', 'Son', 'kakaroto', 'Goku@programacion.com', 'miravalle')
Goku.describe_user()
Goku.greet_user()

print("Numero de intentos")
Goku.increment_login_attempts()

print("  Numero de intentos: " + str(Goku.login_attempts))

print("Reseteando el numero de intentos...")

Goku.reset_login_attempts()
print("  Numero de intentos: " + str(Goku.login_attempts))

z=input()
Goku.secure_account()
print("  Se paso del limite de inicio:  " + str(Goku.login_attempts) +  "  Intentos, Error, intente en 2hr")
    