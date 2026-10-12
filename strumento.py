class Strumento:
    def __init__(self, codice, tipo, marca, anno, costo):
        self.__codice= codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno = anno
        self.__costo = costo
        self.__in_prestito= False

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self, codice_nuovo):
        self.__codice = codice_nuovo

    @property
    def marca(self):
        return self.__marca #per accedere all'attributo marca in modo più semplice

    @property
    def in_prestito(self):
        return self.__in_prestito

    @in_prestito.setter
    def in_prestito(self, nuovo_bool):
        self.__in_prestito = nuovo_bool



    def __str__(self):
        return f"{self.__codice} {self.__tipo} {self.__marca} {self.__anno} {self.__costo} {self.__in_prestito}"


