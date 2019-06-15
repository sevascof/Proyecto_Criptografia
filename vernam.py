def cif_vernam(msg, key):
    cif = []
    for x in msg:
        cif.append(bin(ord(x) ^ ord(key)))
    return cif


def dec_vernam(cif, key):
    dec = []
    for x in cif:
        dec.append(chr(int(x, 2) ^ ord(key)))
    return dec


msg = input("Introduzca el mensaje a cifrar: ")
key = input("Introduzca 1 caracter a usar como clave: ")
print("El mensaje a cifrar es '{}' con clave '{}'".format(msg, key))
cif = cif_vernam(msg, key)
dec = dec_vernam(cif, key)

print("El mensaje cifrado es:")
for x in cif:
    print(x)
print("El mensaje descifrado es: " + ''.join(dec))
input("Presione 'Enter' para finalizar")