titulo = "Programa lista de la compra"
print("\t\n" + titulo + "\n" + "-" * len(titulo + "\n"))

lista = []
while True:
    articulo = input("¿Qué desea comprar? ([Q] para salir): ")
    if articulo.upper() != "Q":
        confirmacion = input("¿Seguro que quiere añadir {} a la compra? (S/N)".format(articulo))

        if confirmacion.upper() == "S":
            comprobar_si_esta = articulo in lista
            if comprobar_si_esta == True:
                print("Ya esta añadido a la lista!!".format(articulo))
            else:
                lista.append(articulo)
                print("{} añadido!".format(articulo))
        elif confirmacion.upper() == "N":
            print("Se ha cancelado añadir {}".format(articulo))
    elif articulo.upper() == "Q":
        print("La lista de compra es \n{}".format(lista))
        exit()