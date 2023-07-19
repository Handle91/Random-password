import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

if __name__ == "__main__":
    longueur_mot_de_passe = int(input("Entrez la longueur du mot de passe désirée : "))
    mot_de_passe_genere = generer_mot_de_passe(longueur_mot_de_passe)
    print("Mot de passe généré:", mot_de_passe_genere)
