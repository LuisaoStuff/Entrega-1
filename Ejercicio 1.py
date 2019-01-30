#	Escriba un programa que pida dos números enteros y que calcule su división, escribiendo 
#	si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta
#	que no se puede dividir por cero.

dividendo=int(input("\n		Introduzca el número a dividir:	"))	#Introducción de valores
divisor=int(input("		Introduzca el divisor:	"))

if divisor==0:		#Si el divisor es 0 muestra un error por teclado
	print("\n		¡No se puede dividir por 0!")
else:
	resto=dividendo%divisor
	if resto==0:	#Si el resto es 0, solo muestra el cociente
		cociente=dividendo//divisor
		print("\n		La división es exacta. El cociente es:	",cociente)
	else:			#Si el resto es distinto de 0, muestra el cociente y el resto
		cociente=dividendo//divisor
		print("\n		La división no es exacta. \n		El cociente es:	",cociente,"\n		Y el resto es:	",resto,"\n")