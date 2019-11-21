import json
import math
import multiprocessing

from Genetic import *
from Probabilistc import *
from misc.tree import Tree

antSpeed = 1
xFactor = 1000000000

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
        growPercentage = getGrowPercentage(p['length'], p['levels'], p['leafLength'])
        tree = Tree("A", p['posX'], p['levels'], p['length'], growPercentage)
        trees.append(tree)
        indexLetras += 1


def analize(pGene, pProba):
    if pGene.Aptitud / pGene.totalAnts > pProba["leaf_count"] / pProba["ant_count"]:
        return pGene.Order, pGene.Aptitud
    else:
        return pProba["loop"], pProba["leaf_count"]


def getData():
    return data


def reinar(pTime):
    global xFactor
    print("Tiempo",pTime)
    geneSet = generateGeneSet(trees)
    quantAntsOO = oneByOne(trees)
    start_timeG = time()
    g = genetic(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, xFactor, trees, start_timeG, (pTime * 0.2))
    #print("Genetic: ", g)
    elapsed_time = time() - start_timeG
    print("Elapsed time: %.10f seconds." % elapsed_time)
    start_timeP = time()
    p = mainProbabilistic(trees, quantAntsOO[0], start_timeP, xFactor, (pTime * 0.2))
    #print("Probabilistic: ", p)
    elapsed_time = time() - start_timeP
    print("Elapsed time: %.10f seconds." % elapsed_time)
    print(quantAntsOO[1])
    print("Genetico: Hormigas Totales:", g.totalAnts," Hojas:",g.Aptitud)
    print("Probabilistico: Hormigas Totales:", p["ant_count"]," Hojas", p["leaf_count"])
    return analize(g, p)
