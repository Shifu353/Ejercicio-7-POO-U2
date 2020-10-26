if __name__ == "__main__":
    from Clase_Hora import Hora
    from Clase_FechaHora import FechaHora
    d = int(input("Ingrese Dia: "))

    mes = int(input("Ingrese Mes: "))

    a = int(input("Ingrese Año: "))

    h = int(input("Ingrese Hora: "))

    m = int(input("Ingrese Minutos: "))

    s = int(input("Ingrese Segundos: "))

    f = FechaHora(d,mes,a,h, m, s)

    f.Mostrar()

    #input()

    h1 = int(input("Ingrese Hora: "))

    m1 = int(input("Ingrese Minutos: "))

    s1 = int(input("Ingrese Segundos: "))

    r = Hora(h1, m1, s1)

    r.Mostrar()

    #input()
    print("Suma de f + r:")

    f2 = f + r

    f2.Mostrar()

    #input()
    print("Suma de r + f:")
    f3 = r + f

    f3.Mostrar()

    restar = int(input("Ingrese un numero para restarle el dia a f3: "))

    f4 = f3 - restar # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de

                    # días indicada por el número entero

    f4.Mostrar()
    
    sumar = int(input("Ingrese numero para sumar el dia a f2: "))
    
    f4 = 1 + f2 # suma un día a un objeto FechaHora

    f4.Mostrar()      
