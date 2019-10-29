class Rango:
    def __init__(self, pProbabilidad, pNumMinimo, pNumMaximo):
        self.probabilidad = pProbabilidad
        self.numMinimo = pNumMinimo
        self.numMaximo = pNumMaximo
        self.hojas = 0
        self.sobrantes = 0

    def __repr__(self):
        return '{}: {} {} {} Hojas:{}'.format(self.__class__.__name__,
                                              self.probabilidad,
                                              self.numMinimo,
                                              self.numMaximo, self.hojas)
