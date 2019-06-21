# -*- coding: utf-8 -*-
import mathill_util as mt
import time


def key_val(key):
    valida = False
    primera = True
    while not valida:

        if primera:
            primera = False
        else:
            key = str(input('Ingrese la llave: '))

        key_mat = mt.mat_key_ascii(key)
        det = mt.determinant_fast(key_mat)
        inv = mt.inv_mod_mul(det, 256)

        if isinstance(det, int) is True:
            if ((det % 256) != 0) and inv:
                if (len(key) >= 5 and len(key) <= 9) or (len(key) >= 17 and len(key) <= 25):
                    valida = True
            else:
                print("La llave no es valida por las siguientes razones:\n(1) La matriz generada por la llave no debe ser singular\n(2) Debe existir una matriz inversa modular\n(3) La llave debe contener entre 5 y 9 caracteres o entre 17 y 25 caracteres\nLa llave no cumple con los requisitos indicados, por favor ingrese otra llave\n")
    print("Llave valida")
    return key_mat

def ord_msg(msg):
    num = []
    for i in range(len(msg)):
        num.append([])
        for j in range(len(msg[i])):
            num[i].append(ord(msg[i][j]))
    return num

def hex2dec_sep(txt, sep):
    i = 0
    lst = []
    dec = []
    while i < len(txt):
        if txt[i] is not sep:
            lst.append(txt[i] + txt[i + 1])
            i += 1
        i += 1
    for j in range(len(lst)):
        dec.append(int(lst[j], 16))
    return dec

def cif(msg_in, key, out_file):

    key_mat = key_val(key)

    start = time.time()
    print("Cifrando...")
    separador = ' '
    padding = '0'
    sub_vec = list(mt.divide_str(msg_in, len(key_mat), padding))
    num = ord_msg(sub_vec)
    
    crypto = []
    for i in range(len(num)):
        crypto.append([])
        crypto[i] = mt.mat_x_vec(key_mat, num[i])

    tmp = []
    cif_hex = []
    for i in range(len(crypto)):
        for j in range(len(crypto[i])):
            tmp.append(crypto[i][j] % 256)
            
    for i in range(len(tmp)):
        cif_hex.append(str(format(tmp[i], '02x')) + separador)

    salida = open(out_file, 'w')
    salida.write(''.join(cif_hex))
    salida.close()

    end = time.time()
    print("Mensaje cifrado en {} segundos".format(end - start))

    return 1

def dec(msg_in, key, out_file):

    key_mat = key_val(key)

    start = time.time()
    print("Descifrando...")
    inversa = mt.inv_key(key_mat, 256)
    separador = ' '
    num_lst = hex2dec_sep(msg_in, separador)
    sub_vec = list(mt.divide_num(num_lst, len(key_mat)))

    plain = []
    for i in range(len(sub_vec)):
        plain.append([])
        plain[i] = mt.mat_x_vec(inversa, sub_vec[i])

    dec_txt = []
    for i in range(len(plain)):
        for j in range(len(plain[i])):
            dec_txt.append(chr(plain[i][j] % 256))

    pad_dec = ''.join(dec_txt)
    salida = open(out_file, 'w')
    salida.write(pad_dec.strip('0'))
    salida.close()

    end = time.time()
    print("Mensaje descifrado en {} segundos".format(end - start))

    return 1

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