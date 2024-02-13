#!/usr/bin/env python3

"""
Hecho por: Alvaro Camilo Torres
Institución: Universidad Nacional de Colombia
Materia: Matemáticas Discretas
"""
from pwn import *
from colorama import Fore, Style
import sys, signal, time, os

def def_handler(sig, frame):
    print(f"\n\n[{rojo}!{reset}] {rojo}Saliendo...{reset}\n")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
primos = [2, 3, 5] # La lista de primos se inicializa con los 3 primeros primos para que funcione el programa

#Colores
amarillo = Fore.YELLOW
azul = Fore.BLUE
rojo = Fore.RED
verde = Fore.GREEN
reset = Style.RESET_ALL # Resetea el color de la consola

# Detecta el sistema operativo para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Indica si un número es primo o no
def hallar_primos(número, primos):
    es_primo = True
    for j in primos:
        if j > int(número**0.5) + 1:
            break
        elif número % j == 0:
            es_primo = False
            break
    return es_primo

# Encuentra los primos entre P_n^2 y P_(n+1)^2
def brocard(primos, n, hallar_primos):
    
    global tope_superior, tope_inferior, intermedios
    i = 1

    while True:
        if n > len(primos) - 2:
            if hallar_primos(primos[2] + i, primos):
                primos.append(primos[2] + i)
            i += 1
        else:
            break

    tope_superior = primos[n + 1] ** 2
    tope_inferior = primos[n] ** 2
    intermedios = []
   

    if tope_superior > primos[-1]:
        for num in range(primos[-1] + 1, tope_superior + 1):
            if hallar_primos(num, primos):
                primos.append(num)

    intermedios = [str(i) for i in range(tope_inferior, tope_superior + 1) if i in primos]

# Evalúa la conjetura de Brocard incrementando el ínice n infinitamente
def brocard_infinito(primos, hallar_primos, brocard, velocidad):
    proc1 = log.progress("")
    proc1.status("Iniciando prueba a la conjetura de Brocard")
       
    if '-v' in sys.argv or '--verbose' in sys.argv:
        proc2 = log.progress("")
        proc2.status("Listando primos entre P_n^2 y P_(n+1)^2")
    n = 1

    time.sleep(2)
   
    while True:
        brocard(primos, n, hallar_primos)
        if len(intermedios) < 4:
            log.info(f" Se ha encontrado una excepción al problema de brocard con el primo {azul}{primos[n]}{reset} donde entre {azul}{primos[n]**2}{reset} y {azul}{primos[n+1]**2}{reset} no hay 4 primos")
            break
        else:
            proc1.status(f"Para {amarillo}P_{n}{reset} = {azul}{primos[n]}{reset}, entre {azul}{tope_inferior}{reset} y {azul}{tope_superior}{reset} se encontraron {verde}{len(intermedios)}{reset} primos")
            n += 1
        if '-v' in sys.argv or '--verbose' in sys.argv:
            proc2.status(f"Los primos encontrados son: {azul}{(reset +', ' + azul).join(intermedios)}{reset}")

        if velocidad == 1:
            time.sleep(2)
        elif velocidad == 2:
            time.sleep(1)
        elif velocidad == 3:
            time.sleep(0.5)        

# Evalúa la conjetura de Brocard para un ínice 'n' en particular
def brocard_individual(primos, hallar_primos, brocard, n):
   
    brocard(primos, n, hallar_primos)
    
    log.info(f"Para {amarillo}P_{n}{reset} = {azul}{primos[int(n)]}{reset}, entre {azul}{tope_inferior}{reset} y {azul}{tope_superior}{reset} se encontraron {verde}{len(intermedios)}{reset} primos")
    if '-v' in sys.argv or '--verbose' in sys.argv:
        log.info(f"Los primos encontrados son: {azul}{(reset +', ' + azul).join(intermedios)}")

# Muestra las instrucciones del programa por consola
def panel_ayuda():
    print(f"""\n\n[{verde}+{reset}] Modo de uso:

        python3 brocard.py [{amarillo}opciones{reset}] [{amarillo}argumentos{reset}]

[{verde}+{reset}] Ejemplos:

        python3 brocard.py -h
        python3 brocard.py -i 3
        python3 brocard.py -n 100

[{verde}+{reset}] Opciones:

        {amarillo}-h{reset}, {amarillo}--help{reset}                  Muestra este panel de ayuda

        {amarillo}-i{reset}, {amarillo}--infinite{reset} {azul}speed{reset}        Prueba la conjetura de Brocard infinitamente hasta que pare el programa.
                                    Como argumento puede recibir un entero del 1-4 para representar velocidad, siendo 1 la más lenta y 4 la más rápida(por defecto)

        {amarillo}-n{reset}, {amarillo}--index{reset} {azul}int{reset}             Prueba el programa con un índice n en específico    
        {amarillo}-v{reset}, {amarillo}--verbose{reset}               Muestra los primos entre el intervalo P_n^2 y P_(n+1)^2
        """)

if __name__ == '__main__': # Si se ejecuta el script directamente
    
    limpiar_pantalla()
    print(f"""{verde} ______                                               __  _                  
|_   _ \                                             |  ]| |                 
  | |_) | _ .--.   .--.   .---.  ,--.   _ .--.   .--.| | \_|.--.             
  |  __'.[ `/'`\]/ .'`\ \/ /'`\]`'_\ : [ `/'`\]/ /' \  |   ( (`\]            
 _| |__) || |    | \__. || \__. // | |, | |    | \__/  |    `'.'.            
|_______/[___]    '.__.' '.___.'\ -;__/[___]    '.__.;__]  [\__) )           
                                _                _                           
                               (_)              / |_                         
    .---.   .--.   _ .--.      __  .---.  .---.`| |-'__   _   _ .--.  .---.  
   / /'`\]/ .'`\ \[ `.-. |    [  |/ /__ \/ /'`\]| | [  | | | [ `/'`\]/ /__ \ 
   | \__. | \__. | | | | |  _  | || \__.,| \__. | |, | \_/ |, | |    | \__., 
   '.___.' '.__.' [___||__][ \_| | '.__.''.___.'\__/ '.__.'_/[___]    '.__.' 
                            \____/                                           {reset}\n""")

    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:

        panel_ayuda()

    elif sys.argv[1] == '-i' or sys.argv[1] == '--infinite':
        try:
            brocard_infinito(primos, hallar_primos, brocard, 4 if len(sys.argv) == 2 or (('-v' in sys.argv or '--verbose' in sys.argv) and len(sys.argv) == 3) else int(sys.argv[2]))
        except ValueError:
            panel_ayuda()
    
    elif sys.argv[1] == '-n' or sys.argv[1] == '--index':
        try:
            brocard_individual(primos, hallar_primos, brocard, int(sys.argv[2]))
        except ValueError:
            panel_ayuda()
