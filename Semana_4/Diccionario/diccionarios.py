alumno = { "nombre" : "Juan" , "edad" : 21 , "carrera": [ "IDS" ] }

colores = { "rojo" : "#FF0000" , "azul" : "#0000FF" }
dict ( nombre = "Juan" , edad = 21 )

#print ( alumno [ "nombre" ] )
#print ( alumno.get ( "nombre" ) )

for k in alumno.keys ():
    print ( k )

for v in alumno.values ():
    print ( v )

for k , v in alumno.items ():
    print ( k , v )

# keys () devuelve todas las claves
# values () devuelve todos los valores
# items () devuelve pares ( clave , valor )
# update () actualiza el diccionario
# pop () elimina un elemento y lo devuelve
# popitem () elimina el último elemento y lo devuelve


frutas = {
    1: { "nombre" : "manzana" , "color" : "roja" } ,
    2: { "color" : "mango" , "color" : "amarillo" } ,
    3: { "nombre" : "fresa" , "color" : "roja" } 
}


#print ( frutas [ 1 ] [ "nombre" ] ) 

frutas [ 4 ] = {
    "nombre" : "sandia" ,
    "color" : "verde"
}

frutas [ 1 ] [ "color" ] = "verde"
#print ( frutas [ 1 ] )

del frutas [ 3 ]

frutas.pop ( 2 )

print ( frutas.keys ( ) )
print ( frutas.values ( ) )
print ( frutas.items ( ) )

for key in frutas :
    print ( key )

for values in frutas.values ( ) :
    print ( values )

for items in frutas.items ( ) :
    print ( items ) 

for key , values in frutas.items ( ) :
    print ( "La clave es:" , key , "El valor es:" , values )


alumnos = {
    12345 : { "nombre:" : "Juan" , "edad" : 21 , "carrera" : "IDS" } ,
    12346 : { "nombre:" : "Ana" , "edad" : 22 , "carrera" : "DS" } ,
    12347 : { "nombre:" : "Luis" , "edad" : 20 , "carrera" : "DS" } 
}

print ( alumnos )

for alumno in alumnos.values ( ) :
    print ( "nombre:" , alumno [ "nombre:" ] )

alumnos [ 12348 ] = { "nombre" : "Maria" , "edad" : 23 , "carrera" : [ "IDS" , "IDS" ] }
print ( alumnos )
alumnos [ 12345 ] [ "edad" ] = 22
print ( alumnos )
alumnos.pop ( 12346 )
print ( alumnos )