
# representation de l'objet

class Personne:

    def __init__(self, nom, prenom, age, residence):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.residence = residence

    def __str__(self):
        return "nom : {}, prenom: {}, age : {}, residence : {}".format(self.nom, self.prenom, self.age, self.residence)

    def __repr__(self):
        return str(self)

user = Personne("yeager", "eren", 23, "bab ezzouar")
print(user)


# addition

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def __repr__(self):
        return str(self)

    def __eq__(self, date):
        if type(date) is Date:
            return self.day == date.day and self.month == date.month and self.year == date.year
        else:
            print("on ne peut comparer que 2 Date")
            return False

    def __add__(self, date):
        if type(date) is Date:
            month = 0
            year = 0

            day = self.day + date.day
            if(day > 30):
                day -= 30
                month = 1

            month += (self.month + date.month)
            if(month > 12):
                month -= 12
                year += 1
            year += (self.year + date.year)
            return Date(day, month, year)
        else:
            print("on ne peut additioner que 2 Date")
            return None

# methodes de conteneur

class Conteneur:
    def __init__(self):
        self._dictionary = {}

    def __getitem__(self, index):
        print("acceder à l'element")
        return self._dictionary[index]

    def __setitem__(self, index, value):
        print("modifier à l'element")
        self._dictionary[index] = value

    def __delitem__(self, index):
        print("supprimer l'element")
        del self._dictionary[index]

    def __contains__(self, value):
        print("tester si l'element existe")
        return value in self._dictionary

import pdb; pdb.set_trace()
