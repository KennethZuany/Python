from funciones import *

# Programa
while opcion != "4" :
    mostrar_menu ( )
    opcion = input ( "Seleccione una opción: " )

    if opcion == "1" :
        agregar_contacto ( agenda )
    elif opcion == "2" :
        mostrar_contactos ( agenda )
    elif opcion == "3" :
        buscar_contacto ( agenda )
    elif opcion == "4" :
        salir ( )
    else:
        print ( "Opción inválida, intente de nuevo." )