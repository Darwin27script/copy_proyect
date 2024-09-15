numero = int(input("Numero a multiplicar: "))

for contador in range(1, 11):

    if contador % 2 == 0:
        print("{} x {} = {}".format(numero, contador, contador * numero))