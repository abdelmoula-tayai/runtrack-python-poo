class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Produit : {self.nom}\nPrix HT : {self.prixHT} euros\nTVA : {self.TVA}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit("Livre", 15.0, 5)
produit2 = Produit("Ordinateur", 1200.0, 20)
produit3 = Produit("Téléphone", 500.0, 10)


produit1.afficher()
produit2.afficher()
produit3.afficher()


produit1.modifierNom("Roman")
produit1.modifierPrix(20.0)

produit2.modifierNom("Laptop")
produit2.modifierPrix(1500.0)

produit3.modifierNom("Smartphone")
produit3.modifierPrix(600.0)


produit1.afficher()
produit2.afficher()
produit3.afficher()
