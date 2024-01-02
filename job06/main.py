class animal:
    def __init__(self) :
        self.age = 0
        self.prenom = ""
        
    
    def viellir(self):
        self.age +=1
        print (f"age de l'animal: {self.age}")
        
    def nommer(self, prenom):
        self.prenom = prenom
    


animal_instance = animal()
print(f"age de l'animal: {animal_instance.age}")

animal_instance.viellir()

animal_instance.nommer("luna")

print(f"l'animal se nomme {animal_instance.prenom}")
