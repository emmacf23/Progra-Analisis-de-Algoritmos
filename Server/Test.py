import json
import math
import multiprocessing

from Genetic import *
from Probabilistc import *
from misc.tree import Tree

antSpeed = 1


def oneByOne(pTrees):
    global antSpeed
    cantAnts = 0
    totalLeaves = 0
    for tree in pTrees:
        timeElapsed = 2 * ((tree.x / antSpeed) + (tree.height / antSpeed))
        cantAnts = math.floor(math.floor(timeElapsed) * (1 / antSpeed))
        leavesXTree = math.floor(tree.leaves_count / cantAnts) * cantAnts
        totalLeaves += leavesXTree
    print("Cantidad Hormigas: ", cantAnts)
    print("Hojas Totales: ", totalLeaves)
    return cantAnts, totalLeaves


def getGrowPercentage(pTreeLength, pTreeLevels, pLeafLength):
    return (pLeafLength / pTreeLength) ** 1 / pTreeLevels


trees = []
with open('test1.json') as json_file:
    data = json.load(json_file)
    indexLetras = 0
    for p in data['test']:
        # print('PosX: ' + str(p['posX']))
        # print('Length: ' + str(p['length']))
        # print('Levels: ' + str(p['levels']))
        # print('LeafLength: ' + str(p['leafLength']))
        # print('')
        growPercentage = getGrowPercentage(p['length'], p['levels'], p['leafLength'])
        tree = Tree("A", p['posX'], p['levels'], p['length'], growPercentage)
        # tree = Tree("A", p['posX'], p['levels'])
        trees.append(tree)
        indexLetras += 1


def analize(pGene, pProba):
    if pGene.Aptitud / pGene.totalAnts > pProba["leaf_count"] / pProba["ant_count"]:
        return pGene.order, data
    else:
        return pProba["loop"], data


def getData():
    return data


def reinar(pTime):
    geneSet = generateGeneSet(trees)
    quantAntsOO = oneByOne(trees)
    start_timeG = time()
    g = genetic(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, 10000, trees, start_timeG, (pTime * 0.2))
    print("Genetic: ", g)
    elapsed_time = time() - start_timeG
    print("Elapsed time: %.10f seconds." % elapsed_time)
    start_timeP = time()
    p = mainProbabilistic(trees, quantAntsOO[0], start_timeP, 10000, (pTime * 0.2))
    print("Probabilistic: ", p)
    elapsed_time = time() - start_timeP
    print("Elapsed time: %.10f seconds." % elapsed_time)
    return analize(g, p)

    """
    mainProbabilistic = multiprocessing.Process(target=mainProbabilistic, args=(trees, quantAntsOO[0], start_time, 900000, (tiempo * 0.2)))
    genetic = multiprocessing.Process(target=genetic, args=(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, 900000, trees, start_time, (tiempo * 0.2)))
    mainProbabilistic.start()
    genetic.start()
    mainProbabilistic.join()
    genetic.join()
    
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
    """
