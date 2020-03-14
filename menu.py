#-*- coding utf8 -*-
import platform
import sys
import os
import datetime


class menu:
    """Clase que se encarga de crear y desplegar el menu del programa para el usuario"""

    def __init__(self):
        """ Inicia los valores del programa """
        self.servicio_parqueo = servicio_parqueo()
        self.option= { "1", self.agrear_auto,
                       "2", self.autos_estacionados,
                       "3", self.ticket_salida,
                       "4", self.exit
                     }

    
    def mostrar_menu():
        """Muestra todas las opciones del menu"""
        print("""
                    Opciones
                1. Agregar un vehiculo
                2. Mostrar los autos estacionados
                3. Sacar un auto
                4. Salir
        """)


    def agrear_auto(self):
        """ Agrega un auto al estacionamiento """
        placa = input("Ingrese la placa del vehiculo ")
        marca = input("Ingrese el modelo del vehiculol ")
        modelo = input("Ingrese el modelo del vehiculo ")
        tipo = input("El vehiculo es un carro (si o no)")
        if str(tipo) == str("si"):
            tipo_vehiculo="carro"
        else:
            tipo_vehiculo="moto"
        self.servicio_parqueo.agrear_auto(placa,marca,modelo, tipo_vehiculo)




    def exit(self):
        """ Cierra el programa"""
        print("Gracias por usar el sistema de parqueo")
        sys.exit()

    
    def autos_estacionados(self):
        """ Muestra todos los autos estacionados """
    
    def ticket_salida(self):
        """ 
        Se utiliza al momento de sacar un auto, esta calcula cuanto tiempo estubo el auto
        para y muestra cuanto tiene que pagar el cliente
        """


    if __name__ == "__main__":
        menu = menu()
        menu.run()
            