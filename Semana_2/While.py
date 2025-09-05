sigue = True
suma = 0

while sigue :
    numero = int ( input ( "Dame un numero (-1 para terminar): " ) )
    if numero == -1 :
        break
    suma = suma + numero

print ( "La suma de los dos numeros es:" , suma )