iterator = iter("hello world")
next(iterator)


class Reverse:
    """Un itérateur permettant de parcourir une chaîne de la dernière lettre
    à la première. On stocke dans des attributs la position courante et la
    chaîne à parcourir"""

    def __init__(self, chaine_a_parcourir):
        """On se positionne à la fin de la chaîne"""
        self.chaine_a_parcourir = chaine_a_parcourir


    def __iter__(self):
        self.position = len(self.chaine_a_parcourir)
        return self

    def __next__(self):
        """Cette méthode doit renvoyer l'élément suivant dans le parcours,
        ou lever l'exception 'StopIteration' si le parcours est fini"""

        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]

obj = Reverse("hello world")
for i in obj:
    print(i)



# generators

def simple_gen():
    print ("before")
    yield 1
    print ("after 1")
    yield 2
    print ("after 2")
    yield 3
    print ("after 3")

iterator = iter(simple_gen())
next(iterator)
next(iterator)
next(iterator)
next(iterator)

for nombre in simple_gen(): # on exécute la fonction
    print(nombre)


import pdb; pdb.set_trace()
