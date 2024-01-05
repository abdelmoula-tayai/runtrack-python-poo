class livre:
    def __init__(self, titre, auteur, page):
        self.__titre = titre
        self.__auteur = auteur
class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Compte {self._numero_compte} - {self._prenom} {self._nom}")

    def afficherSolde(self):
        print(f"Solde du compte {self._numero_compte}: {self._solde} €")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self._solde} €")

    def retrait(self, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self._solde} €")
        else:
            print("Opération impossible : solde insuffisant.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * taux_agios
            self._solde -= agios
            print(f"Agios appliqués. Nouveau solde : {self._solde} €")

    def virement(self, compte_dest, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_dest._numero_compte}.")
        else:
            print("Opération impossible : solde insuffisant.")

# Création d'une instance de CompteBancaire
compte1 = CompteBancaire("123456", "tayai", "abdou", 5000)

# Appels aux méthodes
compte1.afficher()
compte1.afficherSolde()
compte1.versement(2000)
compte1.retrait(1000)


compte2 = CompteBancaire("789012", "Durand", "Marie", -100, decouvert=True)

compte1.virement(compte2, 100)


compte2.agios(0.05)
