a = [ [ 1 , 2 ] , [ 3 , 4 ] ]
b = [ [ 5 , 6 ] , [ 7 , 8 ] ]
C = []
for i in range ( 2 ) :
    fila = []
    for j in range ( 2 ) :
        fila.append ( a [ i ] [ j ] + b [ i ] [ j ] )
    C.append ( fila )



matriz = [
    [ 1 , 2 , 3 ] ,
    [ 4 , 5 , 6 ] ,
    [ 7 , 8 , 9 ]
]

for i in range ( 3 ) :
    print ( matriz [ i ] [ i ] )