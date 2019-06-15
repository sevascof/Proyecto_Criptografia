import base64 as b64

print("Cifrado y descifrado Base64 \nMenu principal")
while 1:
	opc = int(input(" 1\tCifrar\n 2\tDescifrar\n 3\tSalir \nIntroduzca 1, 2 o 3 para continuar: "))

	if opc is 1:
		inp = int(input(" 1\tIngresar texto\n 2\tIngresar archivo \nIntroduzca 1 o 2 para continuar: "))
		if inp is 1:
			txt = input("Introduzca el texto a cifrar: ")
		elif inp is 2:
			msg = open(input("Introduzca el nombre del archivo a cifrar: "))
			txt = msg.read()
		else:
			print("Introduzca un valor valido")
		base = b64.b64encode(txt.encode("utf-8"))
	elif opc is 2:
		inp = int(input(" 1\tIngresar texto\n 2\tIngresar archivo \nIntroduzca 1 o 2 para continuar: "))
		if inp is 1:
			txt = input("Introduzca el texto a descifrar: ")
		elif inp is 2:
			msg = open(input("Introduzca el nombre del archivo a descifrar: "))
			txt = msg.read()
		else:
			print("Introduzca un valor valido")
		base = b64.b64decode(txt.encode("utf-8"))
	elif opc is 3:
		break
	else:
		print("Introduzca una opcion valida")

	print('\n' + str(base, "utf-8"))
	input("\nPresione Enter para volver al menu principal")