print("Cajero automatico")
saldo = 1000
salir = False
while not salir:
    print('''opciones que puedes realizar
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir''')
    opcion = int(input("Elije una opcion: "))

    if opcion == 1:
        print(f"tu saldo es: {saldo} \n")
    elif opcion == 2:
        retirar = int(input("Dijita el el monto a retirar: "))
        if retirar <= saldo:
            saldo -= retirar
            print(f"tu nuevo saldo es: {saldo} \n")
        else:
            print("no cuentas con el saldo suficiente ")
    elif opcion == 3:
        depositar = int(input("Dijita el el monto a depositar: "))
        saldo += depositar
        print(f"tu saldo es: {saldo} \n")
    elif opcion == 4:
        print(f"Hasta luego")
        salir = True
    else:
        print(f"Opcion invalida")
