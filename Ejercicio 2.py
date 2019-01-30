#	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos
#	años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede
#	mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba
#	la frase en singular.

año1=int(input("\n		¿En qué año estamos?	"))		#Introducción de valores
año2=int(input("		Dime un año cualquiera:	"))


if abs(año2-año1)==1:			#Respuesta singular
	if año2>año1:
		print("\n		Falta aún un año.\n")
	else:
		print("\n		Ha pasado un año.\n")
elif año2>año1:					#Respuesta plural
	diferencia=año2-año1
	print("\n		Para llegar al año ",año2,"faltan ",diferencia," años.\n")
elif año2<año1:
	diferencia=abs(año2-año1)
	print("\n		Desde el año ",año1," han pasado ",diferencia," años.\n")
elif año2==año1:				#Valores iguales
	print("\n		Son el mismo año.\n")