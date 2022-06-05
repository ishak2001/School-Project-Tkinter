class System_app(object):
    def __init__(self, ankunft, abfahrt, gleis, reisenach):
        self.__ankunftszeit = ankunft
        self.__abfahrtszeit = abfahrt
        self.__ankunftsgleis = gleis
        self.__abfahrtnach = reisenach
        
    def liefereAnkunftZeit(self):
        return self.__ankunftszeit
    
    def liefereAbfahrtsZeit(self):
        return self.__abfahrtszeit
        
    def liefereGleis(self):
        return self.__ankunftsgleis
    
    def liefereNach(self):
        return self.__abfahrtnach