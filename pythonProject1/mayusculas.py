import string

texto = input("Introduza un texto: ")
letras_mayusculas = 0

for letra in texto:
    if letra in string.ascii_uppercase:
       letras_mayusculas += 1

print("hay {} letras mayusculas en el texto".format(letras_mayusculas))