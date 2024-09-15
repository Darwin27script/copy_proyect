list_numbers_user = []

numbers_user = int(input("Intruduzca un numero en la lista: "))
list_numbers_user.append(numbers_user)

while input("Desea introducir mas numeros? (S/N): ") == "s":
    numbers_user = int(input("Intruduzca un numero en la lista: "))
    list_numbers_user.append(numbers_user)


smaller = list_numbers_user[0]
largest = list_numbers_user[0]

for n in list_numbers_user[1:]:
    if n > largest:
        largest = n
    if n < smaller:
        smaller = n

print("El numero mas pequeño es {} y el mas grande es {}". format(smaller, largest))