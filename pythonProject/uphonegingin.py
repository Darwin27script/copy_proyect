titulo = "Bienvdenido, acá podrás escoger tu proximo dispositivo"
print("\n" + tittle + "\n" + "-" * len(tittle))

opcion =  str(input("Quíeres iOS o Android? Ingresa «A» para android o «I» para iOS: "))

if opcion.upper() == "A":
    opcion = str(input("Tienes dinero? (S/n): "))

    if opcion.upper() == "S":
        opcion = str(input("Te importa la camara del movil? (S/n): "))

        if opcion.upper() == "S":
            print("Google pixel SuperCam PRO")

        elif opcion.upper() == "N":
            print("Android calidad precio.")

    elif opcion.upper() == "N":
        print("Android chino 100€")

    else:
        print("Opciones validas S/n")
        exit()

elif opcion.upper() == "I":
    opcion = str(input("Tienes dinero? (S/n): "))
    if opcion.upper() == "S":
        print("iPhone Ultta Pro Max.")
    elif opcion.upper() == "N":
        print("iPhone segunda mano.")
    else:
        print("opciones validas S/N")
        exit()

else:
    print("Opciones validas «A» o «I»")
    exit()