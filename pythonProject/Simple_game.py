titulo = "The last life"
print("\n\t" + titulo + "\n\t" + "-" * len(titulo) + "\n")

opcion = str(input("Ya ha pasado... La explosión nuclear lo ha arrasado todo...\n"
        "Te has despertado con una contusión en la cabeza y visión borrosa.\n"
        "Es de noche, pero alcanzas a ver una gasolinera con poca luz y una fogata en la cima de una colina cercana.\n"
        "¿Qué decides hacer?\n"
        "A. Ir a la fogata.\n"
        "B. Ir a la gasolinera.\n"))

if opcion.upper() == "A":
    print("No pudiste llegar a la colina "
          "el cansancio y la contusión te impidió continuar.\nMoriste al caer mientras subías.")
    exit()
elif opcion.upper() == "B":
    opcion = str(input("Te levantas sin fuerzas, pero logras llegar a la gasolinera agotado. "
                       "Encuentras medicina para curarte también encuentras una escopeta sin balas.\n"
                       "¿Quieres quedarte la escopeta sin balas?\n"
                       "A. Quedarte la escopeta.\n"
                       "B. Dejar la escopeta.\n"))

    if opcion.upper() == "A": # Se guarda la escopetas
        escopeta = True
    elif opcion.upper() == "B": # deja la escopeta
        escopeta = False
    else:
        print("opcion no valida;")
        exit()
else:
    print("opcion no valida;")
    exit()

opcion = str(input(("Estas solo y sin comida. ¿Debes de buscar alimento que decides hacer?\n"
                    "A. ¿Investigar la fogata de ayer?\n"
                    "B. Tomar camino por carretera e investigar la zona.\n")))

if opcion.upper() == "A":
    opcion = str(input("Sales de la gasolinera y, tras el esfuerzo, ha valido la pena llegaste a la fogata.\n"
                       "¡ehorabuena encuentras comida!\n"
                       "Miras a lo largo y ves personas acercándose, pero no sabes si son de fiar."
                       "Que harás?\n"
                       "A. Esperar a esas personas.\n"
                       "B. Huir con raciones.\n"))
    if opcion.upper() == "B":
        print("has intentando huir con las raciones... te han disparado a la distancia.")
        exit()

    elif opcion.upper() == "A" and escopeta:
        opcion = str(input("¡Confiar a veces es bueno! Son otros supervivientes;\n"
                           "Te cuentan que hay saqueadores de comida que matan a quienes ven,\n"
                           "que ellos no pueden ayudarte de ninguna manera;\nsin embargo,"
                           " te dan 8 balas de munición de escopeta y la ruta a una base militar."
                           "¿Qué decides hacer?\n"
                           "A. No hacer nada.\n"
                           "B. Ir a la base militar.\n"))
        if opcion.upper() == "A":
            print("No has hecho nada has muerto...")
            exit()

        if opcion.upper() == "B":
            opcion = str(input("Te aventuras con la ruta hacia la base militar por medio del alcantarillado\n"
                                "de la ciudad; al parecer es lo suficientemente grande para avanzar y es más\n"
                                "seguro que la superficie. Hay mucho lunático actualmente… Cuando pensabas que\n"
                                "estabas cerca de llegar, te encuentras un hombre mutado por la radiación.\n"
                                "¿Tienes que defenderte, qué harás?\n"
                                "A. Correr.\n"
                                "B. Usar las 8 balas.\n"))
            if opcion.upper() == "A":
                print("Has intentado correr, pero el mutante era más rápido que tú, decansa en paz.")
                exit()

            elif opcion.upper() == "B":
                print("Has atacado al mutante aprovechando cada bala; con suerte lograste neutralizarlo,"
                      " perdiste la escopeta, pero no importó.\n"
                      "Más adelante lograste llegar a la base militar y fuiste rescatado.\n"
                      "Felicidades y gracias por jugar!!!")
            else:
                print("Opcion no valida;")
                exit()


    elif opcion.upper() == "A" and escopeta == False:
        print("Eran supervivientes, sin embargo, al verte desarmado,"
              " desconfiaron de ti pensando que era una táctica de saqueadores para robarles.\n"
              "Te han asesinado.")
        exit()
    else:
        print("Opcion no valida;")
        exit()

elif opcion.upper() == "B":
    print("Has elegido la carretera… los saqueadores te han visto a distancia y te han disparado.\n"
          "Te han matado...")
    exit()
else:
    print("Opcion no valida;")
    exit()