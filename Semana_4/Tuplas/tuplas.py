tupla = ( 1 , 2 , 3 , 4 )
tupla2 = ( "Rojo" , "Verde" , "Azul" )

print ( tupla [ 0 ] )
print ( tupla [ 1 ] )
print ( tupla [ 2 ] )
print ( tupla [ 3 ] )
print ( tupla )
print ( tupla2 [ 0 ] ) 
print ( tupla2 [ 1 ] )
print ( tupla2 [ 2 ] )

print ( len ( tupla ) )
print ( 20 in tupla )
nueva = tupla + ( 50 , )
print ( nueva )

nacimiento = ( 15 , 3 , 2007 )
print ( "Día:" , nacimiento [ 0 ] )
print ( "Mes:" , nacimiento [ 1 ] )
print ( "Año:" , nacimiento [ 2 ] )
print ( "Fecha de nacimiento:" , nacimiento [ 0 ] , "/" , nacimiento [ 1 ] , "/" , nacimiento [ 2 ] )

hora_nacimiento = ( 8 , 11 , 36 )
print ( "Hora de nacimiento:" , hora_nacimiento [ 0 ] , ":" , hora_nacimiento [ 1 ] , ":" , hora_nacimiento [ 2 ] )

fecha_nacimiento = nacimiento + hora_nacimiento
print ( "Fecha y hora de nacimiento:" , fecha_nacimiento [ 0 ] , "/" , fecha_nacimiento [ 1 ] , "/" , fecha_nacimiento [ 2 ] , " " , fecha_nacimiento [ 3 ] , ":" , fecha_nacimiento [ 4 ] , ":" , fecha_nacimiento [ 5 ] )

materias = ( "Matemáticas" , "Física" , "Química" , "Historia" , "Fundamentos de programación" )
print ( "Materia 1:" , materias [ 0 ] )
print ( "Materia 5:" , materias [ -1 ] )
print ( "¿Fundamentos de progamación esta en la tupla?" , "Fundamentos de programación" in materias )
if "Fundamentos de programación" in materias :
    print ( "Si, Fundamentos de programación esta en la tupla" )
else :
    print ( "No, Fundamentos de programación no esta en la tupla" )

for materia in materias :
    if materia == "Fundamentos de programación" :
        print ( materia , "<-- Si, Fundamentos de programación esta en la tupla" )
    else :
        print ( materia , "<-- No, Fundamentos de programación no esta en la tupla" )

alumnos = ( )
alumnos = alumnos + ( input ( "Nombre del alumno:") , input ( "Edad del alumno:") , input ( "Carrera del alumno:") , input ( "Matricula del alumno:" ) )
print ( "Nombre \t\t Edad \t\t Carrera \t\t Matricula" )
print ( alumnos [ 0 ] , "\t" , alumnos [ 1 ] , "\t\t" , alumnos [ 2 ] , "\t\t\t" , alumnos [ 3 ] )
