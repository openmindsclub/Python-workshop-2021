
# class method vs static method

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

    @staticmethod
    def print_user():
        print("{}, {}, {}, {}".format(personne.nom, personne.prenom, personne.age, personne.residence))

user = Personne("yeager", "eren", 23, "bab ezzouar")

# encapsulation

class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self.__prenom = prenom

    def changer_prenom(self, prenom):
        print(self.__prenom)
        self.__prenom = prenom

user = Personne("yeager", "eren")


# proprieter

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            print("Temperature below -273.15 is not possible")
        self._temperature = value

    # proprieter
    temperature = property(fget=get_temperature, fset=set_temperature)

temp = Celsius()
print(temp.temperature)
temp.temperature = 20
print(temp.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            print("Temperature below -273.15 is not possible")
        self._temperature = value

temp = Celsius()
print(temp.temperature)
temp.temperature = 20
print(temp.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit_temp(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            print("Temperature below -273.15 is not possible")
        self._temperature = value


class Rectangle:
    def __init__(self, longeur, largeur):
        self._longeur = longeur
        self._largeur = largeur

    @property
    def surface(self):
        return self._longeur * self._largeur

rect = Rectangle(4, 2)

import pdb; pdb.set_trace()
