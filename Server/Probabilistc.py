import random
from time import time

from misc.ant_admin import AntAdmin


def getBacks(pTrees):
    allBacks = 0
    for tree in pTrees:
        allBacks += tree.total_distance
    return allBacks


def getProbability(pTrees, pAllBacks):
    probabilities = []
    totalProb = 0
    for tree in pTrees:
        prob = 1 - tree.total_distance / pAllBacks
        probabilities.append(prob)
        totalProb += prob
    for index in range(0, len(probabilities)):
        probabilities[index] = probabilities[index] / totalProb
    return probabilities


def getTreeByProbability(pRandom, pProbabilities):
    treePosition = 0
    for probability in pProbabilities:
        if pRandom <= 0 or treePosition >= len(pProbabilities) - 1:
            break
        treePosition += 1
        pRandom -= probability
    return treePosition


def probabilistic(pQuantAnts, pProbabilities, pTrees, pTime,pAntsSpeed):
    ants = []
    for i in range(0, pQuantAnts):
        r = random.uniform(0.0, 1.0)
        position = getTreeByProbability(r, pProbabilities)
        ants.append(position)
    result = AntAdmin.evaluate(pTrees, ants, pAntsSpeed, pTime)
    return result


def mainProbabilistic(pTrees, pQuantAnts, pStartTime, pTime, pTime_lapse,pAntsSpeed):
    allBacks = getBacks(pTrees)
    probabilities = getProbability(pTrees, allBacks)
    bestResult = probabilistic(pQuantAnts, probabilities, pTrees, pTime,pAntsSpeed)
    while time() - pStartTime < pTime_lapse:
        result = probabilistic(pQuantAnts, probabilities, pTrees, pTime,pAntsSpeed)
        if result["leaf_count"] > bestResult["leaf_count"]:
            bestResult = result
    return bestResult

