saldo = 1500
intentos = 0
clave_correcta = "1234"

print("Bienvenido al cajero automático")
clave = input("Ingrese su clave: ")

while clave != clave_correcta and intentos < 3:
    print("Clave incorrecta. Intente de nuevo.")
    intentos += 1
    clave = input("Ingrese su clave: ")

if intentos == 3:
    print("Tarjeta bloqueada.")
else:
    print("Acceso concedido.")
    opcion = 0
    while opcion != 3:
        print("\nMenú:")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Saldo actual:", saldo)
        elif opcion == 2:
            retiro = int(input("Ingrese monto a retirar: "))
            if retiro <= saldo:
                saldo -= retiro
                print("Retiro exitoso. Saldo restante:", saldo)
            else:
                print("Saldo insuficiente.")
        elif opcion == 3:
            print("Gracias por usar el cajero.")
        else:
            print("Opción inválida.")