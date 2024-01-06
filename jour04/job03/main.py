class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, value):
        self._largeur = value

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        self._hauteur = value

    def volume(self):
        return self._longueur * self._largeur * self._hauteur



rectangle1 = Rectangle(longueur=5, largeur=3)

print("Périmètre du rectangle:", rectangle1.perimetre())
print("Surface du rectangle:", rectangle1.surface())


parallelepipede1 = Parallelepipede(longueur=4, largeur=2, hauteur=3)


print("Volume du parallélépipède:", parallelepipede1.volume())
