from facture.commande import Commande
from datetime import date

class CommandeAcquittee(Commande):
    def __init__(self, numero, prix = 0, date = date.today(), datePaiement = date.today()):
        super().__init__(numero, prix = 0, date = date.today())
        self.datePaiement = datePaiement

    def acquitter(commande):
       return CommandeAcquittee(commande.numero, commande.prix)

    def get_datePaiement(self):
        return self.datePaiement

    def set_datePaiement(self, datePaiement):
        self.datePaiement = datePaiement

    def __str__(self):
        return super().__str__() + "\nDate de paiement: " + self.datePaiement

