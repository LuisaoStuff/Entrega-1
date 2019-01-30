#	Escriba un programa que pregunte cuántos números se van a introducir, pida esos 
#	números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

limite=int(input("\n		¿Cuántos números va a introducir?	"))

#	Validación
while limite<=0:
	limite=int(input("\n		¡Eso es imposible!\n		¿Cuántos números va a introducir?	"))

numero=int(input("		Introduzca un número:	"))
print("\n")
for cont in range(0,limite):	# Bucle "for" para introducir números hasta llegar al limite establecido
	print("		Escriba un número mayor que ",numero,end=":	")
	otro=int(input())
	if otro<numero:
		print("\n		¡",otro," no es mayor que ",numero,"!\n")

print("\n\n		Fin del programa\n")