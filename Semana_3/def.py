def tabla ( numero , cantidad = 10 ) :
    for i in range ( 1 , cantidad + 1 ) :
        print ( numero , "x" , i , "=" , numero * i )

#tabla ( 5 )

def saludo ( nombre , edad ) :
    print ( "Te llamas:\n" , nombre, "\n" , "tienes: \n" , edad )

#saludo ( "Kenneth" , 18 )

lista = [ 15 , 48 , 50 , 82 , 10 , 19 , 89 ]
def orden ( lista_ordenada ) :
    lista.sort ( ) 
    print ( "Los numeros ordenados son los siguientes:\n" , lista_ordenada )

orden (lista)