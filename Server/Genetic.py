import random

from Chromosomes import *
from misc.ant_admin import AntAdmin
from time import time


def _generar_padre(pLength, pGeneSet, pAntsSpeed, pTime, pTtrees):
    genes = []
    while len(genes) < pLength:
        genes.append(pGeneSet[random.randint(0, len(pGeneSet) - 1)])
    result = AntAdmin.evaluate(pTtrees, genes, pAntsSpeed, pTime)
    return Chromosome(genes, result["leaf_count"], result["ant_count"], result["loop"])


def _mutar(pFather, pGeneSet, pTime, pTrees):
    index = random.randrange(0, len(pFather.Genes))
    geneChild = pFather.Genes
    for quantChanges in range(0, 3):
        newG, alterno, newGene = random.sample(pGeneSet, 3)
        if newG == geneChild[index]:
            geneChild[index] = alterno
        else:
            geneChild[index] = newG
        # geneChild.append(newGene)
    genes = geneChild
    ##Cambiar Velocidad
    result = AntAdmin.evaluate(pTrees, genes, 1, pTime)
    return Chromosome(genes, result["leaf_count"], result["ant_count"], result["loop"])


def generateGeneSet(pTrees):
    positions = []
    position = 1
    while position < len(pTrees):
        positions.append(position)
        position += 1
    return positions


def genetic(pTargetLength, pOptimalFit, pGeneSet, pAntsSpeed, pTime, pTrees, pStartTime, pTimeLapse):
    random.seed()
    bestDad = _generar_padre(pTargetLength, pGeneSet, pAntsSpeed, pTime, pTrees)
    if bestDad.Aptitud >= pOptimalFit:
        return bestDad
    while time() - pStartTime < pTimeLapse:
        child = _mutar(bestDad, pGeneSet, pTime, pTrees)
        if bestDad.Aptitud >= child.Aptitud:
            continue
        if child.Aptitud >= pOptimalFit:
            return child
        bestDad = child
    return bestDad
