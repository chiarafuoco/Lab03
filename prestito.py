class Prestito:
    def __init__(self,id_prestito,data,id_strumento, cognome_allievo):
        self.__id_prestito = id_prestito
        self.__data= data
        self.__id_strumento= id_strumento
        self.__cognome_allievo= cognome_allievo

    @property
    def id_prestito(self):
        return self.__id_prestito

    @property
    def id_prestito_strumento(self):
        return self.__id_strumento

    def __str__(self):
        return f"{self.__id_prestito} {self.__data} {self.__id_strumento} {self.__cognome_allievo}"