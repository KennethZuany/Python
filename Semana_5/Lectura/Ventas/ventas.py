def menu ( ) :
    print ( "-" - 178 )
    print ( "- - - Menú. - - -" )
    print ( "1. Mostrar ventas." )
    print ( "2. Estadisticas." )
    print ( "3. Buscar cliente." )
    print ( "4. Salir." )
    print ( "-" * 178 )

def ventas ( ) :
    print ( "-" * 178 )
    print ( "- - - Mostrar ventas. - - -" )
    print ( f"{'Cliente':<10} {'Producto':<30} {'Monto':<8}" )
    with open ( "ventas.txt" , "r" ) as f :
        print ( f.read ( ).split ( "\n" ) )
    print ( "-" * 178 )
    return

def estadisticas ( ) :
    print ( "-" * 178 )
    print ( "- - - Estadisticas- - -" )
    print ( "- - Estadisticas por cliente. - -" )
    with open ( "ventas.txt" , "r" ) as f :
        #ventas por cliente
    print ( "- - Estadisticas generales. - -" )
    with open ( "ventas.txt" , "r" ) as f :
        #venta total
    print ( "-" * 178 )
    return

def cliente ( ) :
    print ( "-" * 178 )
    print ( "- - - Buscar cliente. - - -" )
    with open ( "ventas.txt" , "r" ) as f :
        ventas = f.read ( ).split ( "\n" ) 
        if ventas :
            nombre = input ( "Nombre del cliente a buscar: " )
            encontrados = [ c for c in ventas if c [ 0 ] == nombre ]
            if encontrados :
                print ( "-" * 178 )
                print ( "- - - Cliente encontrado. - - -" )
                for c in encontrados :
                    print ( f"- - - Ventas de { nombre }. - - -" )
                print ( "")
            else :
                print ( "-" * 178 )
                print ( "- - - Cliente no encontrado. - - -" )
                print ( "-" * 178 )
        else :
            print ( "-" * 178 )
            print ( "- - - No hay ventas. - - -" )
            print ( "-" * 178 )
    return 

def salir ( ) :
    print ( "-" * 178 )
    print ( "- - - Gracias por usar el gestor de ventas. ¡Hasta luego! - - -" )
    print ( "-" * 178 )
    return

opcion = ""

while opcion != "4" :
    menu ( )
    opcion = input ( "Seleccione una opción: " )
    if opcion == "1" :
        ventas ( )
    elif opcion == "2" :
        estadisticas ( )
    elif opcion == "3" :
        cliente ( )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "-" * 178 )
        print ( "- - - Opción no válida. Ingrese una opción válida. - - -" )
        print ( "-" * 178 ) 