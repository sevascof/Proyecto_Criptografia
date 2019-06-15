import time

a = int(input("El valor de 'a' es: "))
mod = int(input("El valor de 'Ta' es: "))

def inv_mod_mul(a, mod):
	for i in range(mod):
		if (a*i)%mod is 1:
			return i

print("El inverso modular es: {}".format(inv_mod_mul(a,mod)))
input("Presione 'Enter' para terminar")