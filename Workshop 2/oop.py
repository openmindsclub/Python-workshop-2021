
# First class

class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""
    def __init__(self): # Notre méthode constructeur
        # (On definit les attributs de notre class
        # dans cette methode init)
        self.nom = "dfdf"
        self.prenom = "aymen"
        self.age = 23
        self.residence = "bab ezzouar"


# Instancier et accéder à l'objet

user = Personne()
print(user.nom)
print(user.prenom)


# Passer des attributs a nos class

class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self, nom, prenom, age, residence): # Notre méthode constructeur
        # (On definit les attributs de notre class
        # dans cette methode init)
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence

    def function(self):
        if self.age < 18:
            return 18 - self.age
        return False

# Instancier l'objet
user = Personne("khouas", "aymen", 23, "bab ezzouar")
user.function()

print(user.nom)
print(user.prenom)


# methodes

class Personne: # Définition de notre classe Personne
    def __init__(self, nom, prenom, age, residence): # Notre méthode constructeur
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence



user = Personne("khouas", "aymen", 23, "bab ezzouar")
print(user.est_mineur())


class Personne: # Définition de notre classe Personne
    NB_USERS = 0
    def __init__(self, nom, prenom, age, residence): # Notre méthode constructeur
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence
        Personne.NB_USERS += 1

    def est_mineur(self):
        Personne.NB_USERS = 0
        return self.age < 18


class Personne:
    MAX_USERS = 2000
    NB_USERS = 0
    def __init__(self, nom, prenom, age, residence):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence
        Personne.NB_USERS += 1

    @classmethod
    def check_users(cls):
        if Personne.NB_USERS >= Personne.MAX_USERS:
            print("database full, we must free some space")
        else:
            print("there is ennough space")
