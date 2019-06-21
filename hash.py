import hashlib

print("<<<___Calculo de hash MD5___>>>")
f = False
while not f:
	try:
		print(hashlib.md5(open(input('Ingrese la direccion del archivo: '), 'rb').read()).hexdigest())
		f = True
	except FileNotFoundError:
		print("Archivo no encontrado. Por favor ingrese correctamente la direccion delarchivo ")