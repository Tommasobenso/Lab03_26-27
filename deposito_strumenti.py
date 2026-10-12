from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}
        self.contatore = 0


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for riga in file:
                    riga = riga.strip()
                    if riga == "":  # se riga è vuota passo all'iterazione dopo
                        continue
                    campi = riga.split(",")
                    codice = campi[0]
                    tipo = campi[1]
                    marca = campi[2]
                    anno_acquisto = int(campi[3])
                    valore = float(campi[4])

                    strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)   # creo oggetto

                    self.strumenti[codice] = strumento  # dizionario che ha come chiave il codice e come valore l'oggetto relativo

        except FileNotFoundError:
            print("File non trovato")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        ultimo_numero = 0
        for codice in self.strumenti:
            numero = int(codice[1:])    # perchè il codice è del tipo S1
            if numero > ultimo_numero:
                ultimo_numero = numero
            nuovo_codice = f"S{ultimo_numero+1}"
            strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)

            self.strumenti[codice] = strumento
            return strumento



    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumenti = list(self.strumenti.values())
        strumenti_ordinati = sorted(strumenti, key=attrgetter("marca"))

        return strumenti_ordinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        if id_strumento not in self.strumenti:  # se esiste
            raise Exception("Strumento non presente nel deposito.")
        for codice in self.prestiti:    # ora vedo se non è gia stato prestato
            prestito = self.prestiti[codice]
            if prestito.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito.")

        self.contatore += 1
        codice_prestito = f"P{self.contatore}"

        nuovo_prestito = Prestito(codice_prestito, data, id_strumento, cognome_allievo) # creo oggetto
        self.prestiti[codice_prestito] = nuovo_prestito # aggiungo al dizionario
        return nuovo_prestito




    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        if id_prestito not in self.prestiti:    # controllo che sia presente
            raise Exception("Prestito non presente nel sistema.")
        del self.prestiti[id_prestito]      # lo rimuovo dal dizionario dei prestiti attivi



