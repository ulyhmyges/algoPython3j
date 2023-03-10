class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def __str__(self):
        return "Nom: "+ self.nom +"\nAdresse: "+ self.adresse

    def contacter(self):
        print(self)

    def get_nom(self):
        return self.nom

    def get_adresse(self):
        return self.adresse

    def set_nom(self, nom):
        self.nom = nom

    def set_adresse(self, adresse):
        self.adresse = adresse