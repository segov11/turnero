def num_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

def num_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"

def num_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

p = num_perfumeria()
f = num_farmacia()
c = num_cosmetica()

def decorador(categoria):
    print("\n" + " *" * 23)
    print("Su turno es: ")
    if categoria == "P":
        print(next(p))
    elif categoria == "F":
        print(next(f))
    else:
        print(next(c))
    print("Pronto será atendido")
    print("*" * 23 + "\n")
    