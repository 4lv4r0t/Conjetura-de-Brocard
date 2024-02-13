# Conjetura-de-Brocard

Programa diseñado para la prueba de la conjetura de Brocard, esta nos dice que entre 2 números primos con índice n y n+1, si los elevamos al cuadrado, entre esos 2 números van a haber por lo menos 4 números primos, con la condición que el índice 'n' sea mayor o igual a 2.

Entre las opciones que contempla el programa estan:
* Evaluar la conjetura aumentando el índice 'n' de 1 en 1 infinitamente, se puede ajustar la velocidad y mostrar los primos intermedios por pantalla
* Evaluar la conjetura en un índice 'n' en específico, con opción de mostrar los primos intermedios

## Instalación:
Clonamos el repositorio e instalamos las librerías requeridas:
```bash
git clone https://github.com/4lv4r0t/Conjetura-de-Brocard
cd Conjetura-de-Brocard
pip install -r requirements.txt
```

## Modo de uso:
```
[+] Modo de uso:

        python3 brocard.py [opciones] [argumentos]

[+] Ejemplos:

        python3 brocard.py -h
        python3 brocard.py -i 3
        python3 brocard.py -n 100

[+] Opciones:

        -h, --help                  Muestra este panel de ayuda

        -i, --infinite speed        Prueba la conjetura de Brocard infinitamente hasta que pare el programa.
                                    Como argumento puede recibir un entero del 1-4 para representar velocidad, siendo 1 la más lenta y 4 la más rápida(por defecto)

        -n, --index int             Prueba el programa con un índice n en específico    
        -v, --verbose               Muestra los primos entre el intervalo P_n^2 y P_(n+1)^2
```
## Documentación:

En el repositorio se encuentra un notebook (archivo .ipynb), en el cual se explica más a fondo cómo funciona el código, se puede ver con el mismo github o pueden importarlo a herramientas para leer y reproducir notebooks como [Google Colab](https://colab.research.google.com/) o [Jupyter](https://jupyter.org)
