class Ville:
    def __init__(self, nom, habitants):
        self.nom = nom
        self._habitants = habitants

    def get_nombre_habitants(self):
        return self._habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville._habitants += 1

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"population de la ville de {paris.nom}: {paris.get_nombre_habitants()} habitants")
print(f"population de la ville de {marseille.nom}: {marseille.get_nombre_habitants()} habitants")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"mise a jour de la population de la ville de {paris.nom} {paris.get_nombre_habitants()} habitants")
print(f"mise a jour de la population de la ville de {marseille.nom} {marseille.get_nombre_habitants()} habitants")

        