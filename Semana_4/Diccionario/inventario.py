inventario = {
    "Telefono" : 10 ,
    "Tablet" : 5 ,
    "Laptop" : 20
}

opcion = ""

def mostrar_menu ( ) :
    print ( "\n- - - Menú de Inventario - - - \n " )
    print ( "1. Mostrar inventario" )
    print ( "2. Agregar producto" )
    print ( "3. Actualizar cantidad" )
    print ( "4. Eliminar producto" )
    print ( "5. Salir" )

def mostrar_inventario ( inventario ) :
    print ( "\n - - - Inventario - - - \n" )
    for producto in inventario :
        print ( producto , ":" , inventario [ producto ] )

def agregar_producto ( inventario ) :
    print ( "\n - - - Agregar producto - - - \n" )
    nombre = input ( "Ingrese el nombre del producto (singular): " )
    if nombre in inventario :
        print ( "\n - - - El producto ya existe. Intente de nuevo. - - -" )
    else :
        cantidad = int ( input ( "Ingrese la cantidad del producto: " ) )
        inventario [ nombre ] = cantidad
        print ( "\n - - - Producto agregado con éxito. - - -" )

def actualizar_cantidad ( inventario ) :
    print ( "\n - - - Actualizar cantidad - - - \n" )
    nombre = input ( "Ingrese el nombre del producto a actualizar: " )
    if nombre in inventario :
        cantidad = int ( input ( "Ingrese la nueva cantidad: " ) )
        inventario [ nombre ] = cantidad
        print ( "\n - - - Cantidad actualizada con éxito. - - -" )
    else :
        print ( "\n - - - El producto no existe en el inventario. - - -" )


def eliminar_producto ( inventario ) :
    print ( "\n - - - Eliminar producto - - - \n" )
    nombre = input ( "Ingrese el nombre del producto a eliminar: " )
    if nombre in inventario :
        del inventario [ nombre ]
        print ( "\n - - - Producto eliminado con éxito. - - -" )
    else :
        print ( "\n - - - El producto no existe en el inventario. - - -" )

def salir ( ) :
    print ( "\n - - - Gracias por usar el sistema de inventario. ¡Hasta la vista Baby! - - -" )

while opcion != "5" :
    mostrar_menu ( )
    opcion = input ( "Seleccione una opción: " )

    if opcion == "1" :
        mostrar_inventario ( inventario )
    elif opcion == "2" :
        agregar_producto ( inventario )
    elif opcion == "3" :
        actualizar_cantidad ( inventario )
    elif opcion == "4" :
        eliminar_producto ( inventario )
    elif opcion == "5" :
        salir ( )
    else :
        print ( "\n - - - Opción no válida. Intente de nuevo. - - -" )