class ListaNumeri:
    def __init__(self):
        self.lista = []

    def valorizza_lista(self):
        for i in range(5):
            while True:
                
                numero = float(input(f"Inserisci il numero {i+1}: "))
                self.lista.append(numero)
                break  # Uscita dal ciclo quando il dato è valido
            print("Per favore, inserisci un numero valido.")

    def confronta(self, altra_lista):
        if len(self.lista) != 5 or len(altra_lista.lista) != 5:
            print("Entrambe le liste devono contenere 5 numeri.")
            return []
        risultato = []
        for i in range(5):
            somma = self.lista[i] + altra_lista.lista[i]
            risultato.append(somma)
        return risultato


def main():
    # Creazione degli oggetti che contengono le due liste
    lista1 = ListaNumeri()
    lista2 = ListaNumeri()

    # Valorizzazione delle liste
    print("Valorizza la prima lista:")
    lista1.valorizza_lista()

    print("\nValorizza la seconda lista:")
    lista2.valorizza_lista()

    # Confronto delle due liste (somma delle posizioni corrispondenti)
    risultato = lista1.confronta(lista2)

    # Stampa dei risultati
    if risultato:
        print("\nRisultato della somma delle liste:")
        for i in range(5):
            print(f"Posizione {i+1}: {lista1.lista[i]} + {lista2.lista[i]} = {risultato[i]}")

    # Domanda se ripetere l'operazione
    ripeti = input("\nVuoi ripetere l'operazione? (sì/no): ").strip().lower()
    if ripeti == 'sì':
        main()  # Ripete l'intero processo



main()
