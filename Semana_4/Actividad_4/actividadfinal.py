# Menú
def menu ( ) :
    print ( "-" * 130 )
    print ( "\n - - - Menú de la Biblioteca Digital - - - \n" )
    print ( "1. Registrar libro" )
    print ( "2. Consultar biblioteca" )
    print ( "3. Buscar libro" )
    print ( "4. Eliminar libro" )
    print ( "5. Ver estadísticas" )
    print ( "6. Salir" )
    print ( "-" * 130 )

# Registrar libro
def registrar_libro ( biblioteca , fecha_registro ) :
    print ( "-" * 130 )
    print ( "\n - - - Registrar libro - - - \n")
    print ( "-" * 130 )
    while True :
        try :
            titulo = str ( input ( "Ingrese el título del libro: " ).strip ( ).title ( ) )
            autor = str ( input ( "Ingrese el autor del libro: " ).strip ( ).title ( ) )
            año = int ( input ( "Ingrese el año de publicación del libro: " ).strip ( ) )
            genero = str ( input ( "Ingrese el género del libro: " ).strip ( ).title ( ) )
            break
        except ( ValueError , TypeError ) :
            print ( "-" * 130 )
            print ( "Entrada no válida. Por favor, ingrese una entrada válida." )
            print ( "-" * 130 )
    libro = { "Título" : titulo , "Autor" : autor , "Año" : año , "Género" : genero , "Fecha de registro (DD, MM, YYYY)" : fecha_registro }
    biblioteca.append ( libro )
    print ( "-" * 130 )
    print ( f"\n - - - El libro '{ titulo }' de {autor} ha sido registrado exitosamente. - - -\n")
    print ( "-" * 130 )
    return biblioteca

# Consultar biblioteca
def consultar_libros ( biblioteca ) :
    print ( "-" * 130 )
    print ( "\n - - - Consultar biblioteca - - - \n" )
    print ( "-" * 130 )
    if biblioteca :
        print ( f"{'Título':<30} {'Autor':<30} {'Año':<6} {'Género':<20} {'Fecha de registro (DD, MM, YYYY)':<15}" )
        print ( "-" * 130 )
        for libro in biblioteca :
            print ( f"{libro['Título']:<30} {libro['Autor']:<30} {libro['Año']:<6} {libro['Género']:<20} {libro['Fecha de registro (DD, MM, YYYY)']}" )
        print ( "-" * 130 )
    else :
        print ( "\n - - - No hay libros registrados en la biblioteca. - - - \n" )
    return biblioteca

# Buscar libro
def buscar_libro ( biblioteca ) :
    print ( "-" * 130 )
    print ( "\n - - - Buscar libro - - - \n" )
    print ( "-" * 130 )
    if biblioteca :
        titulo = input ( "Ingrese el libro a buscar: " ).strip ( )
        encontrados = [ libro for libro in biblioteca if libro [ "Título" ] == titulo ]
        if encontrados :
            print ( " \n - - - Libro encontrado - - - \n" )
            print ( "-" * 130)
            for libro in encontrados :
                print ( f"Título: { libro [ 'Título' ] }" )
                print ( f"Autor: { libro [ 'Autor' ] }" )
                print ( f"Año: { libro [ 'Año' ] }")
                print ( f"Género: { libro ['Género' ] }" )
                print ( f"Fecha de registro: { libro ['Fecha de registro (DD, MM, YYYY)'] }" )
                print ( "-" * 130 )
        else :
            print ( "-" * 130 )
            print ( "\n - - - Libro no encontrado - - - \n" )
            print ( "-" * 130 )
    else:
        print ( "-" * 130 )
        print ( "\n - - - No hay libros registrados en la biblioteca. - - - \n" )
        print ( "-" * 130)
    return biblioteca

# Eliminar libro    
def eliminar_libro ( biblioteca ) :
    print ( "-" * 130 )
    print ( "\n - - - Eliminar libro - - - \n" )
    print ( "-" * 130 )
    if biblioteca :
        titulo = input ( "Ingrese el título del libro a eliminar: " ).strip ( )
        for libro in biblioteca :
            if libro [ "Título" ] == titulo :
                biblioteca.remove ( libro )
                print ( "-" * 130)
                print ( f"\n - - - El libro '{ titulo }' ha sido eliminado exitosamente. - - - \n" )
                print ( "-" * 130 )
                return biblioteca
        print ( "-" * 130 )
        print ( "\n - - - Libro no encontrado. No se pudo eliminar. - - - \n" )
        print ( "-" * 130 )
    else:
        print ( "-" * 130 ) 
        print ( "\n - - - No hay libros registrados en la biblioteca. - - - \n" )
        print ( "-" * 130 )
    return biblioteca

