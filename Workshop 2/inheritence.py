class Personne:
    MAX_USERS = 2000
    NB_USERS = 0
    def __init__(self, nom, prenom, age, residence):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence
        Personne.NB_USERS += 1

    def est_mineur(self):
        return self.age < 18

    @classmethod
    def check_users(cls):
        if Personne.NB_USERS >= Personne.MAX_USERS:
            print("database full, we must free some space")
        else:
            print("there is ennough space")


class Client(Personne):

    def __init__(self, nom, prenom, age, residence, num_client):
        super().__init__(nom, prenom, age, residence)
        self.num_client = num_client

    def acheter_produit(self):
        print("le client {} à acheter un produit".format(self.num_client))

class Employer(Personne):

    def __init__(self, nom, prenom, age, residence, poste, salaire):
        super().__init__(nom, prenom, age, residence)
        self.poste = poste
        self.salaire = salaire

    def virer(self):
        print("vous etes virer")


user1 = Client("khouas", "aymen", 23, "bab ezzouar", 10)
#user2 = Client("jeager", "eren", 21, "somewhere", 20)

#user2 = Client("jeager", "eren", 21, "somewhere", 'gardient de securiter', )

import pdb; pdb.set_trace()
