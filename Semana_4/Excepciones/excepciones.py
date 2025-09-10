# 1
try :
    numero = int ( input ( "Ingrese un número: " ) )
    resultado = 10 / numero
    print ( "El resultado es:" , resultado )
except ZeroDivisionError :
    print ( "Error: No se puede dividir por cero." )

# 2
try :
    archivo = open ( "archivo_inexistente.txt" )
    contenido = archivo.read ( )
except FileNotFoundError :
    print ( "Error: El archivo no existe." )
except PermissionError :
    print ( "Error: No tiene permiso para leer el archivo." )

# 3
try :
    n = int ( input ( "Número: " ) )
    print ( 100 / n )
except ZeroDivisionError :
    print ( "No se puede dividir por cero." )
except ValueError :
    print ( "Debe ingresar un número válido." )
else :
    print ( "La operación se realizó correctamente." )
finally :
    print ( "Fin del programa." )

# 4
try :
    number = int ( input ( "Ingrese un número: " ) )
    print ( number / 5 )
except ValueError :
    print ( "Error: Debe ingresar un número válido." )

# 5 
try : 
    edad = int ( input ( "Ingrese su edad: " ) )
    if edad < 0 or edad > 120 :
        raise ValueError
    print ( edad )
except ValueError :
    print ( "Error: Debe ingresar un número válido para la edad." )

# reclucibidad
def edad_valida ( ) :
    try: 
        edad = int ( input ( "Ingrese su edad: " ) )
        if int ( edad ) < 0 :
            print ( "Edad no válida, intente de nuevo." )
            edad_valida ( )
            return
        print ( "Edad ingresada:", edad )
    except ValueError :
        print ( "Error: Debe ingresar un número válido para la edad." )
        edad_valida ( )
    except TypeError :
        print ( "Error: Tipo de dato inválido." )

edad_valida ( )