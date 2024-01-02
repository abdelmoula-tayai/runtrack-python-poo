class personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def SePresenter(self):
        return f"je suis {self.prenom} {self.nom}"

personne1 = personne("jhon", "doe")
personne2 = personne("abdou", "tayai")

print(personne1.SePresenter())
print(personne2.SePresenter())