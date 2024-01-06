import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        return [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        return [self.paquet.pop(), self.paquet.pop()]

    def calculer_total(self, main):
        total = 0
        as_present = False

        for carte in main:
            if carte.valeur.isdigit():
                total += int(carte.valeur)
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_present = True
                total += 11  

        
        if as_present and total > 21:
            total -= 10

        return total

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        self.melanger_paquet()
        main_joueur = self.distribuer_cartes()
        main_croupier = self.distribuer_cartes()

        print("Main du joueur:")
        self.afficher_main(main_joueur)

        while True:
            choix = input("Voulez-vous prendre une carte ? (o/n): ").lower()
            if choix == 'o':
                main_joueur.append(self.paquet.pop())
                print("Main du joueur:")
                self.afficher_main(main_joueur)

                total_joueur = self.calculer_total(main_joueur)
                if total_joueur > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            elif choix == 'n':
                break
            else:
                print("Veuillez entrer 'o' ou 'n'.")

        total_joueur = self.calculer_total(main_joueur)
        print(f"Total du joueur: {total_joueur}")

        
        while self.calculer_total(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        print("\nMain du croupier:")
        self.afficher_main(main_croupier)
        total_croupier = self.calculer_total(main_croupier)
        print(f"Total du croupier: {total_croupier}")

    
        if total_joueur > 21 or (total_croupier <= 21 and total_croupier >= total_joueur):
            print("\nLe croupier gagne.")
        else:
            print("\nLe joueur gagne.")


jeu_blackjack = Jeu()
jeu_blackjack.jouer()

        