"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""
import os
os.system('cls')

def evaluarCarrera(acciones:list, pista:str):
    pista = list(pista)
    esGanador = True 
    for i in range(len(pista)):
        if acciones[i] == 'jump' and pista[i] != '|':
            pista[i] = 'X'
            esGanador = False
        if acciones[i] == 'run' and pista[i] != '_':
            pista[i] = '/'
            esGanador = False
    
    print("".join(pista))
    if esGanador:
        print('El atleta ha ganado la carrera')
    else:
        print('El atleta NO ha ganado la carrera')


        


evaluarCarrera(['run', 'jump', 'run', 'run', 'jump','run',], '_|__|_')
evaluarCarrera(['run', 'jump', 'run', 'run', 'jump','jump',], '_|__|_')
