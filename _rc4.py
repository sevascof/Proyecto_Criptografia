# -*- coding: utf-8 -*-
import time


def round_up(n):
    res = int(n)
    return res if res == n or n < 0 else res + 1


def sec_msg(msg):  # Seccionamiento del mensaje en grupos de 256
    sec = []
    i = j = cont = 0
    while i < round_up(len(msg) / 256):
        sec.append([])
        while j < (cont + 256):
            if j < len(msg):
                sec[i].append(msg[j])
            else:
                sec[i].append('0')
            j += 1
        i += 1
        cont += 256

    return sec


def vec_key(key):  # Vector clave T
    i = j = 0
    t = []
    while i < 256:
        for j in range(len(key)):
            if i < 256:
                t.append(ord(key[j]))
            i += 1

    return t


def KSA(t):  # Algoritmo KSA
    i = j = 0
    s = list(range(0, 256, 1))
    for i in range(len(s)):
        j = (j + s[i] + t[i]) % 256
        tmp1 = s[i]
        tmp2 = s[j]
        s[i] = tmp2
        s[j] = tmp1

    return s


def PRGA(sec, s):  # Algoritmo PRGA
    key_stream = []
    for sub_msg in range(len(sec)):
        key_stream.append([])
        i = j = k = tmp1 = tmp2 = 0
        while k < len(sec[sub_msg]):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            tmp1 = s[i]
            tmp2 = s[j]
            s[i] = tmp2
            s[j] = tmp1
            t = (s[i] + s[j]) % 256
            key_stream[sub_msg].append(s[t])
            k += 1

    return key_stream


def XOR(sec, key_stream, option):  # Funcion Exclusive OR
    msg = []
    for i in range(len(sec)):
        msg.append([])
        for j in range(len(sec[i])):
            if option:
                msg[i].append(ord(sec[i][j]) ^ key_stream[i][j])
            elif not option:
                msg[i].append(sec[i][j] ^ key_stream[i][j])

    return msg


def cif(msg_in, key, out_file):
    start = time.time()
    print("Cifrando...")
    separador = ' '

    sec = sec_msg(msg_in)
    t = vec_key(key)
    s = KSA(t)
    key_stream = PRGA(sec, s)
    cif_xor = XOR(sec, key_stream, 1)

    cif_hex = []
    for i in range(len(cif_xor)):
        for j in range(len(cif_xor[i])):
            cif_hex.append(str(format(cif_xor[i][j], '02x') + separador))

    salida = open(out_file, 'w', encoding="ISO-8859-1")
    salida.write(''.join(cif_hex))
    salida.close()

    end = time.time()
    print("Mensaje cifrado en {} segundos".format(end - start))

    return 1


def dec(msg_in, key, out_file):
    start = time.time()
    print("Descifrando...")
    separador = ' '

    cifr = []
    i = 0
    while i < len(msg_in):
        if msg_in[i] is not separador:
            cifr.append(msg_in[i] + msg_in[i + 1])
            i += 1
        i += 1

    msg_dec = []
    for i in range(len(cifr)):
        msg_dec.append(int(cifr[i], 16))

    sec = sec_msg(msg_dec)
    t = vec_key(key)
    s = KSA(t)
    key_stream = PRGA(sec, s)
    dec = XOR(sec, key_stream, 0)

    dec_txt = []
    for i in range(len(dec)):
        for j in range(len(dec[i])):
            dec_txt.append(chr(dec[i][j]))

    pad_dec = ''.join(dec_txt)
    salida = open(out_file, 'w', encoding="ISO-8859-1")
    salida.write(pad_dec.strip('0'))
    salida.close()

    end = time.time()
    print("Mensaje descifrado en {} segundos".format(end - start))


"""___ ___ ___ --- --- --- ___ ___ ___ --- --- --- ___ ___ ___ --- --- ---"""

# flag = False
# f = False
# while not flag:
#     _choice = str(input('Ingrese -c para cifrar o -d para descifrar: '))

#     if _choice is 'c':
#         while not f:
#             try:
#                 _arch = str(input('-i '))
#                 _file = open(_arch, 'r')
#                 _message = _file.read()
#                 f = True
#             except FileNotFoundError:
#                 print("Archivo no encontrado. Por favor ingrese un archivo valido")
#         _key = str(input('-k '))
#         _output = str(input('-o '))
#         cif(_message, _key, _output)
#         flag = True
#     elif _choice is 'd':
#         while not f:
#             try:
#                 _arch = str(input('-i '))
#                 _file = open(_arch, 'r')
#                 _message = _file.read()
#                 f = True
#             except FileNotFoundError:
#                 print("Archivo no encontrado. Por favor ingrese un archivo valido")
#         _key = str(input('-k '))
#         _output = str(input('-o '))
#         dec(_message, _key, _output)
#         flag = True
#     else:
#         print("Por favor ingrese una bandera valida")
#         flag = False
# print("Codigo ejecutado exitosamente")
