class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def AfficherLesPoints(self):
        print(f"les coordonees du point sont: {self.x} {self.y}")
    
    def AfficherX(self):
        print(f"valeur de X: {self.x}")
    
    def AfficherX(self):
        print(f"valeur de y: {self.y}")
        
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
        
    def changerX(self, nouvelle_valeur_y):
        self.x = nouvelle_valeur_y
        
Point1 = Point(3, 5)
Point1.AfficherLesPoints()
        
        
        