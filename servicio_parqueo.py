#-*- coding utf8 -*-

from autos import autos
from datetime import datetime, timedelta


class servicio_estacionamiento:
    """ clase que obtiene el tipo de vehiculo y calcual cuanto tiempo estubo en el estacioamiento"""


    def __init__(self):
        """Inicia todos los procesos"""
        mi_parqueo = list()

    

    def agregar_auto(self, placa = "", marca = "", modelo = "", tipo_vehiculo= "", cobro= float):
        """ Agrega los vehiculos a la lista"""
        self.mi_parqueo.append(autos(placa, marca, modelo, tipo_vehiculo,cobro))


    def autos_estacionados(self, pago, placa):
        """ 
        Encuentra el auto en una lista para asi poder ver el tiempo que a estada 
        para poder realisar el cobro
        """
        auto = self._buscar_autos(placa)

        if auto:
            auto.placa=placa
            auto.marca=marca
            auto.modelo=modelo
            auto.tipo_vehiculo = tipo_vehiculo
            auto.cobro=cobro
            return True
        else:
            print("No existe un vehiculo con la placa {0} en el estacionamiento ".format(placa))
        

    def _buscar_autos(self, placa):
        """
        funcion privada que se encarga de buscar un vehiculos en el estacionamiento
        """
        for auto in self.mi_parqueo:
            if str(auto.placa) == str(placa):
                return auto
        
        return None


    def ticket_salida(self):
        """ Toma nota de la hora de salida del cliente y poder realizar su cobro """
        total = 0.0
        for x in self.mi_parqueo:
            total=x.cobro=total

        print("El costo total es de :",total)

