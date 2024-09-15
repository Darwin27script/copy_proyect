# ejemplo
texto_usuario = input("Introduzca el texto: ")

# Variables
espacios = 0
puntos = 0
comas = 0

for contador in texto_usuario:
    if contador == " ":
        espacios += 1
    elif contador == ".":
            puntos += 1
    elif contador == ",":
        comas += 1

print("Espacios = {}\nPuntos = {}\nComas = {}".format(espacios, puntos, comas))