# Menú
def mostrar_menu( ) :
    print ( "\n \n- - - Menú de la Calculadora - - -\n" )
    print ( "1. Agregar dispositivo." )
    print ( "2. Buscar gasto de un dispositivo." )
    print ( "3. Consumo de todos los dispositivos." )
    print ( "4. Salir" )

# Agregar dispositivo
def agregar_dispositivo ( dispositivos ) :
    print ( "\n- - - Agregar dispositivo - - -" )
    dispositivo = input ( "Nombre del dispositivo: " )
    consumo = float ( input ( "Consumo del dispositivo (W): " ) )
    uso = float ( input ( "Uso diario (H): " ) )
    dispositivos.append ( [dispositivo , consumo , uso ] )
    print ( "\n- - - Dispositivo agregado exitosamente - - - " )

# Calcular kWh mes
def calcular_kwh_mes ( watts , horas , costo_kwh ) :
    consumo_diario = watts * horas
    consumo_mensual = consumo_diario * 30 / 1000
    costo_mensual = consumo_mensual * costo_kwh
    return consumo_mensual , costo_mensual

# Gasto de un dispositivo
def gasto_dispositivo ( dispositivos , costo_kwh ) :
   print ( " \n- - - Buscar gasto de un dispositivo - - - ")
   dispositivo = input ( "Nombre del dispositivo a buscar: " )
   encontrados = [ c for c in dispositivos if c [ 0 ] == dispositivo ]
   if encontrados :
       print ( "\n- - - Dispositivo encontrado - - - ")
       for c in encontrados :
           print ( "Dispositivo:" , c [ 0 ] , "| Consumo (W):" , c [ 1 ] , "| Uso (H):" , c [ 2 ] )
           consumo_total = int ( c [ 1 ] ) * int ( c [ 2 ] )
           consumo_mensual, costo_mensual = calcular_kwh_mes ( c [ 1 ] , c [ 2 ] , costo_kwh)
           print ( "Dispositivo:" , c [ 0 ] , "| Consumo mensual:" , round ( consumo_mensual ) , "kWh" , "| Costo mensual:" , round ( costo_mensual ) , "pesos" )
           print ( "El consumo total del dispositivo es:" , round ( consumo_total )  , "Wh" )
   else : 
    print ( "\n - - - Dispositivo no encontrado - - - \n")

# Consumo de todos los dispositivos 
def consumo_total ( dispositivos , costo_kwh ) :
    print ( "\n- - - Consumo de todos los dispositivos - - - \n" )  
    total_kwh = 0
    total_costo = 0
    for d in dispositivos :
        consumo_mensual , costo_mensual = calcular_kwh_mes ( d [ 1 ] , d [ 2 ] , costo_kwh )
        print ( "Dispositivo:" , d [ 0 ] , "| Consumo mensual:" , round ( consumo_mensual ) , "kWh" , "| Costo mensual:" , round ( costo_mensual ) , "pesos" )
        total_kwh += consumo_mensual
        total_costo += costo_mensual
    print ( "\nConsumo total mensual:" , round ( total_kwh ) , "kWh" )
    print ( "Costo total mensual:" , round ( total_costo ) , "pesos" )
    return total_kwh, total_costo
        

# Salir
def salir ( ) :
    print ( "\n \n- - - Gracias por usar la calculadora. ¡Hasta luego!- - - \n \n " )

# Variable y lista
dispositivos = [ ]
opcion = ""

# Programa
costo_kwh = float ( input ( "\n \n Ingrese el costo por kWh en pesos: " ) )
while opcion != "4" :
    mostrar_menu ( )
    opcion = input ( "Seleccione una opción: " )
    if opcion == "1" :
        agregar_dispositivo ( dispositivos )
    elif opcion == "2" :
        gasto_dispositivo ( dispositivos, costo_kwh )
    elif opcion == "3" :
        consumo_total ( dispositivos , costo_kwh )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "\n \n - - - Opción no valida. Ingrese una opción valida - - - \n \n" )