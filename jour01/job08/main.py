import math

class cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def changer_rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def AfficherInfo(self):
        print(f"cercle de rayon {self.rayon}")
        
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon**2
    
    def diametre(self):
        return 2 * self.rayon
 
 
cercle1 = cercle(4)
cercle2 = cercle(7)
   
print("Cercle 1 :")
cercle1.AfficherInfo()
print("Circonférence :", cercle1.circonference())
print("Diamètre :", cercle1.diametre())
print("Aire :", cercle1.aire())

print("\nCercle 2 :")
cercle2.AfficherInfo()
print("Circonférence :", cercle2.circonference())
print("Diamètre :", cercle2.diametre())
print("Aire :", cercle2.aire())
        
        