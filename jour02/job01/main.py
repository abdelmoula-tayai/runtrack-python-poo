class rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur

mon_rectangle = rectangle(10, 6)

print("Longueur initiale:", mon_rectangle.get_longueur())
print("Largeur initiale:", mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Vérification des modifications
print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())
 
        