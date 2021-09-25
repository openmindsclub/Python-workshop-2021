# ces exemples sont inspirer de ce tutoriel https://gist.github.com/Zearin/2f40b7b9cfc51132851a


# comprendre que les fonctions sont des objets

def shout(word='yes'):
    return word.capitalize() + '!'

print(shout())

scream = shout

print(scream())

del shout
try:
    print(shout())
except NameError as e:
    print e

print(scream())


#####################################################################

def talk():
    def whisper(word='yes'):
        return word.lower() + '...'

    print whisper()

talk()

try:
    print whisper()
except NameError as e:
    print e
    Python's functions are objects



#####################################################################

def getTalk():
    def shout(word='yes'):
        return word.capitalize() + '!'

    return shout

talk = getTalk()
print talk
print talk()

print getTalk()()


def doSomethingBefore(func):
    print 'I do something before then I call the function you gave me'
    var = func()

doSomethingBefore(talk)
