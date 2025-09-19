def menu ( ) :
    print ( "-" * 178 )
    print ( "- - - Menú. - - -" )
    print ( "1. Mostrar ventas." )
    print ( "2. Estadisticas." )
    print ( "3. Buscar cliente." )
    print ( "4. Salir." )
    print ( "-" * 178 )

def ventas ( ) :
    print ( "-" * 178 )
    print ( "- - - Mostrar ventas. - - -" )
    print ( "-" * 178 )
    print ( f"{'Clientes':<30} {'Producto':<30} {'Monto':<10}" )
    print ( "-" * 178 )
    with open ( "ventas.txt" , "r" ) as f :
        ventas = f.read ( ).splitlines ( )
        for venta in ventas :
            lista_venta = venta.split ( "," )
            print ( f"{lista_venta [ 0 ]:<30}{lista_venta [ 1 ]:<30} {lista_venta [ 2 ]:<10}" )
    print ( "-" * 178 )
    return

def estadisticas ( ) :
    print ( "-" * 178 )
    print ( "- - - Estadísticas- - -" )
    print ( "-" * 178 )
    ventas_cliente = { }
    monto_total = 0
    with open ( "ventas.txt" , "r" ) as f:
        ventas = f.read ( ).splitlines ( )
        for venta in ventas :
            lista_venta = venta.split ( "," )
            if len ( lista_venta ) >= 1 :
                cliente = lista_venta [ 0 ].strip ( )
                monto = float ( lista_venta [ 2 ].strip ( ) )
                ventas_cliente [ cliente ] = ventas_cliente.get ( cliente , 0 ) + monto
                monto_total += monto
    print ( "- - Estadisticas por cliente. - -" )
    print ( "-" * 178 )
    for cliente , monto in ventas_cliente.items ( ) :
        print ( f"{cliente:<30} Total vendido: ${monto:<15}" )
    print ( "-" * 178 )
    print ( "- - Estadisticas generales. - -" )
    print ( f"\nMonto total vendido: ${monto_total:<15}" )
    print ( "-" * 178 )
    return

def cliente ( ) :
    print ( "-" * 178 )
    print ( "- - - Buscar cliente. - - -" )
    nombre = input ( "Nombre del cliente a buscar: " )
    encontrados = [ ]
    with open ( "ventas.txt" , "r" ) as f :
        ventas = f.read ( ).splitlines ( )
        for venta in ventas :
            lista_venta = venta.split ( "," )
            if lista_venta [ 0 ].strip ( ).lower ( ) == nombre.lower ( ) :
                encontrados.append ( lista_venta )
        if encontrados :
            print ( "-" * 178 )
            print ( "- - - Cliente encontrado. - - -" )
            print ( "-" * 178 )
            print ( f"- - - Ventas de { nombre }. - - -" )
            print ( f"{'Cliente':<30}{'Producto':<30}{'Monto':<10}" )
            for c in encontrados :
                print ( f"{c [ 0 ]:<30}{c [ 1 ]:<30}{c [ 2 ]:<10}" )
            print ( "-" * 70 )
        else :
            print ( "-" * 178 )
            print ( "- - - Cliente no encontrado. - - -" )
            print ( "-" * 178 )
    return 

def salir ( ) :
    print ( "-" * 178 )
    print ( "\n\n- - - Gracias por usar el gestor de ventas. ¡Hasta luego! - - -\n\n" )
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