# Sistema de registro en gimnasio

# Paso 1: Preguntar cuántos clientes se registrarán
num_clientes = input ( "Numero de clientes: " )
if int ( num_clientes ) <= 0 :
    num_clientes = input ( "Ingresa un numero valido: " )
num_clientes = int ( num_clientes )

# Paso 2: Variables acumuladoras
ingresos_totales = 0
suma_edades = 0
contador_clientes = 0
resumen_clientes = ""

membresia_basica = 0
membresia_premium = 0
membresia_vip = 0

edad_menor = 1000
nombre_menor = ""
edad_mayor = -1
nombre_mayor = ""

# Paso 3: Ciclo para registrar a cada cliente
i = 1
while i <= num_clientes :
    print ( "\n--- Registro del cliente #" , i , "---" )

    nombre = input ( "Nombre: " )
    edad = input ( "Edad: " )
    if int ( edad ) <= 0 :
        edad = input ( "Invalido. Edad: " )
    edad = int ( edad )
    tipo_persona = input ( "Tipo de persona (estudiante/profesor/ninguno): " )
    if tipo_persona == "estudiante" :
        print ( "Elegiste estudiante" ) 
    elif tipo_persona == "profesor" :
        print ( "Elegiste profesor " )
    elif tipo_persona == "ninguno" :
        print ( "Elegiste ninguno" )
    else :
        tipo_persona = print ( "Invalido. Tipo de persona: " )
    membresia = input ( "Tipo de membresía (basica/premium/vip): " )
    if membresia == "basica" :
        print ( "Elegiste membresia basica" )
    elif membresia == "premium" :
        print ( "Elegiste membresia premium" )
    elif membresia == "vip" :
        print ( "Elegiste membresia vip" )
    else :
        membresia = input ( "Invalido.\nTipo de membresia: " )

    if edad < 18 and membresia != "basica" :
        print ( "Invalido." )
        continue
    if edad < 18 :
        precio = 200
    elif edad <= 40 :
        if membresia == "básica" :
            precio = 300
        elif membresia == "premium" :
            precio = 500
        else :
            precio = 700
    elif edad <= 59 :
        if membresia == "básica" :
            precio = 250
        elif membresia == "premium" :
            precio = 450
        else :
            precio = 600
    else :
        if membresia == "básica" :
            precio = 250
        elif membresia == "premium" :
            precio = 450
        else:
            precio = 600
        precio = precio * 0.8

    # Descuentos por tipo de persona
    if tipo_persona == "estudiante" :
        precio = precio * 0.85
    elif tipo_persona == "profesor" :
        precio = precio * 0.90

    # Acumuladores
    ingresos_totales = ingresos_totales + precio
    suma_edades = suma_edades + edad
    contador_clientes = contador_clientes + 1

    if membresia == "basica" :
        membresia_basica = membresia_basica + 1
    elif membresia == "premium" :
        membresia_premium = membresia_premium + 1
    else :
        membresia_vip = membresia_vip + 1

    # Registrar cliente más joven y mayor
    if edad < edad_menor :
        edad_menor = edad
        nombre_menor = nombre
    if edad > edad_mayor :
        edad_mayor = edad
        nombre_mayor = nombre

    # Concatenar al resumen
    resumen_clientes = resumen_clientes + "Nombre: " + nombre + " | Edad: " + str ( edad ) + " | Membresía: " + membresia + " | Pago: $" + str ( precio ) + "\n"

    i = i + 1

# Paso 4: Imprimir reporte final
print ( "\n============================" )
print ( "  REPORTE FINAL - GIMNASIO" )
print ( "============================" )

print ( "\nTotal de clientes:" , contador_clientes )

if contador_clientes > 0 :
    print ("\nResumen de clientes:" )
    print ( resumen_clientes )

    promedio = suma_edades / contador_clientes
    print ("-------------------------------------")
    print ( "Total de ingresos:" , ( ingresos_totales ) )
    print ( "Promedio de edad:" , ( promedio ) , "años" )
    print ( "Clientes por membresía - Basica:" , membresia_basica , " Premium:" , membresia_premium , " VIP:" , membresia_vip )
    print ( "Cliente más joven:" , nombre_menor , "con" , edad_menor , "años" )
    print ( "Cliente de mayor edad:" , nombre_mayor , "con" , edad_mayor , "años" )
else :
    print ( "No se registraron clientes." )