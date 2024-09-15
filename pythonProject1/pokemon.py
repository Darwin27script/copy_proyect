from random import randint
from os import system

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

distancia_de_barra = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # se pelean los pokemon

    # turno de pikachu
    turno_pikachu = "Turno de pikachu"
    print("\t\n" + "-" * len(turno_pikachu) + turno_pikachu + "-" * len(turno_pikachu) + "\n")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola Voltio
        print("Pikachu ataca con Bola Voltio.\n")
        vida_squirtle -= 10

    else:
        # Onda Trueno
        print("Pikachu ataca con Onda Trueno\n")
        vida_squirtle -= 11

    if vida_pikachu <= 0:
        vida_pikachu = 0
    if vida_squirtle <= 0:
        vida_squirtle = 0

    # Barra de vida pikachu
    barras_de_vida_pikachu = int((vida_pikachu * distancia_de_barra) / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu,
                                              "-" * (distancia_de_barra - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    # Barra de vida Squirtle
    barras_de_vida_squirtle = int((vida_squirtle * distancia_de_barra) / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle,
                                              "-" * (distancia_de_barra - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    # Pausa estetica
    input("Presione Enter para continuar...")

    # clear
    system("cls")

    # turno de squirtle
    turno_squirtle = "Turno de Squirtle"
    print("\t\n" + "-" * len(turno_squirtle) + turno_squirtle + "-" * len(turno_squirtle) + "\n")

    ataque_squirtle = ""
    opciones = ["P", "A", "B", "N"]
    while ataque_squirtle.upper() not in opciones:
        ataque_squirtle = input("¿Qué ataque vas a realizar []? \n[P]lacaje.\nPistola de [A]gua.\n[B]urbuja."
                                "\n[N]o hacer nada\n")

    if ataque_squirtle.upper() == "P":
        # Squirtle ataca con placaje
        print("Squirtle ataca con Placaje\n")
        vida_pikachu -= 10

    elif ataque_squirtle.upper() == "A":
        # Squirtle ataca con pistola de agua
        print("Squirtle ataca con Pistola Agua\n")
        vida_pikachu -= 12

    elif ataque_squirtle.upper() == "B":
        # squirtle ataca con Burbuja
        print("Squirtle ataca con Burbuja.\n")
        vida_pikachu -= 9

    elif ataque_squirtle.upper() == "N":
        # No hacer nada
        print("Squirtle no hace nada\n")

    if vida_pikachu <= 0:
        vida_pikachu = 0
    if vida_squirtle <= 0:
        vida_squirtle = 0

    # Barra de vida pikachu
    barras_de_vida_pikachu = int((vida_pikachu * distancia_de_barra) / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu,
                                              "-" * (distancia_de_barra - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    # Barra de vida Squirtle
    barras_de_vida_squirtle = int((vida_squirtle * distancia_de_barra) / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle,
                                              "-" * (distancia_de_barra - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    # Pausa estetica
    input("Presione Enter para continuar...")

    # clear
    system("cls")

# Dictar ganador!!
if vida_pikachu <= 0:
    print("\nSquirtle gana el combate!!")
elif vida_squirtle <= 0:
    print("\nPikachu gana el combate!!")