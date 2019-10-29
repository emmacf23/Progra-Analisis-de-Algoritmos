class Arbol:

    def __init__(self, pUbicacion, pDuracionSubir,pCantHojas):
        self.ubicacion = pUbicacion
        self.duracionSubir = pDuracionSubir
        self.cantHojas = pCantHojas;

    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                  self.ubicacion, self.duracionSubir,self.cantHojas)
