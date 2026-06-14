import random

simple_list = ["sri","weer",1,4,2]

print(simple_list[0])
print(simple_list[-1])  # -1 is the last index of the list 

simple_list.extend(["HI","suuee"]) # adding new items into end of the list 
print(simple_list)

simple_list.append("tharindi") #add one item to end of list
print(simple_list)

simple_list.pop(1) #remove item from list by index 

print(simple_list)

random_index = random.choice(simple_list) # get random item from a list 

print(random_index)

#option two for pick random item from the list 
random_index= random.randint(0,4)
print(simple_list[random_index])

#Nested List 
list1 =["kandy","Colombo","ampara","Mathara"]

list =[list1,simple_list]

print(list)
