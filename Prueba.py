import math
import multiprocessing
from multiprocessing import pool
import random
from time import time

from Arbol import *
from Rango import *
from Hormigas import *

velocidad = 2


def oneByOne(tiempo, arboles, start_time):
    global velocidad
    hojasTotales = 0
    while time() - start_time < tiempo:
        hormigasTotales = 0
        for arbol in arboles:
            duracion = 2 * ((arbol.ubicacion / velocidad) + (arbol.duracionSubir / velocidad))
            hormigasTotales = math.floor(math.floor(duracion) / velocidad)
            hojasxArbol = math.floor(arbol.cantHojas / hormigasTotales) * hormigasTotales
            hojasTotales += hojasxArbol
            print("Hojas Por Arbol: ", hojasxArbol)
        print("Cantidad Hormigas: ", hormigasTotales)
        print("Hojas Totales: ", hojasTotales)
        break


def cantHojas(arboles, cantHormigas, rango):
    global velocidad
    rango.hojas = 0
    for arbol in arboles:
        rango.hojas += math.floor(arbol.cantHojas / cantHormigas) * cantHormigas
    duracion = 2 * ((arboles[-1].ubicacion / velocidad) + (arboles[-1].duracionSubir / velocidad))
    rango.sobrantes = cantHormigas - math.floor(math.floor(duracion) / velocidad)


def sacarRangos(cantRangos, maxHormigas):
    rango = math.floor(maxHormigas / cantRangos)
    rangos = []
    for cant in range(0, cantRangos):
        rangos.append(Rango(1, rango * cant + 1, rango * (cant + 1)))
    return rangos


def genRandom(min, max):
    return random.randint(min, max)


def probabilistic(maxHormigas, arboles):
    ranges = sacarRangos(25, maxHormigas)
    mejorRango = ranges[random.randint(0, len(ranges) - 1)]
    cantHojas(arboles, genRandom(mejorRango.numMinimo, mejorRango.numMaximo), mejorRango)
    for prueba in range(0, 10):
        ran = random.uniform(0.0, 1.0)
        for _range in ranges:
            quantRandomAnts = random.randint(_range.numMinimo, _range.numMaximo)
            if _range.probabilidad > ran:
                cantHojas(arboles, quantRandomAnts, _range)
                if _range.hojas >= mejorRango.hojas and _range.sobrantes <= _range.numMaximo - _range.numMinimo:
                    mejorRango = _range
                    _range.probabilidad += 0.09
                else:
                    _range.probabilidad -= 0.5
    return mejorRango


if __name__ == "__main__":
    tiempo = int(input("Inserte un tiempo por favor:"))
    arboles = [Arbol(4, 2, 50), Arbol(8, 3, 100)]
    start_time = time()
    oneByOne(tiempo * 0.2, arboles, start_time)
    print("_____________________________")
    print(probabilistic(150, arboles))
    elapsed_time = time() - start_time
    print("Elapsed time: %.15f seconds." % elapsed_time)
    """
    tiempo = int(input("Inserte un tiempo por favor:"))
    arboles = [Arbol(4, 2, 1500000), Arbol(8, 3, 500000)]
    start_time = time()
    oneByOne = multiprocessing.Process(target=oneByOne, args=(
        tiempo, arboles))
    probabilistic = multiprocessing.Process(target=probabilistic,args=(150,arboles))
    oneByOne.start()
    probabilistic.start()

    oneByOne.join()
    probabilistic.join()

    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
    """
