from random import randrange
from math import ceil

def choose_number(born_inf = 0, born_sup = 49):
    n = -1
    while n < born_inf or n > born_sup:
        n = input("Tapez un nombre (entre " + str(born_inf) + " et "+ str(born_sup) + " )... ")
        n = int(n) # plus tard on vas ajouter essayer de catch l'exeption de cette partie
        if n < born_inf:
            print("Ce nombre est inferieur à" + str(born_inf))
        if n > born_sup:
            print("Ce nombre est supérieur à" + str(born_sup))
    return n

def roulette():
    argent = 1000 # On a 1000 $ au début du jeu
    continuer = True

    print("montant initial", argent, "$.")

    while continuer:
        print("nombre a miser")
        nombre_mise = choose_number(born_inf = 0, born_sup = 49)
        print("mise")
        mise = choose_number(born_inf = 0, born_sup = argent)

        numero_gagnant = randrange(50)
        print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

        if numero_gagnant == nombre_mise:
            print("Félicitations ! Vous obtenez", mise * 3, "$ !")
            argent += mise * 3
        elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
            mise = ceil(mise * 0.5)
            print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
            argent += mise
        else:
            print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            argent -= mise

        if argent <= 0:
            print("Vous êtes ruiné ! C'est la fin de la partie.")
            continuer = False
        else:
            print("Vous avez à présent", argent, "$")

if __name__ == '__main__':
    roulette()
