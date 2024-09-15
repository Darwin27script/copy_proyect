titulo = "Bienvenido, te gusta el queso?"
print("\n" + titulo + "\n" + "-" * len(titulo))

puntuacion = 0

opcion = str(input("Que haces cuando miras una tabla de quesos?\n"
                   "A. No puedo tenerla cerca salgo corriendo.\n"
                   "B. Me acerco a probarla.\n"
                   "C. Devoro todo queso a mi paso.\n"
                   "Ingrese una opción: "))


if opcion.upper() == "A":
    puntuacion += 0

elif opcion.upper() == "B":
    puntuacion += 5

elif opcion.upper() == "C":
    puntuacion += 10
else:
    print("las opciones son A B y C")
    exit()

opcion = str(input("Como te gusta la hamburgesa?\n"
                   "A. Sin Queso\n"
                   "B. Con queso\n"
                   "C. Solo con queso\n"
                   "Ingrese una opcion: "))

if opcion.upper() == "A":
    puntuacion += 0

elif opcion.upper() == "B":
    puntuacion += 5

elif opcion.upper() == "C":
    puntuacion += 10
else:
    print("las opciones son A B y C")
    exit()

opcion = str(input("Eres intorelante a la lactosa?\n"
                   "Si.\n"
                   "A veces.\n"
                   "No.\n"
                   "Ingrese una opcion: "))

if opcion.upper() == "A":
    puntuacion += 0

elif opcion.upper() == "B":
    puntuacion += 5

elif opcion.upper() == "C":
    puntuacion += 10
else:
    print("las opciones son A B y C")
    exit()


if puntuacion >= 25:
    print("Puntuacion: {}\n"
          "Felicidades, Eres el devorador de quesos. ".format(puntuacion))
elif puntuacion >= 15:
    print("Puntuacion: {}\n"
          "Felicidades, Eres   una persona que le gusta el queso.".format(puntuacion))
else:
    print("Puntuacion: {}\n"
          "felicidades, No te gusta el  queso.".format(puntuacion))

