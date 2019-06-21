import argparse
import os
import _rc4
import _mth

parser = argparse.ArgumentParser()

parser.add_argument("-rc4", "--rc4", help="Algoritmo RC4", action="store_true")
parser.add_argument("-mth", "--mth", help="Algoritmo de matrices Hill", action="store_true")
parser.add_argument("-i", "--Archivo", help="Nombre del archivo a cifrar", default=os.getcwd(), required=False)
parser.add_argument("-a", "--ayuda", action="store_true", help="Ayuda en pantalla")
parser.add_argument("-c", "--Cifrado", action="store_true", help="Uso de algoritmo para cifrar archivo")
parser.add_argument("-d", "--Descifrado", action="store_true", help="Uso de algoritmo para descifrar archivo")
parser.add_argument("-k", "--llave", help="Llave con la que se ha de cifrar o descifrar el mensaje")
parser.add_argument("-o", "--salida", help="Nombre del archivo de salida")

args = parser.parse_args()

if args.rc4 and args.ayuda:
    print("""
             ______________________________UNIVERSIDAD AUTONOMA DE OCCIDENTE______________________________
            |------------------------------Algortirmo RC4 y Matrices de Hill------------------------------|
            |                                                                                             |
            | Sintaxis para algoritmo RC4.                                                                |
            |     >>> python Proyecto_final_vga.py -rc4 <Accion> -i <Entrada> -k <Clave> -o <Salida>      |
            |                                                                                             |
            | Accion:                                                                                     |
            |     -c: Cifrado de archivo                                                                  |
            |	  -d: Decifrado de archivo                                                                |
            |                                                                                             |
            | Entrada: Debe ser un archivo de texto plano que se desee cifrar o Decifrar                  |
            |                                                                                             |
            |     Ejemplo: baldor.txt                                                                     |
            |                                                                                             |
            | Clave: La clave debe estar compuesta por caracteres imprimibles y su tamaño debe ser        |
            |        menor o igual a 256 caracteres.                                                      |
            |                                                                                             |
            |        Ejemplo: P@ss0123                                                                    |
            |                                                                                             |
            | Ejemplo de uso del algoritmo RC4:                                                           |
            |                                                                                             |
            |     Cifrar: python Proyecto_final_vga.py -rc4 -c -i baldor.txt -k P@ss0123 -o baldor.cif    |
            |                                                                                             |
            |     Decifrar: python Proyecto_final_vga.py -rc4 -d -f baldor.cif -k P@ss0123 -o baldor.dec  |
            |                                                                                             |
            | Elaborado por: Sebastian Vasco Florez sebastian.vasco@uao.edu.co                            |
            |                Marco Tulio Giron      marco.giron@uao.edu.co                                |
            |                                                                                             |
            | Docente:       Siler Amador Donado    samador@unicauca.edu.co                               |
            |                                                                                             |
            |                                                 Especializacion en Seguridad Informatica    |
            |                                                          Certificados y Firmas digitales    |
            |                                                                                 21/06/19    |
            |_____________________________________________________________________________________________|
            """)

elif args.mth and args.ayuda:
    print("""
             ______________________________UNIVERSIDAD AUTONOMA DE OCCIDENTE______________________________
            |------------------------------Algortirmo RC4 y Matrices de Hill------------------------------|
            |                                                                                             |
            | Sintaxis para algoritmo Matrices de Hill.                                                   |
            |     >>> python Proyecto_final_vga.py -mth <Accion> -i <Entrada> -k <Clave> -o <Salida>      |
            |                                                                                             |
            | Accion:                                                                                     |
            |     -c: Cifrado de archivo                                                                  |
            |     -d: Decifrado de Archivo                                                                |
            |                                                                                             |
            | Entrada: Debe ser un archivo de texto plano que se desee cifrar o Decifrar                  |
            |                                                                                             |
            |     Ejemplo: baldor.txt                                                                     |
            |                                                                                             |
            | Clave: La clave debe estar compuesta por caracteres imprimibles y debe cumplir con las      |
            |        siguientes condiciones:                                                              |
            |        1) La matriz generada por la clave no debe ser singular                              |
            |        2) Debe existir una matriz inversa modular                                           |
            |        3) La clave debe contener entre 5 y 9 caracteres o entre 17 y 25 caracteres          |
            |        Nota: Los puntos 1) y 2) seran calculados automaticamente                            |
            |                                                                                             |
            |        Ejemplo: P@ss0123                                                                    |
            |                                                                                             |
            | Ejemplo de uso del algoritmo de Matrices de Hill:                                           |
            |                                                                                             |
            |     Cifrar: python Proyecto_final_vga.py -mth -c -i baldor.txt -k P@ss0123 -o baldor.cif    |
            |                                                                                             |
            |     Decifrar: python Proyecto_final_vga.py -mth -d -f baldor.cif -k P@ss0123 -o baldor.dec  |
            |                                                                                             |
            | Elaborado por: Sebastian Vasco Florez sebastian.vasco@uao.edu.co                            |
            |                Marco Tulio Giron      marco.giron@uao.edu.co                                |
            |                                                                                             |
            | Docente:       Siler Amador Donado    samador@unicauca.edu.co                               |
            |                                                                                             |
            |                                                 Especializacion en Seguridad Informatica    |
            |                                                          Certificados y Firmas digitales    |
            |                                                                                 21/06/19    |
            |_____________________________________________________________________________________________|
            """)

elif args.rc4 and args.Cifrado and args.Archivo and args.llave and args.salida:
    file_in=open(args.Archivo,"r",encoding="ISO-8859-1").readline()
    _rc4.cif(file_in, args.llave, args.salida)

elif args.rc4 and args.Descifrado and args.Archivo and args.llave and args.salida:
    file_in=open(args.Archivo,"r",encoding="ISO-8859-1").readline()
    _rc4.dec(file_in, args.llave, args.salida)

elif args.mth and args.Cifrado and args.Archivo and args.llave and args.salida:
    file_in=open(args.Archivo,"r",encoding="ISO-8859-1").readline()
    _mth.cif(file_in, args.llave, args.salida)

elif args.mth and args.Descifrado and args.Archivo and args.llave and args.salida:
    file_in=open(args.Archivo,"r",encoding="ISO-8859-1").readline()
    _mth.dec(file_in, args.llave, args.salida)

else:
	print("Por favor ingrese:\n>>> python Proyecto_final_vga.py -h\nPara visualizar la ayuda del programa.")