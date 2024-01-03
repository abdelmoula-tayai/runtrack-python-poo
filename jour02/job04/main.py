class Student:
    def __init__(self, nom, prenom, id_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etudiant = id_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_id_etudiant(self):
        return self.__id_etudiant

    def set_id_etudiant(self, id_etudiant):
        self.__id_etudiant = id_etudiant

    def get_credits(self):
        return self.__credits

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            print(f"{nombre_credits} crédits ajoutés avec succès.")
            self.__level = self.__studentEval()  # Mise à jour du niveau après l'ajout de crédits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom = {self.__prenom}") 
        print(f"prenom = {self.__nom}")
        print(f"id = {self.__id_etudiant}")
        print(f"Niveau: {self.__level}")

john_doe = Student("Doe", "John", 145, 90)

print(f"Le nombre de credit de {john_doe.get_prenom()} {john_doe.get_nom()} est de : {john_doe.get_credits()}")

john_doe.studentInfo()

