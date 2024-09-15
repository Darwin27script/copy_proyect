import random
print("Adivina adivinador")
number = int(input("Adivina el número entre (1/10): "))
win_number = random.randint(1, 10)
if number == win_number:
    print("Ehorabuena has acertado el número")
else:
    print("No has acertado, el numero era: {}".format(win_number))
