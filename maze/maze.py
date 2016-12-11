# coding: utf-8 

import numpy

class MazeGame(object):

    def __init__(self, data, start, end):
        """Inicializuje bludiste
        data je 2D matice , 
        start je pozice zacatku, napr [1,1]
        stop je pozice konce cile. napr. [10,10].

        Pokud start nebo stop je mimo bludiste, vyvola vyjimku
        """
        assert data.dtype == bool

    def getSize(self):
        "Vrati velikost bludiste"
        return self.data.shape

    def getStart(self):
        return (0,0)

    def getEnd(self):
        return (10, 10)

    def isFree(self, x, y):
        "Vrátí False jestli na pozici x,y chodba. Jinak vrací True"
        return True                        

    def getSolution(self):
        "Vrati nejake nejkratsi reseni bludiste nebo vyvola vyjimku"
        return MazePath(steps=[])

    @staticmethod 
    def fromString(data):
        """
        Postavi bludiste z retezce. 
        Prazdne radky se ignoruji, 
        X nebo # je zed,  B je zacatek a E je konec.
        """
        data = numpy.array([[True, True, True], [False, True, True]])
        return MazeGame(data, start=(0,0), end=(1,2))

class MazePath(object):
    "Objekt obsahujici cestu v bludisti"

    def __init__(self, steps):
        "Inicializuje objekt MazePath"
        pass

    def length(self):
        "Vraci delku cesty v bludisti"
        return 0

    def __iter__(self):
        "Iterator vracejici jednotlive body cesty"
        yield (0,0)
        yield (0,1)
        yield (1,1)
