texto = "                                hola, Mundo!"
texto2 = "Python es genial. "
texto3 = texto + " " + texto2
print ( texto3 ) 

texto4 = 15
texto5 = texto + " " + texto2 + " " + str ( texto4 )
print ( texto5 )

print ( type ( texto5 ) )

print ( texto5 [ 0 ] )
print ( texto5 [ 1 ] )
print ( texto5 [ 2 ] )
print ( texto5 [ 3 ] )

print ( texto5 [ 0 : 4 ] )
print ( texto5 [ 5 : 11 ] )
print ( texto5 [ 5 : 11 : 2 ] )

print ( texto5.capitalize ( ) )
print ( texto5.title ( ) ) 
print ( texto5.upper ( ) )
print ( texto5.lower ( ) )
print ( texto5.center ( 50 , "*" ) )
print ( texto5.find ( "Python" ) )

lista = [ "Juan" , "Pedro" ]
nombre = "juan"
for nomb in lista :
    if nombre.lower ( ) == nomb.lower ( ) :
        print ( "El nombre está en la lista" )
        break
if nombre.lower ( ) in lista:
    print ( "El nombre está en la lista" )
else :
    print ( "El nombre no está en la lista" )

texto6 = texto5.replace ( "Python" , "Java" )
print ( texto6 )

print ( texto6.lstrip ( ) )
print ( texto6.rstrip ( ) )
print ( texto6.strip ( ) )

print ( texto6.split ( ) )

email = "juan.perez@example.com"
print ( email.split ( "@" ) )

personas = "Juan, Pedro, Maria,Lucia"
print ( personas.split ( "," ) )
lista_nombres = [ ]
for nombre in personas.split ( "," ) :
    lista_nombres.append ( nombre.strip ( ) )
print ( lista_nombres )

nombre = "Juan"
clase = "Matemáticas"
print ( f"Hola { nombre }, bienvenida a la clase de { clase } { 4 + 3 } " )

print ( "Hola {}, bienvenida a la clase de {} {} ".format ( nombre , clase , 4 + 3 ) )