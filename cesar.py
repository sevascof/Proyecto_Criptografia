# SUSTITUCION MONOALFABETICA POR DESPLAZAMIENTO
# -*- coding: utf-8 -*-

from heapq import nlargest
import time
start = time.time()

lang = "español"

if lang is "ingles":
  abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
elif lang is "español":
  abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

plain = "nacio una flor a orillas de una fuente mas pura que la flor de la ilusion y un huracan tronchola de repente cayendo al agua la preciosa flor"

clave = 'y'

print("A cifrar: " + plain + ". Con clave: " + clave)

plain = plain.lower()
c_msg = []

# Eliminacion de espacios y caracteres especiales en el mensaje
for i in range(0, len(plain)):
  if plain[i] in abc:
    c_msg.append(plain[i])

# Conteo de letras
conteo = {}
for i in range(0, len(abc)):
  conteo[abc[i]] = c_msg.count(abc[i]) # /len(c_msg)*100

# Encontrando los mas repetidos con 'nlargest' de lib 'heapq'
most_rep = nlargest(5, conteo, key = conteo.get)
print("Las letras que mas se repiten en el criptograma son:")
for v in most_rep: print(v, '>', conteo.get(v), "veces")

# Cifrado
ind_crypto = []
crypto = []
for i in range(0, len(c_msg)):
  ind_crypto.append((abc.index(c_msg[i]) + abc.index(clave)) % (len(abc)))

for i in range(0, len(ind_crypto)) :
  crypto.append(abc[ind_crypto[i]])

print("Mensaje cifrado: \n"+''.join(crypto))

end = time.time()
print("\nCodigo ejecutado en {} segundos".format(end-start))

# Descifrado
dec = []
msg = []
for i in range(len(crypto)):
	dec.append((abc.index(crypto[i]) - abc.index(clave)) % len(abc))
	msg.append(abc[dec[i]])

print("El mensaje descifrado es: " + ''.join(msg))

"""
Cybergrafia:
https://www.geeksforgeeks.org/switch-case-in-python-replacement/
http://letterfrequency.org/letter-frequency-by-language/
"""