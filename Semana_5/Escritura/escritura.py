# open ( nombre , modo )

# Modos principales:
#   "w" escritura (Sobreescribe)
#   "a" agregar (Append)
#   "x" crear (Error si ya existe)

nombre = input ( "Escribe tu nombre: " )
archivo = open ( "Datos.txt" , "w" )
archivo.write ( f"Hola, {nombre} \n" )
archivo.write ( "Estamos escribiendo en un archivo. Clase de programación\n" )
archivo.close ( )  

with open ( "Datos.txt" , "a" ) as archivo :
    archivo.write ( "Nueva linea \n" )

import csv 
with open ( "datos.csv" , "w" , newline= "" ) as file :
    writer = csv.writer ( file )
    writer.writerow ( [ "Nombre" , "Edad" ] )
    writer.writerow ( [ "Ana" , 20 ] )
    writer.writerow ( [ "Miguel" , 20 ] )
    writer.writerow ( [ "Juan" , 20 ] )
    writer.writerow ( [ "Ana" , 20 ] )
    