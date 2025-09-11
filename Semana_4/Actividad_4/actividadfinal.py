# Menú
def menu ( ) :
    print ( "\n\n - - - Menú de la Biblioteca Digital - - - \n" )
    print ( "1. Registrar libro" )
    print ( "2. Consultar biblioteca" )
    print ( "3. Buscar libro" )
    print ( "4. Eliminar libro" )
    print ( "5. Ver estadísticas" )
    print ( "6. Salir" )

# Registrar libro
def registrar_libro ( biblioteca , fecha_registro ) :
    print ( "\n\n - - - Registrar libro - - - \n")
    titulo = input ( "Ingrese el título del libro: " ).strip ( ).title ( )
    autor = input ( "Ingrese el autor del libro: " ).strip ( ).title ( )
    while True :
        try :
            año = int ( input ( "Ingrese el año de publicación del libro: " ).strip ( ) )
            break
        except ValueError :
            print ( "Año inválido. Por favor, ingrese un número entero.")
    genero = input ( "Ingrese el género del libro: " ).strip ( ).title ( )
    libro = { "Título" : titulo , "Autor" : autor , "Año" : año , "Género" : genero , "Fecha de registro (DD, MM, YYYY)" : fecha_registro }
    biblioteca.append ( libro )
    print ( f"\n - - - El libro '{ titulo }' de {autor} ha sido registrado exitosamente. - - -\n")
    return biblioteca

# Consultar libros
def consultar_libros ( biblioteca ) :
    print ( "\n\n - - - Consultar biblioteca - - - \n" )
    if biblioteca :
        print ( f"{'Título'} {'Autor'} {'Año'} {'Género'} {'Fecha de registro (DD, MM, YYYY)'}" )
        print ( "-" * 100 )
        for libro in biblioteca :
            print ( f"{libro['Título']} {libro['Autor']} {libro['Año']} {libro['Género']} {libro['Fecha de registro (DD, MM, YYYY)']}" )
    else :
        print ( "\n - - - No hay libros registrados en la biblioteca. - - - \n" )
    return biblioteca

# Buscar libro
def buscar_libro ( biblioteca ) :
    print ( "\n\n - - - Buscar libro - - - \n" )
    titulo = input ( "Ingrese el libro a buscar: " ).strip ( ).title ( )
    encontrados = [ libro for libro in biblioteca if libro [ "Título" ] == titulo ]
    if encontrados :
        print ( " \n - - - Libro encontrado - - - \n" )
        for libro in encontrados :
            print ( f"Título: { libro [ 'Título' ] }" )
            print ( f"Autor: { libro [ 'Autor' ] }" )
            print ( f"Año: { libro [ 'Año' ] }")
            print ( f"Género: { libro ['Género' ] }" )
            print ( f"Fecha de registro: { libro ['Fecha de registro (DD, MM, YYYY)'] }" )
            print ( "-" * 40 )
    else :
        print ( "\n - - - Libro no encontrado - - - \n" )
    return biblioteca

# Eliminar libro    
def eliminar_libro ( biblioteca ) :
    print ( "\n\n - - - Eliminar libro - - - \n" )
    titulo = input ( "Ingrese el título del libro a eliminar: " ).strip ( ).title ( )
    for libro in biblioteca :
        if libro [ "Título" ] == titulo :
            biblioteca.remove ( libro )
            print ( f"\n - - - El libro '{ titulo }' ha sido eliminado exitosamente. - - - \n" )
            return biblioteca
    print ( "\n - - - Libro no encontrado. No se pudo eliminar. - - - \n" )
    return biblioteca

# Ver estadísticas (Total de libros, autor con más publicaciones, género más frecuente)
def estadisticas ( biblioteca ) :
    print ( "\n\n - - - Estadísticas de la Biblioteca - - - \n" )
    total_libros = len ( biblioteca )
    if total_libros == 0 :
        print ( "No hay libros registrados en la biblioteca." )
        return biblioteca
    autores = { libro [ "Autor" ] : 0 for libro in biblioteca }
    generos = { libro [ "Género" ] : 0 for libro in biblioteca }
    for libro in biblioteca :
        autores [ libro [ "Autor" ] ] += 1
        generos [ libro [ "Género" ] ] += 1
        autor_mas_publicaciones = max ( autores , key = autores.get )
        genero_mas_frecuente = max ( generos , key = generos.get )
    print ( f"Total de libros registrados: { total_libros }" )
    print ( f"Autor con más publicaciones: { autor_mas_publicaciones } ( { autores [ autor_mas_publicaciones ] } libros ) " )
    print ( f"Género más frecuente: { genero_mas_frecuente } ( { generos [ genero_mas_frecuente ] } libros ) " )
    return biblioteca

# Salir
def salir ( ) :
    print ( "\n\n - - - Gracias por usar el gestor de biblioteca digital. ¡Hasta luego! - - - \n\n" )
    return

# Fecha de registro
def fecha ( ) :
    try :
        fecha_registro = ( int ( input ( "Fecha de registro - Día (DD): " ) ) , int ( input ( "Fecha de registro - Mes (MM): " ) ) , int ( input ( "Fecha de registro - Año (YYYY): " ) ) )
        return fecha_registro
    except ( ValueError , TypeError ) :
        print ( "\n - - - Opción no válida. Por favor, registre una fecha válida. - - - \n" )
        return fecha ( )
        
# Opción
def opcion_menu ( ) :
    try :
        opcion = int ( input ( "Seleccione una opción: " ) )
        return opcion
    except ( ValueError , TypeError ) :
        print ( "\n - - - Opción no válida. Por facor, ingresa una opción del 1 al 6. - - - \n" )
        return opcion_menu ( )

# Programa principal
biblioteca = [ { "Título" : str , "Autor" : str , "Año" : int , "Género" : str , "Fecha de registro (DD, MM, YYYY)" : str} ]

while opcion != "6" :
    menu ( )
    opcion = str ( opcion_menu ( ) )
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
        print ( "\n - - - Opción no válida. Por favor, seleccione una opción del 1 al 6. - - - \n" )   