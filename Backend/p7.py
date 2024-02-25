import random
import string

def generateur_mot_de_passe():
    longueur_mot_de_passe = int(input("Entrez la longueur du mot de passe : "))

    caracteres = string.ascii_letters + string.digits + string.punctuation

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur_mot_de_passe))

    print(f"Votre mot de passe aléatoire : {mot_de_passe}")

if __name__ == "__main__":
    generateur_mot_de_passe()