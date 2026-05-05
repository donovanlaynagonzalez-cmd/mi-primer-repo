dia = int(input("escribe el numero de el dia de la semana "))
if dia > 3:
    print("dia no valido")
match dia:
    case 1:
        print("hoy es lunes")
    case 2:
        print("hoy es martes")
    case 3:
        print("hoy es miercoles")