#	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.


num=int(input("\n		Este programa calcula los divisores del número introducido.\n		Numero:	"))

while num<=0:		#	Validación para que num sea mayor que 0
	num=int(input("\n		¡El número debe ser mayor que cero!\n		Numero:	"))


print("		Los divisores de ",num," son:\n		|",num,end="|")
for Divisor in range(num//2,0,-1):
	
	if num%Divisor==0:
		print(Divisor,end="|")
	Divisor=Divisor+1

print("\n")

#	He usado end="caracter" para evitar los saltos de linea de "print" y mostrar
#	todos los divisores en una sola linea.