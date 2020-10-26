class FechaHora (object):
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__ (self, dia=0,mes=0,año=0,hora=0,minutos=0,segundos=0):
        if(hora>=0 and hora<24 and minutos>-1 and minutos<60 and segundos>-1 and segundos<60 and mes>0 and mes<13):
            if((año%400==0) or (año%4==0 and año%100==0)):
                mesbisiesto = [31,29,31,30,31,30,31,30,31,30,31]
            else:
                mesbisiesto = [31,28,31,30,31,30,31,30,31,30,31]
            if dia <= mesbisiesto[mes-1] and dia>0:
                self.__dia = dia
                self.__mes = mes
                self.__año = año
                self.__hora = hora
                self.__minutos = minutos
                self.__segundos = segundos
            else:
                print("Dia fuera de Rango")
    
    def Mostrar (self):
        return print("{}/{}/{} {}:{}:{}".format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos))
    
    def __add__ (self,horas):
        dia = self.__dia
        mes = self.__mes 
        año = self.__año
        hora = self.__hora
        minutos = self.__minutos
        segundos = self.__segundos

        if((año%400==0) or (año%4==0 and año%100==0)):
            mesbisiesto = [31,29,31,30,31,30,31,30,31,30,31]
        else:
            mesbisiesto = [31,28,31,30,31,30,31,30,31,30,31]
        if type(horas) == int:
            if(horas>0):
                dia+=horas
                while(dia>mesbisiesto[mes-1]):
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        dia-=mesbisiesto[mes-1]
                        mes+=1
                return FechaHora(dia,mes,año,hora,minutos,segundos)
            else:
                print("Ingrese un numero positivo")
        else:
            hora += horas.getHora()
            minutos += horas.getMinutos()
            segundos += horas.getSegundos()
            if segundos>=60:
                if segundos == 60:
                    segundos = 0
                    minutos += 1
                else:
                    segundos -= 60
                    minutos += 1
            if minutos>=60:
                if minutos == 60:
                    minutos = 1
                    hora += 1
                else:
                    minutos -= 60
                    hora += 1
            if hora>=24:
                hora -= 24
                dia += 1
            if dia > mesbisiesto[mes-1]:
                dia -= mesbisiesto[mes-1]
                mes+=1
            if mes > 12:
                mes -= 12
                año += 1
            return(FechaHora(dia,mes,año,hora,minutos,segundos))
                
    def __radd__ (self,horas):
        dia = self.__dia
        mes = self.__mes 
        año = self.__año
        hora = self.__hora
        minutos = self.__minutos
        segundos = self.__segundos

        if((año%400==0) or (año%4==0 and año%100==0)):
            mesbisiesto = [31,29,31,30,31,30,31,30,31,30,31]
        else:
            mesbisiesto = [31,28,31,30,31,30,31,30,31,30,31]
        if type(horas) == int:
            if(horas>0):
                dia+=horas
                while(dia>mesbisiesto[mes-1]):
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        dia-=mesbisiesto[mes-1]
                        mes+=1
                return FechaHora(dia,mes,año,hora,minutos,segundos)
            else:
                print("Ingrese un numero positivo")
        else:
            hora += horas.getHora()
            minutos += horas.getMinutos()
            segundos += horas.getSegundos()
            if segundos>=60:
                if segundos == 60:
                    segundos = 0
                    minutos += 1
                else:
                    segundos -= 60
                    minutos += 1
            if minutos>=60:
                if minutos == 60:
                    minutos = 1
                    hora += 1
                else:
                    minutos -= 60
                    hora += 1
            if hora>=24:
                hora -= 24
                dia += 1
            if dia > mesbisiesto[mes-1]:
                dia -= mesbisiesto[mes-1]
                mes+=1
            if mes > 12:
                mes -= 12
                año += 1
            return(FechaHora(dia,mes,año,hora,minutos,segundos))
    
    def __sub__ (self,resta):
        if((self.__año%400==0) or (self.__año%4==0 and self.__año%100==0)):
            mesbisiesto = [31,29,31,30,31,30,31,30,31,30,31]
        else:
            mesbisiesto = [31,28,31,30,31,30,31,30,31,30,31]
        
        if type(resta)!=float and resta>0:
            dia = self.__dia
            mes = self.__mes
            año = self.__año
            dia = dia - resta
            while dia<1:
                if(mes==0):
                    dia+=31
                    mes=12
                    año+=1
                else:
                    dia=mesbisiesto[mes-2]
                    #dia-=1 #BORRAAR
                    mes-=1
            return (FechaHora(dia,mes,año,self.__hora,self.__minutos,self.__segundos))
        else:
            print("Usted ingrese un numero real o 0")
