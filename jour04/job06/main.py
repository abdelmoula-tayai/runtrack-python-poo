class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}$")
        
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")
        
    def demarrer(self):
        print("Attention, je roule")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        print(f"Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\nNombre de roues = {self.roues}")

    def demarrer(self):
        print("Attention, je roule")


voiture1 = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)
voiture1.informationsVehicule()
voiture1.demarrer()


moto1 = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)
moto1.informationsVehicule()
moto1.demarrer()


