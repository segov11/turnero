import numeros

def preguntar():
    print("Bienvenido a la farmacia")
    
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmeticos")
        try:
            mi_categoria = input("Seleccione su categoría: ").upper()
            ["P","F","C"].index(mi_categoria)
        except ValueError:
            print("Opción invalida")
        else:
            break
    numeros.decorador(mi_categoria)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Opcion invalida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita.")
                break
inicio()            