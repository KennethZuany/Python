with open ( "Biblioteca.txt" , "w" ) as file :
    n = int ( input ( "Número de libros: " ) )
    file.write ( f"{'Nombre':<15} {'Autor':<10} {'Año':<6}\n")
    for i in range ( n ) :
        nombre = input ( "Nombre del libro: " )
        autor = input ( "Autor del libro: " )
        año = int ( input ( "Año de publicación: " ) )
        file.write ( f"{nombre:<15} {autor:<10} {año:<6}\n")
