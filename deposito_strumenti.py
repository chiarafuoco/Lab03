from strumento import Strumento
from operator import attrgetter
from prestito import Prestito
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome= nome
        self.__responsabile= responsabile
        self.__lista_strumenti_deposito= []
        self.__lista_prestiti= []

    @property #anche se non richiesto essendo privato con il doppio underscore
    #ha senso lasciare la libertà di cambiarlo, con questo leggo
    def nome(self):
        return self.__nome

    @nome.setter #modifico con il nuovo nome
    def nome(self,nuovo_nome):
        self.__nome = nuovo_nome

    @property
    def responsabile(self): #leggo il nome del responsabile
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, nuovo_nome_responsabile): #metto a disposizione la possibilità di modificare
        self.__responsabile = nuovo_nome_responsabile

    @property
    def lista_prestiti(self):
        return self.__lista_prestiti

    @lista_prestiti.setter
    def lista_prestiti(self, nuova_lista):  # metto a disposizione la possibilità di modificare
        self.__lista_prestiti = nuova_lista




    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path,"r", encoding="utf=8") as infile:
                lista_strumenti= [ ]
                for line in infile:
                    line= line.rstrip("\n")
                    line= line.split(",")
                    s= Strumento(line[0],line[1],line[2],line[3],line[4]) #ho creato lo
                    # strumento della riga in questione, utilizzando la classe Strumento
                    lista_strumenti.append(s) #aggiungo ogni strumento alla lista

                self.__lista_strumenti_deposito= lista_strumenti #ho sovrascritto la lista corrispondente
                #all'attributo lista strumenti con una lista creata leggendo il file
            print("File caricato con successo!")
        except FileNotFoundError:
            print("File non trovato o non esistente")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""

        ultimo_strumento = self.__lista_strumenti_deposito[len(self.__lista_strumenti_deposito)-1] #estraggo l'ultimo strumento
        ultimo_codice = ultimo_strumento.codice #estraggo il codice dell'ultimo strumento
        ultimo_codice = int(ultimo_codice.lstrip("S")) #estraggo il codice numerico dello strumento
        s = Strumento(f"S{str(ultimo_codice+1)}", tipo, marca, anno_acquisto, valore) #creo il nuovo strumento creando anche il nuovo ID

        self.__lista_strumenti_deposito.append(s) #aggiungo il nuovo strumento alla lista della classe

        return s #returno lo strumento aggiunto, che verrà visualizzato in console come stringa



    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        self.__lista_strumenti_deposito.sort(key=attrgetter("marca")) #ho ordinato
        #gli strumenti per marca

        return self.__lista_strumenti_deposito #la parte del print era già fatta, dunque bastava returnare la lista ordinata


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        if self.__lista_prestiti != []:

            ultimo_prestito = self.__lista_prestiti[len(self.__lista_prestiti) - 1]  # estraggo l'ultimo prestito
            ultimo_codice = ultimo_prestito.id_prestito  # estraggo il codice dell'ultimo prestito
            ultimo_codice = int(ultimo_codice.lstrip("P"))  # estraggo il codice numerico del prestito
        else:
            ultimo_codice= 0

        lista_id_strumento= [] #lista di tutti gli id strumenti presenti nel deposito
        for el in self.__lista_strumenti_deposito: ##ciclo per creare la lista
            lista_id_strumento.append(el.codice) #aggiungo il codice strumento nella lista codici

        if id_strumento in lista_id_strumento: #controllo se l'id dello strumento è nella lista di id
            for el in self.__lista_strumenti_deposito: #ciclo per trovare lo strumento
                if el.codice == id_strumento: #controllo se ho trovato lo strumento
                    if el.in_prestito == False: #controllo che non sia in prestito
                        el.in_prestito = True #imposto che lo strumento è in prestito
                        p = Prestito(f"P{str(ultimo_codice + 1)}", data, id_strumento, cognome_allievo) #ho creato un prestito aggiungendo l'id
                        self.__lista_prestiti.append(p) #aggiungo alla lista di prestiti
                        return p
                    else:
                        print("Errore: strumento già in prestito")
        else:
            print("Errore: strumento non presente")


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        lista_id_prestiti= [] #lista di tutti gli id dei prestiti fatti
        for el in self.__lista_prestiti: ##ciclo per creare la lista
            lista_id_prestiti.append(el.id_prestito) #aggiungo il codice prestito nella lista di id prestiti

        if id_prestito in lista_id_prestiti: #controllo se l'id del prestito è nella lista di id
            for el in self.__lista_prestiti: #ciclo per trovare il prestito
                if el.id_prestito == id_prestito: #controllo se ho trovato il prestito
                    id_strumento_in_prestito = el.id_prestito_strumento
                    for strumento in self.__lista_strumenti_deposito:  # ciclo per trovare lo strumento
                        if strumento.codice == id_strumento_in_prestito:  # controllo se ho trovato lo strumento
                            strumento.in_prestito = False #strumento non più in prestito
                            self.__lista_prestiti.remove(el) #rimuovo il prestito, che in questo ciclo è la variabile "el"
                            return id_prestito
        else:
            print("Errore: strumento non presente")
