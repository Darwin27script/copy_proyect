
# Enter numbers
print("Bienvenido\n")
print("Introduzca tres números enteros y se le dirá cuál de ellos es el más pequeño y el más grande.\n")
numberOne = int(input("Ingrese el primer numero: "))
numberTwo = int(input("Ingrese el segundo numero: "))
numberThree = int(input("Ingrese el tercer numero: "))
print("El número más grande es: {}".format(max(numberOne, numberTwo, numberThree)))
print("El número más pequeño es: {}".format(min(numberOne, numberTwo, numberThree)))