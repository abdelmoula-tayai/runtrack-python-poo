class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 10  # Valeur arbitraire pour l'exemple

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        self.niveau = input("Choisissez le niveau de difficulté (facile, moyen, difficile): ")

    def lancerJeu(self):
        if self.niveau == "facile":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)
        elif self.niveau == "moyen":
            joueur = Personnage("Joueur", 80)
            ennemi = Personnage("Ennemi", 60)
        elif self.niveau == "difficile":
            joueur = Personnage("Joueur", 60)
            ennemi = Personnage("Ennemi", 80)
        else:
            print("Niveau non valide. Choisissez entre facile, moyen ou difficile.")
            return

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)
            self.verifierSante(joueur, ennemi)

        self.verifierGagnant(joueur, ennemi)

    def verifierSante(self, joueur, ennemi):
        print(f"{joueur.nom} - Vie: {joueur.vie} | {ennemi.nom} - Vie: {ennemi.vie}")

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie <= 0:
            print(f"{ennemi.nom} a gagné!")
        elif ennemi.vie <= 0:
            print(f"{joueur.nom} a gagné!")

# Exemple d'utilisation
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

        
        