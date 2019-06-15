import time
start = time.time()

lang = "español"

if lang is "ingles":
  abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
elif lang is "español":
  abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

plain = "DWÑSDWFSBOUÑDHYDZOAHQMÑEÑEYLOEMSCINUHJMSQIFLDKOFCSWKHTÑHFVUEZCNWFYCKZZUFYEHVÑIHMTVYMÑJZXEEUSZFVTAGWUBGWUBFVTAEUSZJZXE"
clave = "zeus"

#print("A cifrar: " + plain + "\nCon clave: " + clave)

c_msg = []
c_key = []

# Eliminacion de espacios y caracteres especiales en el mensaje y clave
for i in range(len(plain)):
  if plain[i].lower() in abc:
    c_msg.append(plain[i].lower())

for i in range(len(clave)):
  c_key.append(clave[i].lower())

# CIPHER
ind_crypto = []
crypto = []
i = j = 0

for i in range(len(c_msg)):
  ind_crypto.append((abc.index(c_msg[i]) + abc.index(c_key[i%len(c_key)])) % (len(abc)))
for i in range(len(ind_crypto)) :
  crypto.append(abc[ind_crypto[i]])

cif = ''.join(crypto)
#print("Cifrado: " + cif)

# DECIPHER
cifr = cif
cifrado = []
for i in range(len(cifr)):
  if cifr[i] in abc:
    cifrado.append(cifr[i].lower())

cifrado = plain.lower()

print("Mensaje cifrado: {} con clave {}\n".format(cifrado, clave))

key = clave
d_pos = []
decif = []
for i in range(len(cifrado)):
  d_pos.append(abc.index(cifrado[i]))
for i in range(len(d_pos)):
  decif.append(abc[(d_pos[i] - abc.index(key[i%len(key)]))%len(abc)])

dec = ''.join(decif)
print("Mensaje Descifrado: " + dec + "\n")

end = time.time()
print("Codigo ejecutado en {} ms".format(1000*(end-start)))