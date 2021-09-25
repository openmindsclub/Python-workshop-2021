
# exemple lire et ecrire dans un fichier
file = open('test_file.txt', 'r')
string = file.read()
file.close()
print(string)

file = open('test_file.txt', 'w')
file.write(string + "\nCe fichier a etait modifer")
file.close()


# WITH

with open('test_file.txt', 'r') as file:
    string = file.read()
    print(string)

with open('test_file.txt', 'w') as file:
    file.write(string + "\nCe fichier a etait modifer")

# serialisation

import pickle

score = {
    "joueur 1" : 56,
    "joueur 2" : 58,
    "joueur 3" : 49,
}

# enregistrer
with open('score_file', 'wb') as file:
    my_pickler = pickle.Pickler(file)
    my_pickler.dump(score)

# recuperer
with open('score_file', 'rb') as file:
    my_unpickler = pickle.Unpickler(file)
    score_recuperer = my_unpickler.load()


# serialisation de nos propre objets

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



class Foo(object):

  def __init__(self, val=2):
     self.val = val

  def __getstate__(self):
     print("I'm being pickled")
     self.val *= 2
     return self.__dict__

  def __setstate__(self, d):
     print("I'm being unpickled with these values: " + repr(d))
     self.__dict__ = d
     self.val *= 3

import pickle
f = Foo()
f_data = pickle.dumps(f)
f_new = pickle.loads(f_data)
