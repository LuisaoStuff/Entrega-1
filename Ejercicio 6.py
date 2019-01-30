#	Ejercicio 6
#	Examen tablas de multiplicar

limite=int(input("\n		Numero de preguntas:	"))

#	Validación preguntas
while limite<=0:
	print("\n		El número de preguntas debe ser al menos 1.")
	limite=int(input("		Numero de preguntas:	"))	

correctas=0

#	Prueba

for cont in range(0,limite):

	from random import randint
	a = randint(2, 10)
	b = randint(2, 10)

	print("\n		¿Cuánto es",a,"multiplicado por",b,end="?	")
	c=int(input())

	if a*b==c:	#Respuesta correcta
		print("		¡Respuesta correcta!")
		correctas=correctas+1
	else:		#Respuesta incorrecta
		print("		¡Respuesta incorrecta!")

#	Cálculo de la nota

nota=(correctas/limite)*10
nota=round(nota,2)
print("\n			Has sacado un",nota)

if nota==10:
	print("			   ¡Enhorabuena!")
elif nota==0:

	import time
	import webbrowser
	print("		    ¡No has acertado ni una!")
	time.sleep(2)
	webbrowser.open('https://pics.me.me/Facebook-911ed1.png')

print("\n")