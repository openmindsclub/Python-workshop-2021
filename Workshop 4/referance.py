

my_list = [1,2,3]
new_list = my_list
new_list.append(4)

print(new_list) # output = [1,2,3,4]
print(my_list) # output = [1,2,3,4]

new_list is my_list # output = True

# How to copy the list with a different refferance

my_list = [1,2,3]
new_list = list(my_list) # my_list.copy()
new_list.append(4)


new_list is my_list # output = False

print(new_list) # output = [1,2,3,4]
print(my_list) # output = [1,2,3]
