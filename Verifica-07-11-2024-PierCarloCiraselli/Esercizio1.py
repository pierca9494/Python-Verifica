class DivisoreDati:
    def __init__(self):
        # Incapsulamento delle liste
        self.__numeri = []
        self.__stringhe = []
        self.__booleani = []

    def aggiungi_dato(self, dato):
        """Aggiunge un dato alla lista corretta in base al suo tipo."""
        if isinstance(dato, (int, float)):
            self.__numeri.append(dato)
        elif isinstance(dato, str):
            self.__stringhe.append(dato)
        elif isinstance(dato, bool):
            self.__booleani.append(dato)
        else:
            print("Tipo di dato non riconosciuto.")

    def richiedi_dati(self, numero_dati):
        """Richiede l'inserimento di dati dall'utente per il numero di volte specificato."""
        for _ in range(numero_dati):
            dato_input = input("Inserisci un dato (numero, parola o valore booleano): ")
            # Converti il dato al tipo appropriato
            if dato_input.lower() == "true":
                dato = True
            elif dato_input.lower() == "false":
                dato = False
            elif dato_input.replace('.', '', 1).isdigit():
                dato = float(dato_input) if '.' in dato_input else int(dato_input)
            else:
                dato = dato_input
            self.aggiungi_dato(dato)

    def stampa_lista(self, tipo_lista):
        """Stampa una singola lista in base al tipo specificato."""
        if tipo_lista == "numeri":
            print("Lista Numeri:", self.__numeri)
        elif tipo_lista == "stringhe":
            print("Lista Stringhe:", self.__stringhe)
        elif tipo_lista == "booleani":
            print("Lista Booleani:", self.__booleani)
        else:
            print("Tipo di lista non valido. Usa 'numeri', 'stringhe' o 'booleani'.")

    def stampa_tutte_liste(self):
        """Stampa tutte le liste insieme."""
        print("Lista Numeri:", self.__numeri)
        print("Lista Stringhe:", self.__stringhe)
        print("Lista Booleani:", self.__booleani)


# Esempio di utilizzo
divisore = DivisoreDati()

# Richiesta di inserire i dati
numero_dati = int(input("Quanti dati vuoi inserire? "))
divisore.richiedi_dati(numero_dati)

# Stampa di una lista specifica o di tutte
scelta = input("Vuoi stampare una lista singola o tutte? (singola/tutte): ")
if scelta == "singola":
    tipo_lista = input("Quale lista vuoi stampare? (numeri/stringhe/booleani): ")
    divisore.stampa_lista(tipo_lista)
elif scelta == "tutte":
    divisore.stampa_tutte_liste()
else:
    print("Scelta non valida.")
