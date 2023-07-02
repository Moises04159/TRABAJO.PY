def verificar_dia(dia):
    dia:str=input("Ingrese que dia es hoy: ")
    match dia:
        case "Lunes":
            print("Hoy es lunes")
        case "Martes":
            print("Hoy es martes")
        case "Miércoles":
            print("Hoy es miércoles")
        case _:
            print("Hoy es otro día")

verificar_dia("Miércoles")

