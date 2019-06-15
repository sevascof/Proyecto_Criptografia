from heapq import nlargest

txt = "lkas alskd asidn asodinaslkdna pajd aslkda dasdjas aspdmas dlidf rsfpijad fonf doinw iwem  lw inwef eiwe wefjnwefkwojef  weoifnwe fwejnfw oeinfwe fwelk we"

# Abecedarios
lang = "español"

if lang is "ingles":
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lan_freq = ['e', 't', 'a']
elif lang is "español":
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lan_freq = ['e', 'a', 'o']

# Eliminando espacios
j_txt = []
for i in range(len(txt)):
    if txt[i] is not ' ':
        j_txt.append(txt[i].lower())

message = ''.join(j_txt)

# Analisis de frecuencia
def conteo(abc, msg):
  conteo = {}
  for i in range(len(abc)):
    conteo[abc[i]] = msg.count(abc[i])
  most_rep = nlargest(3, conteo, key=conteo.get)
  print("Las letras que mas se repiten son:")
  for v in most_rep:
    print(v, '>', conteo.get(v), "veces")
  return most_rep

print(conteo(abc, message))