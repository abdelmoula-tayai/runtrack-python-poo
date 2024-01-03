class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        if self.__statut_commande == "en cours":
            self.__plats_commandes = {}
            self.__statut_commande = "annulée"
            print("Commande annulée.")
        else:
            print("La commande ne peut pas être annulée, statut actuel:", self.__statut_commande)

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande} - Statut: {self.__statut_commande}")
        for plat, details in self.__plats_commandes.items():
            print(f"  - {plat}: {details['prix']} € ({details['statut']})")
        total = self.__calculer_total()
        tva = self.__calculer_tva()
        print(f"Total à payer: {total} € (TVA incluse: {tva} €)")

    def __calculer_tva(self):
        tva_taux = 0.2 
        total = self.__calculer_total()
        tva = total * tva_taux
        return round(tva, 2)


ma_commande = Commande(101)

ma_commande.ajouter_plat("Pâtes carbonara", 12.50)
ma_commande.ajouter_plat("Salade César", 8.75)
ma_commande.ajouter_plat("Tiramisu", 5.25)

ma_commande.afficher_commande()

ma_commande.annuler_commande()

ma_commande.afficher_commande()
