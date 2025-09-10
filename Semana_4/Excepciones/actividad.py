numeros = [ ] 

def pedir_numero ( pedida = 3 ) :
    while pedida > 0 :
        try :
            numero = int ( input ( "Ingrese un número: " ) )
        except ValueError :
            print ( "Error: Debe ingresar un número válido." )
            continue
        pedida -= 1
        numeros.append ( numero )
    return numeros

def mostrar_lista ( lista ) :
    print ( "Números ingresados:" )
    for numero in lista :
        print ( numero )

def promedio ( lista ) :
    print ( "El promedio es:" , sum ( lista ) / len ( lista ) )

while True :
    pedir_numero ( )
    mostrar_lista ( numeros )
    promedio ( numeros )
    break