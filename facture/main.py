# This is a sample Python script.
from facture.client import Client
from facture.commande import Commande
from datetime import date

from facture.commandeAcquittee import CommandeAcquittee


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mario = Client("Mario", "Nintendo")
    assert mario.__str__() == "Nom: Mario\nAdresse: Nintendo"
    c1 = Commande(1, 20, date.fromisoformat("2021-03-02"))
    assert c1.get_date() == date.fromisoformat("2021-03-02")
    assert c1.get_prix() == 20
    assert c1.get_numero() == 1
    print(date.fromisoformat("2023-03-02"))
    c2 = Commande(8, 50, date.fromisoformat("2023-03-02"))
    print(c2)
    print(c1.__add__(c2))
    print(CommandeAcquittee.acquitter(c2).get_datePaiement())
