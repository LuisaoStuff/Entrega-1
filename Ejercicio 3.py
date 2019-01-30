#	Escriba un programa que pida tres números y que escriba si son los tres 
#	iguales, si hay dos iguales o si son los tres distintos.

print("\n		Este programa comprueba las equivalencias de los tres\n		números introducidos:")
A=float(input("		Número 1:	"))
B=float(input("		Número 2:	"))		#Introducción de números
C=float(input("		Número 3:	"))

if A==B and B==C:			#Si A=B y B=C quiere decir que son todos iguales.
	print("\n		Los tres números son iguales.\n")
elif A==B or A==C or B==C:	#Si A=B o A=C o B=C quiere decir que hay dos numeros iguales.
	print("\n		Ha escrito uno de los números dos veces.\n")
elif A!=B and B!=C:			#Si A es distinto de B y B es distinto de C, todos son distintos.
	print("\n		Los tres números que ha escrito son distintos.\n")
