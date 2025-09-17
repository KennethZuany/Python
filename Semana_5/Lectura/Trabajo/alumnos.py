def nombres_lista ( ) :
    print ( "-" * 178 )
    print ( "\n - - - Nombres en lista. - - -\n" )
    with open ( "alumnos.txt", "r" ) as f :
        print ( f.read ( ).split ( "\n" ) )
    print ( "-" * 178 )
    return

def numero_alumnos ( ) :
    print ( "-" * 178 )
    print ( "\n - - - Número de alumnos. - - -\n" )
    with open ( "alumnos.txt" , "r" ) as f:
        lineas = f.readlines ( )
        print ( len ( lineas ) )
    print ( "-" * 178 )
    return

def agregar_alumno ( ) :
    print ( "-" * 178 )
    print ( "\n - - - Agregar alumno. - - -\n" )
    nombre = input ( "Introduzca el nombre del alumno a agregar: " ).capitalize ( )
    with open ( "alumnos.txt" , "a" ) as f :
        f.write ( f"\n{nombre}" )
    print ( f"\n - - - {nombre} agregado exitosamente. - - -" )
    print ( "-" * 178 )
    return

def salir ( ) :
    print ( "-" * 178 )
    print ( "\n - - - Gracias por usar el programa. ¡Hasta luego! - - -\n" )
    print ( "-" * 178 )
    return

def menu ( ) :
    print ( "-" * 178 )
    print ( "\n - - - Menú. - - -" )
    print ( "1. Nombres en lista." )
    print ( "2. Número de alumnos." )
    print ( "3. Agregar alumno." )
    print ( "4. Salir" )
    print ( "-" * 178 )

opcion = ""

while opcion != "4" :
    menu ( )
    opcion = input ( "Seleccione una opción: " )
    if opcion == "1" :
        nombres_lista ( )
    elif opcion == "2" :
        numero_alumnos ( )
    elif opcion == "3" :
        agregar_alumno ( )
    elif opcion == "4" :
        salir ( )
    else :
        print ( "-" * 178 )
        print ( "\n - - - Opción no válida. Por favor, ingresa una opción del 1 al 4. - - -\n" )
        print ( "-" * 178 )