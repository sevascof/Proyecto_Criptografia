import math
import random
import time
from heapq import nlargest

START = time.time()

print(
    "\nSi el mensaje descifrado carece de coherencia por favor corra el programa nuevamente, esto es debido a la seleccion aleatoria de las distancias escogidas para realizar el calculo del MCD en adicion con la posibilidad de error de las Hipotesis planteadas\n")

FILE = open('TAREA1.txt', 'r')
TXT = FILE.read()

# Abecedarios
LANG = "español"

if LANG is "ingles":
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    LAN_FREQ = ['e', 't', 'a']
elif LANG is "español":
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    LAN_FREQ = ['e', 'a', 'o']

# Eliminando caracteres innecesarios
J_TXT = []
for i in range(len(TXT)):
    if TXT[i].lower() in ABC:
        J_TXT.append(TXT[i].lower())

MESSAGE = ''.join(J_TXT)

# Distancia entre grupos
DISTANCIAS = {}
# Tomado de {1} range(a, a+1): define el tamaño 'a' de los grupos a buscar
for seqLen in range(4, 6):
    for seqStart in range(len(MESSAGE) - seqLen):
        seq = MESSAGE[seqStart:seqStart + seqLen]
        for i in range(seqStart + seqLen, len(MESSAGE) - seqLen):
            if MESSAGE[i: i + seqLen] == seq:
                if seq not in DISTANCIAS:
                    DISTANCIAS[seq] = []
                DISTANCIAS[seq].append(i - seqStart)

# print(DISTANCIAS)

# MCD distancias
TMP1 = DISTANCIAS[random.choice(list(DISTANCIAS.keys()))]
TMP2 = DISTANCIAS[random.choice(list(DISTANCIAS.keys()))]
TMP3 = DISTANCIAS[random.choice(list(DISTANCIAS.keys()))]
TMP4 = DISTANCIAS[random.choice(list(DISTANCIAS.keys()))]

TAM_CLAVE = math.gcd(math.gcd(TMP1[0], TMP2[0]), math.gcd(TMP3[0], TMP4[0]))
print("El tamaño de la clave es: {}".format(TAM_CLAVE))

# Division de texto
SUB_CRYPTOS = []
JOTAS = 0
while JOTAS < TAM_CLAVE:
    SUB_CRYPTOS.append([])
    for corrimiento in range(0, len(MESSAGE) - TAM_CLAVE, TAM_CLAVE):
        SUB_CRYPTOS[JOTAS].append(MESSAGE[corrimiento + JOTAS])
    print("jotas[{}] = {}, {}, {}, ...".format(JOTAS, SUB_CRYPTOS[JOTAS][0], SUB_CRYPTOS[JOTAS][1], SUB_CRYPTOS[JOTAS][2]))
    JOTAS += 1

SUBS = [[]] * TAM_CLAVE
for k in range(len(SUB_CRYPTOS)):
    SUBS[k] = ''.join(SUB_CRYPTOS[k])

# print(SUBS)

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


# Mas repetidos en jotas
MAS_REP_SUBS = []
for i in range(len(SUBS)):
    MAS_REP_SUBS.append([])
    MAS_REP_SUBS[i] = conteo(ABC, SUBS[i])

# Ubicacion en ABC
POSICIONES = []
for i in range(len(SUBS)):
    POSICIONES.append([])
    for j in range(len(SUBS[i])):
        POSICIONES[i].append(ABC.index(SUBS[i][j]))


# Hipotesis Ci = (Mi + k) mod(Ta)
def hipo(Ci, Mi, abc):
    mod = len(abc)
    for k in range(mod):
        if (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[1])):
            print("Hipotesis 1 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[2])):
            print("Hipotesis 2 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[2]) + k) % mod) is abc.index(Ci[1])):
            print("Hipotesis 3 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[2]) + k) % mod) is abc.index(Ci[2])):
            print("Hipotesis 4 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[1])) and (
                ((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[0])):
            print("Hipotesis 5 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[1])) and (
                ((abc.index(Mi[2]) + k) % mod) is abc.index(Ci[0])):
            print("Hipotesis 6 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[2])) and (
                ((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[0])):
            print("Hipotesis 7 " + abc[k])
            return k
        elif (((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[2])) and (
                ((abc.index(Mi[2]) + k) % mod) is abc.index(Ci[0])):
            print("Hipotesis 8 " + abc[k])
            return k
        elif (((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[1])):
            print("Hipotesis 9 " + abc[k])
            return k
        elif (((abc.index(Mi[1]) + k) % mod) is abc.index(Ci[0])) and (
                ((abc.index(Mi[0]) + k) % mod) is abc.index(Ci[2])):
            print("Hipotesis 10 " + abc[k])
            return k


# Descubrir clave
LETRAS_CLAVE = []
for i in range(TAM_CLAVE):
    LETRAS_CLAVE.append(ABC[hipo(MAS_REP_SUBS[i], LAN_FREQ, ABC)])

CLAVE = ''.join(LETRAS_CLAVE)
print("La clave usada para cifrar el mensaje fue: '{}'".format(CLAVE))

# Descifrado
RESULTADO = []
MSG_DESCIF = []
for i in range(len(MESSAGE)):
    RESULTADO.append((ABC.index(MESSAGE[i]) - ABC.index(CLAVE[i % TAM_CLAVE])) % len(ABC))
    MSG_DESCIF.append(ABC[RESULTADO[i]])
print("\nEl mensaje descifrado es: " + ''.join(MSG_DESCIF))

# Medicion temporal
END = time.time()
print("\nCódigo ejecutado en {} segundos".format(END - START))

"""
Referencias
{0} https://inventwithpython.com/cracking/chapter20.html
{1} https://inventwithpython.com/hacking/chapter21.html
{2} https://cryptii.com/pipes/vigenere-cipher
{3} http://artemisa.unicauca.edu.co/~samador
"""