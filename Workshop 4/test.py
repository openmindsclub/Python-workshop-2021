
class Personne:
    MAX_USERS = 2000
    NB_USERS = 0
    def __init__(self, nom, prenom, age, residence):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence
        Personne.NB_USERS += 1

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d

my_class = Personne

user = my_class("yeager", "eren", 23, "bab ezzouar")

import pdb; pdb.set_trace()
