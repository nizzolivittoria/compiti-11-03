class atleta:
    def __init__(self , nome , altezza , sport , anni , squadra = 0 , visitaMedica = False):
        self.nome = nome
        self.sport = sport
        self.altezza = altezza
        self.anni = anni
        self.visitaMedica = visitaMedica
    def squadra (self , nome_squadra):
        self.squadra = nome_squadra
    def visualizza_dati(self):
        print("io sono un atleta e mi chiamo", self.nome, "sono alto", self.altezza, "metri, pratico", self.sport, "la mia squadra è", self.squadra, "e ho effettuato la visita medica")
    def effettua_visita(self):
        self.visitaMedica = True
a1 = atleta("Matteo", 1.85 , "calcio", 23)
a1.squadra ("Torino")
a1.visualizza_dati()
a1.effettua_visita()
