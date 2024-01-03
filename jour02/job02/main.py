class livre:
    def __init__(self, titre, auteur, page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def get_page(self):
        return self.__page
    
    def set_page(self, page):
        if isinstance(page, int) and page > 0:
            self.__page = page
        else:
            print("erreur : le nombre doit etre un entier positif")


    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté, impossible de le rendre.")
            

mon_livre = livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)
 
print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_page())


mon_livre.set_page(150)  
print("Nouveau nombre de pages:", mon_livre.get_page())

mon_livre.set_page("200")  
print("retour a la valeur initial :", mon_livre.get_page())

print("Le livre est disponible:", mon_livre.verification())


mon_livre.emprunter()

mon_livre.emprunter()

mon_livre.rendre()

mon_livre.rendre()