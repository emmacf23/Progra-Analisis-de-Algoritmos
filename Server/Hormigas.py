class Hormiga:

    def __init__(self, pReturnTime,pVelocidad):
        self.returnTime = pReturnTime
        self.cantHojas= 0
        self.velocidad = pVelocidad

    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                  self.returnTime, self.cantHojas,self.velocidad)
