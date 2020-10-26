class Hora (object):
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__ (self,hora,minutos,segundos):
        if hora>-1 and hora<24 and minutos>-1 and minutos<60 and segundos>-1 and segundos<60:
            self.__hora = hora
            self.__minutos = minutos
            self.__segundos = segundos
        else:
            print("Ingrese hora en el rango [0,23] minutos en el rango [0,59] y minutos en el rango [1,59]")
    
    def Mostrar (self):
        return print("{}:{}:{}".format(self.__hora,self.__minutos,self.__segundos))

    def getHora (self):
        return self.__hora

    def getMinutos (self):
        return self.__minutos
        
    def getSegundos (self):
        return self.__segundos
