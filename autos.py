#-*- coding utf8 -*-
#Programa autos.py
#Objetivo: Programa que controla los registros del estacionamiento de un auto o
#          moto en el estacionamiento
#Autor: Carlos Ariel Molina Marquez
#Fecha 13/marzo/2020
import datetime


class autos:
    """
    Controla el ingreso de los vehiculos al estacionamiento
    y guarda la informacion
    """

    def __init__(self, placa="", marca="", modelo="", tipo_vehiculo="", hora_ingreso="", estado=""):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo_vehiculo = tipo_vehiculo
        self.hora_ingreso = datetime.time.today()
        self.estado = True