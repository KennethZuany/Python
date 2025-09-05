#MINUTOS POR PAUSA
pausa_minutos = 15

# Datos Usuario
nombre = input ("Nombre:")
origen = input ("Ciudad de salida:")
destino = input ("Ciudad de destino:")

# Datos Viaje
distancia = input ("Distancia entre ciudad de salida y ciudad destino (kilometros):")
velocidad = input ("Velocidad promedio estimada (km/h):")
precio_gas = input ("Precio por litro de gasolina:")
rendimiento = input ("Rendimiento del vehiculo (km/l):")
dinero_disponible = input ("Dinero disponible para el viaje: ")

#Conversiones
velocidad_numero = int (velocidad)
distancia_numero = int (distancia)
precio_gas_numero = int (precio_gas)
rendimiento_numero = int (rendimiento)
dinero_disponible_numero = int(dinero_disponible)

# Calculos
tiempo = distancia_numero / velocidad_numero
tiempo_minutos = int (tiempo) * 60
horas = int (tiempo_minutos // 60)
gas_requerida = distancia_numero / rendimiento_numero
dinero_requerido = gas_requerida * precio_gas_numero
precio_gas_requerida = gas_requerida * precio_gas_numero

# Print
print ("\n \n \n")
print ("Hola,\n", nombre, "\n Este es tu resumen del viaje")
print ("Vas a salir de \n", origen, "\ny vas a \n", destino)
print ("Tiempo estimado sin pausas: \n", horas, "h", tiempo_minutos, "m")
print ("Tiempo estimado con dos paradas de 15 minutos cada una: \n", horas, "h", pausa_minutos, "m")
print ("Gasolina requerida (litros): \n", gas_requerida)
print ("Dinero necesario para gasolina: \n", dinero_requerido)

if  precio_gas_requerida > dinero_disponible_numero:
    print("¡¡¡NO TIENES SUFICIENTE DINERO!!!")
else:
    print("Tienes el dinero necesario")