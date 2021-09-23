
# forme basique

def division(nominateur, denominateur):
    try:
        result = nominateur / denominateur
    except:
        print("une erreur est survenue")



def division(nominateur, denominateur):

    try:
        result = nominateur / denominateur
    except ZeroDivisionError as e:
        print("une erreur est survenue \n:{}".format(e))

# plusieurs exceptions

def division():
    try:
        nominateur = int(input())
        denominateur = int(input())
        result = nominateur / denominateur
    except ZeroDivisionError as e:
        print("une erreur est survenue \n:{}".format(e))
    except ValueError as e:
        print("you gave a string \n:{}".format(e))


# finally and else
def division():
    try:
        nominateur = int(input())
        denominateur = int(input())
        result = nominateur / denominateur
    except ZeroDivisionError as e:
        print("une erreur est survenue \n:{}".format(e))
        return None
    except ValueError as e:
        print("une erreur est survenue \n:{}".format(e))
        return None
    else:
        print("Aucune erreur, good job")
    finally:
        print("Se code s'execute a la fin dans tous les cas")


# raise

def test_age(age):
    if age < 18:
        raise ValueError("vous ne pouvez pas continuer sur se site")

#assertions
var = 5
assert var == 8
assert var == 5


# create your own exceptions

class MilkBeforeCerealError(Exeptions):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# exemple

class MakingCereals:
    def __init__(self):
        self.cereal_done = False
        self.milk_done = False

    def adding_cereals(self):
        self.cereal_done = True

    def adding_milk(self):
        if self.cereal_done:
            self.milk_done = True
        else:
            raise MilkBeforeCerealError("WHAAATT!! NO YOU CAN'T JUST PUT THE MILK BEFORE THE CEREALS")

import pdb; pdb.set_trace()


class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.

    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""

    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)
