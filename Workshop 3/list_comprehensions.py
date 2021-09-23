
# list comprehension

my_list = [i for i in range(20)]
# code equivalent
my_list = []
for i in range(20):
    my_list.append(i)


number_list = [5, 10, 4, 52, 7, 81, 23]
even_list = [i for i in number_list if i % 2 == 0]
# code equivalent
number_list = [5, 10, 4, 52, 7, 81, 23]
even_list = []
for i in number_list:
    if i % 2 == 0:
        even_list.append(i)

number_list = [5, 10, 4, 52, 7, 81, 23]
even_list_strings = [strt(i) for i in number_list if i % 2 == 0]
# code equivalent
even_list = []
for i in number_list:
    if i % 2 == 0:
        even_list.append(str(i))

# Function with an infinity of parameters

def function(name ,*args):
    print(type(args))
    print(args)
    for value in args:
        print(value)

function(5, 1, 't')



def function(**named_args):
    print(type(named_args))
    print(named_args)
    for key in named_args:
        print("arg name : {}, value : {}".format(key , named_args[key]))

function(orange=2, pomme=3, bannanes=10)
