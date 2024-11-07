class RaccoglitoreDati:
    def __init__(self):
        self.__collezione = []  # Collezione per contenere tutti i dati inseriti dall'utente

    def aggiungi_dati(self, numero_di_dati):
        """Chiede all'utente di inserire un numero specifico di parole o numeri e li aggiunge alla collezione."""
        for _ in range(numero_di_dati):
            dato = input("Inserisci una parola o un numero: ")
            # Conversione automatica a numero se possibile
            if dato.isdigit():  # Controlla se è un numero intero
                dato = int(dato)
            elif dato.replace('.', '', 1).isdigit():  # Controlla se è un numero decimale
                dato = float(dato)
            self.__collezione.append(dato)

    def ottieni_unici(self):
        """Restituisce una lista di elementi senza duplicati multipli, mantenendo solo la prima occorrenza."""
        unici = []
        for elemento in self.__collezione:
            if elemento not in unici:  # Aggiunge solo se l'elemento non è già presente
                unici.append(elemento)
        return unici

    def stampa_senza_ripetizioni(self):
        """Stampa tutti gli elementi nella collezione senza duplicati multipli."""
        unici = self.ottieni_unici()
        print("Elementi unici:", unici)

    def stampa_collezione(self):
        """Stampa l'intera collezione (solo per verifica)."""
        print("Intera collezione:", self.__collezione)


# Esempio di utilizzo
raccoglitore = RaccoglitoreDati()

# Richiesta di inserire i dati
ripetizioni = int(input("Quante volte vuoi ripetere l'operazione di inserimento dati? "))
for _ in range(ripetizioni):
    numero_di_dati = int(input("Quanti dati vuoi inserire in questa ripetizione? "))
    raccoglitore.aggiungi_dati(numero_di_dati)

# Stampa degli elementi unici
raccoglitore.stampa_senza_ripetizioni()

# (Opzionale) Stampa dell'intera collezione per verifica
# raccoglitore.stampa_collezione()
