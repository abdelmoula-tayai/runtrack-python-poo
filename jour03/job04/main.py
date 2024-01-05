class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but!")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive!")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge!")

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} - Numéro {self.numero}, Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"{joueur.nom} a rejoint l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()


joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Modric", 8, "Milieu")


equipe1 = Equipe("Barcelona")
equipe2 = Equipe("Real Madrid")


equipe1.ajouterJoueur(joueur1)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Modric", "passe")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "carton_jaune")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

print("ce script a mis fin au debat sur l'ovni messi et l'eternel second ronaldo")


