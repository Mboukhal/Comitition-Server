import random

def jeu_devinette_nombre():
    nombre_secret = random.randint(1, 10)
    tentative = 0

    print("Devinez le nombre (entre 1 et 10) : ")

    while True:
        guess = int(input())
        tentative += 1

        if guess == nombre_secret:
            print(f"Félicitations ! Vous avez deviné le nombre en {tentative} tentatives.")
            break
        elif guess < nombre_secret:
            print("Trop bas ! Réessayez.")
        else:
            print("Trop élevé ! Réessayez.")

jeu_devinette_nombre()
