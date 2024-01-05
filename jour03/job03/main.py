class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée de la liste.")
        else:
            print(f"Tâche '{tache.titre}' non trouvée dans la liste.")

    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.statut = "Terminée"
            print(f"Tâche '{tache.titre}' marquée comme terminée.")
        else:
            print(f"Tâche '{tache.titre}' non trouvée dans la liste.")

    def afficherListe(self):
        print("Liste des tâches:")
        for tache in self.taches:
            print(f"{tache.titre} - {tache.statut}")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list


tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser", "aller s'entrainer")


liste_taches = ListeDeTaches()


liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)


liste_taches.afficherListe()


liste_taches.marquerCommeFinie(tache1)


taches_a_faire = liste_taches.filterListe("À faire")
print("Tâches à faire:")
for tache in taches_a_faire:
    print(f"{tache.titre} - {tache.statut}")


liste_taches.supprimerTache(tache2)


liste_taches.afficherListe()
