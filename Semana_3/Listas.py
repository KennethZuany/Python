materias = ["Lengua Materna" , "Matematicas" , "Ciencias" , "Ingles"]
print ( materias [ 0 ] , materias [ -1 ] )

nombres = [ ]
nombres.append ( input ( "Dame el primer nombre:" ) )
nombres.append ( input ( "Dame el segundo nombre:" ) )
nombres.append ( input ( "Dame el tercer nombre:" ) )
nombres.append ( input ( "Dame el cuarto nombre:" ) )
nombres.append ( input ( "Dame el quinto nombre:" ) )
print ( nombres [ : : -1 ] )

temperatura = [ 48, 30, 25, 10, 32 ]
print ( "Temperatura:" , temperatura )
print ( "Temperatura minima:" , min ( temperatura ) )
print ( "Temperatura maxima:" , max ( temperatura ) )
cantidad = len ( temperatura )
suma = sum ( temperatura )
print ( "Cantidad de temperaturas:" , cantidad )
print ( "Suma de temperaturas:" , suma )
promedio = suma / cantidad
print ( "Promedio de temperaturas:" , promedio )