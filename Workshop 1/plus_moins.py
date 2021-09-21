import random

def choose_number(born_inf, born_sup):
    n = -1
    while n < born_inf or n > born_sup:
        n = input("Tapez un nombre (entre " + str(born_inf) + " et "+ str(born_sup) + " )... ")
        n = int(n) # plus tard on vas ajouter essayer de catch l'exeption de cette partie
        if n < born_inf:
            print("Ce nombre est inferieur à" + str(born_inf))
        if n > born_sup:
            print("Ce nombre est supérieur à" + str(born_sup))
    return n

def plus_moins():
    max_num = 100
    min_num = 0
    nb_max_dessaie = 10

    random_number = random.randrange(min_num, max_num)
    reponse_trouver = False
    essaie = 0

    while not reponse_trouver and essaie < nb_max_dessaie:
        essaie += 1
        n = choose_number(min_num, max_num)
        if n == random_number:
            print("Felicitation, solution trouver en " + str(essaie) + " essaies")
            reponse_trouver = True
        elif n < random_number:
            print("c'est plus ")
        else:
            print("c'est moins ")

    if not reponse_trouver:
        print("malheureusement vous avez perdus essayer une prochaine fois!!")


if __name__ == '__main__':
    plus_moins()
