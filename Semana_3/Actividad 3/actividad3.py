# Menú
def mostrar_menu( ) :
    print ( "\n- - - Menú de la Calculadora - - -" )
    print ( "1. Agregar dispositivo." )
    print ( "2. Buscar gasto de un dispositivo." )
    print ( "3. Consumo de todos los dispositivos." )
    print ( "4. Salir" )

# Agregar dispositivo
def agregar_dispositivo ( dispositivos ) :
    print ( "\n- - - Agregar dispositivo - - -" )
    dispositivo = input ( "Nombre del dispositivo: " )
    consumo = input ( "Consumo del dispositivo (W): " )
    uso = input ( "Uso diario (H): " )
    dispositivos.append ( [dispositivo , consumo , uso ] )
    print ( "\n- - - Dispositivo agregado exitosamente - - - " )


# Gasto de un dispositivo
def gasto_dispositivo ( dispositivos ) :
   print ( " \n- - - Buscar gasto de un dispositivo - - - ")
   dispositivo = input ( "Nombre del dispositivo a buscar: " )
   # No recuerdo como buscar en la lista con los booleanos.
   else : 
    print ( "\n - - - Dispositivo no encontrado - - - \n")

# Consumo de todos los dispositivos 
def consumo_total ( lista ) :
    print ( "\n- - - Consumo de todos los dispositivos - - - \n" )  
    for dispositivo in lista :
        print ( "Dispositivo:" , dispositivo [ 0 ] , "| Consumo (W):" , dispositivo [ 1 ] , "| Uso (H):" , dispositivo [ 2 ] )
        consumo_total = [ int ( dispositivo [ 1 ] ) * int ( dispositivo [ 2 ] ) ]
    print ( "El consumo total de todos los dispositivos es:" , consumo_total, "Wh" )
# No se como sacar todos los consumos totales de dispositivos y luego sumarlos uno a uno

# Salir
def salir ( ) :
    print ( "\n \n- - - Gracias por usar la calculadora. ¡Hasta luego!- - - \n \n " )

# Variable y lista
lista = [ ]
opcion = ""

# Programa
while opcion != "4" :
    mostrar_menu ( )
    opcion = input ( "Seleccione una opción: " )

    if opcion == "1" :
        agregar_dispositivo ( lista )
    elif opcion == "2" :
        gasto_dispositivo ( lista )
    elif opcion == "3" :
        consumo_total ( lista )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "\n \n - - - Opción no valida. Ingrese una opción valida - - - \n \n" )