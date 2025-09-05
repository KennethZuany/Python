# Menu
def mostrar_menu ( ) :
    print ( "\n--- Menú de Agenda ---" )
    print ( "1. Agregar contacto" )
    print ( "2. Mostrar contactos" )
    print ( "3. Buscar contacto" )
    print ( "4. Salir" )

# Agregar Contacto
def agregar_contacto ( lista ) :
    nombre = input ( "Ingrese el nombre: " )
    telefono = input ( "Ingrese el teléfono: " )
    correo = input ( "Ingrese el correo: " )
    lista.append ( [nombre , telefono , correo] )
    print ( "Contacto agregado con éxito." )

# Mostrar Contacto
def mostrar_contactos ( lista ) :
    for contacto in lista :
        print ( contacto[0] , contacto[1] , contacto[2] )

# Buscar Contacto
def buscar_contacto ( lista ) :
    nombre = input ( "Ingrese el nombre a buscar: " )
    encontrados = [c for c in lista if c[0] == nombre]
    if encontrados :
        print ( "\n--- Contacto encontrado ---" )
        for c in encontrados :
            print ( "Nombre:", c[0], "| Teléfono:", c[1], "| Correo:", c[2])
    else :
        print ( "Contacto no encontrado." )

# Salir
def salir ( ) :
    print ( "Gracias por usar la agenda. ¡Hasta luego!" )

# Variable y lista
agenda = []
opcion = ""