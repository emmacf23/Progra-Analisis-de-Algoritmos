class Chromosome:
    def __init__(self, genes, aptitud,ants,order):
        self.Genes = genes
        self.Order = order
        self.totalAnts = ants
        self.Aptitud = aptitud

    def __repr__(self):
        return '{}: Aptitud: {} Total Hormigas {} Order: {}'.format(self.__class__.__name__, self.Aptitud,self.totalAnts,self.Order)