# Ver estadísticas
def estadisticas ( biblioteca ) :
    print ( "-" * 130 )
    print ( "\n - - - Estadísticas de la Biblioteca - - - \n" )
    print ( "-" * 130 )
    total_libros = len ( biblioteca )
    if total_libros == 0 :
        print ( "-" * 130 )
        print ( "- - - No hay libros registrados en la biblioteca. - - -" )
        print ( "-" * 130 )
        return biblioteca
    autores = { libro [ "Autor" ] : 0 for libro in biblioteca }
    generos = { libro [ "Género" ] : 0 for libro in biblioteca }
    for libro in biblioteca :
        autores [ libro [ "Autor" ] ] += 1
        generos [ libro [ "Género" ] ] += 1
        autor_mas_publicaciones = max ( autores , key = autores.get )
        genero_mas_frecuente = max ( generos , key = generos.get )
    print ( "-" * 130 )
    print ( f"Total de libros registrados: { total_libros }" )
    print ( f"Autor con más publicaciones: { autor_mas_publicaciones } ( { autores [ autor_mas_publicaciones ] } libros ) " )
    print ( f"Género más frecuente: { genero_mas_frecuente } ( { generos [ genero_mas_frecuente ] } libros ) " )
    print ( "-" * 130 )
    return biblioteca

# Salir
def salir ( ) :
    print ( "-" * 130 )
    print ( "\n - - - Gracias por usar el gestor de biblioteca digital. ¡Hasta luego! - - - \n" )
    print ( "-" * 130 )
    return

# Fecha de registro
def fecha ( ) :
    try :
        fecha_registro = ( int ( input ( "Fecha de registro - Día (DD): " ) ) , int ( input ( "Fecha de registro - Mes (MM): " ) ) , int ( input ( "Fecha de registro - Año (YYYY): " ) ) )
        return fecha_registro
    except ( ValueError , TypeError ) :
        print ( "-" * 130 )
        print ( "\n - - - Opción no válida. Por favor, registre una fecha válida. - - - \n" )
        print ( "-" * 130 )
        return fecha ( )
        
# Opción
def opcion_menu ( ) :
    try :
        opcion = int ( input ( "Seleccione una opción: " ) )
        return opcion
    except ( ValueError , TypeError ) :
        print ( "-" * 130 )
        print ( "\n - - - Opción no válida. Por facor, ingresa una opción del 1 al 6. - - - \n" )
        print ( "-" * 130 )
        return opcion_menu ( )

# Programa principal
biblioteca = [
{"Título": "Cien años de soledad", "Autor": "Gabriel García Márquez", "Año":
1967, "Género": "Novela", "Fecha de registro (DD, MM, YYYY)": (1, 3, 2023)},
{"Título": "1984", "Autor": "George Orwell", "Año": 1949, "Género":
"Distopía", "Fecha de registro (DD, MM, YYYY)": (12, 5, 2023)},
{"Título": "Don Quijote de la Mancha", "Autor": "Miguel de Cervantes", "Año":
1605, "Género": "Novela", "Fecha de registro (DD, MM, YYYY)": (20, 8, 2023)},
{"Título": "El Principito", "Autor": "Antoine de Saint-Exupéry", "Año": 1943,
"Género": "Fábula", "Fecha de registro (DD, MM, YYYY)": (7, 6, 2023)},
{"Título": "Crimen y castigo", "Autor": "Fiódor Dostoievski", "Año": 1866,
"Género": "Novela", "Fecha de registro (DD, MM, YYYY)": (15, 4, 2023)},
{"Título": "Rayuela", "Autor": "Julio Cortázar", "Año": 1963, "Género":
"Novela", "Fecha de registro (DD, MM, YYYY)": (22, 7, 2023)},
{"Título": "Fahrenheit 451", "Autor": "Ray Bradbury", "Año": 1953, "Género":
"Ciencia ficción", "Fecha de registro (DD, MM, YYYY)": (30, 9, 2023)},
{"Título": "La Odisea", "Autor": "Homero", "Año": -800, "Género": "Épica",
"Fecha de registro (DD, MM, YYYY)": (11, 10, 2023)},
{"Título": "Pedro Páramo", "Autor": "Juan Rulfo", "Año": 1955, "Género":
"Novela", "Fecha de registro (DD, MM, YYYY)": (3, 11, 2023)},
{"Título": "Orgullo y prejuicio", "Autor": "Jane Austen", "Año": 1813,
"Género": "Romántica", "Fecha de registro (DD, MM, YYYY)": (25, 12, 2023)},
{"Título": "Drácula", "Autor": "Bram Stoker", "Año": 1897, "Género": "Terror",
"Fecha de registro (DD, MM, YYYY)": (5, 1, 2024)},
{"Título": "La sombra del viento", "Autor": "Carlos Ruiz Zafón", "Año": 2001,
"Género": "Novela", "Fecha de registro (DD, MM, YYYY)": (14, 2, 2024)}
]

opcion = ""

while opcion != "6" :
    menu ( )
    opcion = str ( opcion_menu ( ) )
    print ( "-" * 130 )
    if opcion == "1" :
        fecha_registro = fecha ( )
        registrar_libro ( biblioteca , fecha_registro )
    elif opcion == "2" :
        consultar_libros ( biblioteca )
    elif opcion == "3" :
        buscar_libro ( biblioteca )
    elif opcion == "4" :
        eliminar_libro ( biblioteca )
    elif opcion == "5" :
        estadisticas ( biblioteca )
    elif opcion == "6" :
        salir ( )
    else :
        print ( "-" * 130 )
        print ( "\n - - - Opción no válida. Por favor, seleccione una opción del 1 al 6. - - - \n" )   
        print ( "-" * 130 )