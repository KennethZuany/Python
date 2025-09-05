from funciones import *

# Programa
while opcion != "4" :
    mostrar_menu ( )
    opcion = input ( "\n \nSeleccione una opción: " )

    if opcion == "1" :
        resultado = area_cuadrado ( )
        print ( "El área del cuadrado es:" , resultado )
    elif opcion == "2" :
        resultado = area_rectangulo ( )
        print ( "El área del rectángulo es:" , resultado )
    elif opcion == "3" :
        resultado = area_circulo ( )
        print ( "El área del círculo es:" , resultado )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "Opción invalida, intente de nuevo." )