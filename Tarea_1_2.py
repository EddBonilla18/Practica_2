# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:08:02 2020

@author: booed_000
"""

print('Tarea 2, Practica_02')
class Restaurant():

    def __init__(self, nombre, tipo_Restaurante):
        self.nombre = nombre.title()
        self.tipo_Restaurante = tipo_Restaurante

    def describe_restaurant(self):
        msg = self.nombre + " el mejor servicio de " + self.tipo_Restaurante + "."
        print(msg)

    def open_restaurant(self):
        msg = self.nombre + " abierto ahora, adelante!"
        print(msg)
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('El Perro loco', 'Tacos')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served = 0
print("Servicio de " + str(restaurant.set_number_served) + "_Clientes")
restaurant.set_number_served = 430

print("Servicio de " + str(restaurant.set_number_served) + "_Clientes")
restaurant.set_number_served = 1257
print("Servicio de " + str(restaurant.set_number_served) + "_Clientes")

print('Introduzca nuevo valor de numero de servicio')
b=input()
restaurant.increment_number_served = restaurant.set_number_served + b
print("Servicio de " + str(restaurant.increment_number_served) + "_Clientes")
