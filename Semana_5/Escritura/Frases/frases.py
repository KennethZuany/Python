archivo_nombre = input ( "Nombre del archivo: " )

with open ( f"{archivo_nombre}.txt" , "w" ) as file :

    for i in range ( 4 ) :
        frase = input ( "Una frase" )
        file.write ( f"{frase}\n" )