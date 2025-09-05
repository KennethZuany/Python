# Menu
def mostrar_menu ( ) :
    print ( "Bienvenido a la calculadora de áreas.\n ¿Qué quieres que haga? ") 
    print ( "1. Calcular área del cuadrado" )
    print ( "2. Calcular área del rectangulo" )
    print ( "3. Calcular área del circulo" )
    print ( "4. Salir")

# Área cuadrado
def area_cuadrado ( ) :
    lado = float ( input ( "¿Cuánto mide el lado? " ) )
    return lado * lado 

# Área rectangulo
def area_rectangulo ( ) :
    base = float ( input ( "¿Cuánto mide la base? " ) )
    altura = float ( input ( "¿Cuánto mide la altura? " ) )
    return base * altura

# Área circulo
def area_circulo ( ) :
    pi = 3.1416
    radio = float ( input ( "¿Cuánto mide el radio? " ) )
    radio_2 = float ( radio * radio )
    return pi * radio_2 

# Salir
def salir ( ) :
    print ( "Gracias por usa la agenda. ¡Hasta luego!" )

# Variable
opcion = ""
resultado = ""