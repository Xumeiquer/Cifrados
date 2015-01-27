#!/usr/bin/env python
# -*- codign: utf8 -*-

import sys
from docopt import docopt

__all__ = ["cesar", "u_cesar"]
__author__ = "Jaume Martin"
__version__ = "0.1"
__license__ = "MIT"
__app_name__ = "cesar"
__doc__ = """Usage: cesar.py [-h] ( -c | -d ) -n <numero> -t <texto>
cesar.py -c -n <numero> -t <texto> [-g <fichero>]
cesar.py -d -n <numero> -t <texto> [-g <fichero>]

Opciones:
-h, --help                        Muesta este mensaje
-c, --cifra                       Cifra el texto
-d, --descifra                    Descifra el texto
-t <texto>, --texto <texto>       Texto original
-g <archivo>, --guadar <archivo>  Guarda el resultado en el fichero
-n <numero>, --numero <numero>    Numero de desplazamiento

"""

ALFABETO = [chr(x) for x in range(32, 127)]
ALFABETO_NUEVO = []
TAMANYO_AFABETO = len(ALFABETO)

def args_correctos(args):
    """Comprueba que los parametros son correctos
    """
    if len(args["--texto"]) > 0 and args["--numero"].isdigit():
        if int(args["--numero"]) > 0 and int(args["--numero"]) < TAMANYO_AFABETO:
            return True
    return False


def genera_algabeto_cod(desplazamiento):
    """Genera el alfabeto de caracteres para cifrar
    """
    global ALFABETO
    global ALFABETO_NUEVO
    ALFABETO_NUEVO = []
    for idx, letra in enumerate(ALFABETO):
        nueva_letra_idx = (idx + desplazamiento) % TAMANYO_AFABETO
        ALFABETO_NUEVO.append(ALFABETO[nueva_letra_idx])

def genera_algabeto_descod(desplazamiento):
    """Genera el alfabeto de caracteres para descifrar
    """
    global ALFABETO
    global ALFABETO_NUEVO
    ALFABETO_NUEVO = []
    tamanyo_alfabeto = len(ALFABETO)
    for idx, letra in enumerate(ALFABETO):
        nueva_letra_idx = (idx - desplazamiento) % tamanyo_alfabeto
        ALFABETO_NUEVO.append(ALFABETO[nueva_letra_idx])


def cesar(texto, desplazamiento=None):
    """Implementa la codificacion Cesar
    """
    global ALFABETO
    global ALFABETO_NUEVO
    if isinstance(desplazamiento, int) and desplazamiento > 0 and desplazamiento < TAMANYO_AFABETO:
        genera_algabeto_cod(desplazamiento)
    elif desplazamiento != None:
        raise TypeError("Desplazamiento debe ser de tipo entero")
    texto_cifrado = ""
    for l in texto:
        try:
            texto_cifrado += ALFABETO_NUEVO[ALFABETO.index(l)]
        except (ValueError):
            sys.stderr.write("{}.py no puede encontrar la letra {} para cifrarla".format(__app_name__, l))
            sys.exit(-1)
    return texto_cifrado


def u_cesar(texto, desplazamiento=None):
    """Implementa la descodificacion Cesar
    """
    global ALFABETO
    global ALFABETO_NUEVO
    if isinstance(desplazamiento, int) and desplazamiento > 0 and desplazamiento < TAMANYO_AFABETO:
        genera_algabeto_descod(desplazamiento)
    elif desplazamiento != None:
        raise TypeError("Desplazamiento debe ser de tipo entero")
    texto_descifrado = ""
    for l in texto:
        try:
            texto_descifrado += ALFABETO_NUEVO[ALFABETO.index(l)]
        except(ValueError):
            sys.stderr.write("{}.py no puede encontrar la letra {} para cifrarla".format(__app_name__, l))
            sys.exit(-1)
    return texto_descifrado

    
if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    if args_correctos(args):
        if args["--cifra"]:
            genera_algabeto_cod(int(args["--numero"]))
            texto = cesar(args["--texto"])
            sys.stdout.write(texto)
        else:
            genera_algabeto_descod(int(args["--numero"]))
            texto = ucesar(args["--texto"])
            sys.stdout.write(texto)
