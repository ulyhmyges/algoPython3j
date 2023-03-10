from datetime import date

class Commande:
    def __init__(self, numero, prix = 0, date = date.today()):
        self.date = date
        self.numero = numero
        self.prix = prix

    def calculTVA(self):
        self.prix = self.prix * 1.196
        return self.prix

    def __add__(self, other):
        if self.numero >= other.numero:
            numero = self.numero + 1
            date = self.date
        else:
            numero = other.numero + 1
            date = other.date
        prix = self.prix + other.prix
        return Commande(numero, prix, date)


    def __str__(self):
        return "Commande:\nDate: {}\nNuméro: {}\nPrix: {:.2f} euros".format(self.date, self.numero, self.prix)

    def get_date(self):
        return self.date

    def get_numero(self):
        return self.numero

    def get_prix(self):
        return self.prix

    def set_date(self, date):
        self.date = date

    def set_numero(self, numero):
        self.numero = numero

    def set_prix(self, prix):
        self.prix = prix
