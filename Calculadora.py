print("Calculadora")

n1 = n2 = 0
salir = False
while not salir:
    print('''operaciones que puedes realizar
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir''')
    opcion = int(input("Elije una opcion: "))
    if 1 >= opcion <= 4:
        n1 = float(input("Introduce un numero: "))
        n2 = float(input("Introduce otro numero: "))
    if opcion == 1:
        suma = n1 + n2
        print(f"Resultado de la suma: {suma:.2f} \n")
    elif opcion == 2:
        resta = n1 - n2
        print(f"Resultado de la resta: {resta:.2f} \n")
    elif opcion == 3:
        multiplicacion = n1 * n2
        print(f"Resultado de la multiplicacion: {multiplicacion:.2f} \n")
    elif opcion == 4:
        division = n1 / n2
        print(f"Resultado de la division: {division:.2f} \n")
    elif opcion == 5:
        print("Saliendo ... \n")
        salir = True
    else:
        print(f"Opcion invalida")
