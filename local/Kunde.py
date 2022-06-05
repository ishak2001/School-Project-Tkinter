class Kunde(object):
    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname

    #Ändern
    def vornameAendern(self, neuerVorname):
        self.__vorname = neuerVorname

    def nachnameAendern(self, neuerNachname):
        self.__nachname = neuerNachname

    #Zurückliefern
    def liefereVorname(self):
        return self.__vorname

    def lieferenachname(self):
        return self.__nachname