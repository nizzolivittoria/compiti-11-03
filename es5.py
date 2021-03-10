class Prodotto:
    def __init__(self , nome,  numero , provenienza, prezzo):
        self.nome = nome
        self.numero = numero
        self.prezzo = prezzo
        self.provenienza = provenienza

    def assegna_prezzo(self):
        self.prezzo = self.prezzo*self.numero

    def informazioni(self):
        print("il prodotto" , self.nome , "viene prodotto in" , self.provenienza , "e il suo prezzo è di" , self.prezzo , "€")

p1 = Prodotto("libro" , 3 ,"Francia" , 4)
p1.assegna_prezzo()
p1.informazioni()
