# Gestor de reportes de ventas.
# El programa debe:
#   Solicitar al usuario el nombre de un archivo donde guardará la información. (Si no existe, debe crearse automaticamente)
#   Permitir registrar ventas (producto, cantidad y precio unitario)
#   Guardar cada venta en el archivo en formato CSV o texto estructurado.
#   Mostrar en pantalla el historial completo de ventas leyendo desde el archivo.
#   Calcular y mostrar el total de ventas acumuladas.
#   Permitir eliminar un registro de venta específico (para esto, deberas reescribir el archivo sin ese dato).
# Implementa manejo de excepciones para los casos:
#   Archivo inexistente.
#   Error de formato al leer los datos.
#   Ingreso de datos no válidos.
# REQUISITOS EXTRA:
#   Usa funciones para separar las tareas principales: registrar_venta(), monstra_venta(), calcular_total(), eliminar_venta().
#   Al final, genera un archivo "reporte_final.txt" con el resumen de todas las ventas registradas durante la sesión, incluyendo el total acumulado y la fecha del reporte.

nombre_archivo = ""

def crear_archivo ( ) :
    print ( "-" * 178 )
    print ( "\n- - - Crear archivo. - - -\n" )
    nombre = input ( "Introduzca el nombre del archivo a crear: " ).title ( )
    try :
        archivo = open ( f"{nombre}.txt" , "x" )
        with open ( f"{nombre}.txt" , "w" ) as f :
            f.write ( f"{'Producto':<30} {'Cantidad (PZS)':<30} {'Precio unitario':<30}\n" )
            f.write ( "-" * 100)
        return archivo
    except FileExistsError :
        print ( "-" * 178 )
        print ( "\n- - - Error: El archivo ya existe. - - -\n" )
        print ( "-" * 178 )

def registrar_venta ( ) :
    print ( "-" * 178 )
    print ( "\n- - - Registrar venta. - - -\n" )
    nombre = input ( "Nombre del archivo donde registrará la venta: " ).title ( )
    try :  
        archivo = open ( f"{nombre}.txt" , "a" )
        producto = input ( "Introduzca el producto vendido: " ).title ( )
        try :
            cantidad = int ( input ( "Introduzca la cantidad vendida: " ) )
            precio_unidad = int ( input ( "Introduzca el precio unitario: " ) )
            archivo.write ( f"\n{producto:<30} {cantidad:<30} ${precio_unidad:<30}" )
            return archivo
        except ValueError :
            print ( "-" * 178 )
            print ( "\n- - - Error: Debe ingresar un valor válido. - - -" )
            print ( "-" * 178 )
            return registrar_venta ( )
    except FileNotFoundError :
        print ( "-" * 178 )
        print ( "\n- - - Error: Archivo no encontrado. - - -\n" )
        print ( "-" * 178 )
        return registrar_venta ( )
    
def historial_ventas ( ) :
    print ( "-" * 178 )
    print ( "\n- - - Historial de ventas. - - -\n" )
    nombre = input ( "Nombre del archivo de donde generara el historial: " ).title ( )
    try :
        archivo = open ( f"{nombre}.txt" , "r" )
        print ( archivo )
    except FileNotFoundError :
        print ( "-" * 178 )
        print ( "\n- - - Error: Archivo no encontrado. - - -\n" )
        print ( "-" * 178 )

def salir ( ) :
    print ( "-" * 178 )
    print ( "\n\n- - - Gracias por usar el gestor de ventas. ¡Hasta luego! - - -\n\n" )
    print ( "-" * 178 )

def menu ( ) :
    print ( "-" * 178 )
    print ( "\n- - - Menú. - - -\n" )
    print ( "1. Crear archivo de venta." )
    print ( "2. Registrar venta (Primero debe crear el archivo)." )
    print ( "3. Historial de ventas.")
    print ( "4. Salir ")
    print ( "-" * 178 )

opcion = ""

while opcion != "4" :
    menu ( )
    opcion = input ( "Seleccione una opción del menú: " )
    if opcion == "1" :
        crear_archivo ( )
    elif opcion == "2" :
        registrar_venta ( )
    elif opcion == "3" :
        historial_ventas ( )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "-" * 178 )
        print ( "\n- - - Error: Opción no válida. - - -\n" ) 
        print ( "-" * 178 )