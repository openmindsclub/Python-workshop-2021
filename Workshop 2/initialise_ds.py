# LIST

# initialiser une liste vide
my_list = []
# autre maniere d'initialiser une liste vide
my_list = list()
# initialiser une liste
my_list = [2, 5, "python"]

my_list = [2, 5, "python", 6]
my_list[:2]

for index, value in enumerate(my_list):
    print(index, value)

# TUPLE

# initialiser un tuple vide
my_tuple = ()
# autre maniere d'initialiser un tuple vide
my_tuple = tuple()
# initialiser un tuple
my_tuple = (2, 5, "python")
#  initialiser un tuple a partire d'une liste
my_tuple = tuple([1, 2, 5])


# Strings

# changer la valleur d'un caractere dans un String

my_string = "hello world"
# on remplace le ' ' par un '_'
my_string = my_string[:5] + "_" + my_string[6:]

my_string = "hello world"
# dans ce cas on peu aussi utiliser la methode replace
my_string = my_string.replace(" ", "_")


my_list = [1, 2]
my_list.append(3) # cette methode modifie directement la liste

my_string = "hello world"
my_string.replace(" ", "_") # cette methode ne modifie
# pas la chaine de caractere par contre elle retourne une nouvelle

# on doit donc assigner la valeur a une autre variable
# si on veut l'utilier
my_string = my_string.replace(" ", "_")


# DICT

# exemple
my_dictionary_user = {
    "pseudo" : "aymenkhs",
    "nom" : "khouas",
    "prenom" : "aymen",
    "age" : 23,
    "age" : 3,
}


my_dictionary = {}

my_dictionary = {"orange" : 2, "pomme": 3}

my_dictionary = dict()

my_dictionary = dict(orange=2, pomme=3, lemon=5)


# ajouter modifier une valleur

my_dictionary["bananas"] = 5


# parcourir un dictionnaire
for key in my_dictionary:
    print (key, my_dictionary[key])
