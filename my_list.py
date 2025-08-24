#make an empty list named my_list
my_list = []
print('Empty list: ', my_list)

#add elements 10, 20, 30, 40 to my_list using append function, this has to be done one argument at a time
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('Appended list: ', my_list)

#insert value 15 at second position in my_list
my_list.insert(1, 15)
print('My_list after inserting 15 at index 1:', my_list)

# extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print('My_list after extend:', my_list)

# remove the last element 
last_element = my_list.pop()      
print('Removed last element:', last_element)
print('My_list after pop:', my_list)

# sort my_list in ascending order
my_list.sort()            
print('My_list sorted in ascending fashion:', my_list)

# find and print the index of value 30
index_30 = my_list.index(30)
print('Index of 30:', index_30)