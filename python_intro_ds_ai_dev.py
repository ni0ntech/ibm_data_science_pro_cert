#-----------------------------------------------------------------------------------
# String interpolation is a way to insert variables into strings.
#-----------------------------------------------------------------------------------
#####################################################################################
#-----------------------------------------------------------------------------------
# String interpolation (f-strings):
#-----------------------------------------------------------------------------------

name = "Jack"
age = 30
#print(f"My name is {name} and I am {age} years old.")


#-----------------------------------------------------------------------------------
# str.format() method:
#-----------------------------------------------------------------------------------

name = "Jack"
age = 30
#print("My name is {} and I am {} years old.".format(name, age))


#-----------------------------------------------------------------------------------
# % Operator:
#-----------------------------------------------------------------------------------

name = "Jack"
age = 30
#print("My name is %s and I am %d years old." % (name, age))


#-----------------------------------------------------------------------------------
# % Additional capabilities:
#-----------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# Expression evaluation:
#------------------------------------------------------------------------------------

x = 10
y = 20
#print(f"The sum of x and y is {x+y}.")

#------------------------------------------------------------------------------------
# Raw String (r' ' ):
#------------------------------------------------------------------------------------

regular_string = "C:\new_folder\file.txt"
#print("Regular String:", regular_string)

raw_string = r"C:\new_folder\file.txt"
#print("Raw String:", raw_string)


#------------------------------------------------------------------------------------
# Lists and Tuples:
#------------------------------------------------------------------------------------
#####################################################################################
#------------------------------------------------------------------------------------
# Lists:
#------------------------------------------------------------------------------------

list = ["The Bodyguard", 7.0, 1992]

#print(list)
#print(list[-3])
#print(list[0])
#print(list[-2])
#print(list[1])
#print(list[-1])
#print(list[2])

list_content = ["The Bodyguard", 7.0, 1992, [1, 2], ("A", 1)]
#print(list_content)


#------------------------------------------------------------------------------------
# List Operations:
#------------------------------------------------------------------------------------

new_list = ["The Bodyguard", 7.0, 1992, "BG", 1]
#print(new_list)
#print(new_list[3:5])


#------------------------------------------------------------------------------------
# We can use the method extend to add new elements to the list:
#------------------------------------------------------------------------------------

new_list.extend(['pop', 10])
#print(new_list)


#------------------------------------------------------------------------------------
# Another similar method is append. If we apply append instead of extend, we add one
# element to the list:
#------------------------------------------------------------------------------------

new_list.append(['pop', 10])
#print(new_list)


#------------------------------------------------------------------------------------
# Each time we apply a method, the list changes. If we apply extend we add two new 
# elements to the list. The list L is then modified by adding two new elements:
#------------------------------------------------------------------------------------

new_list.extend(['pop', 10])
#print(new_list)


#------------------------------------------------------------------------------------
# If we append the list ['a','b'] we have one new element consisting of a nested list:
#------------------------------------------------------------------------------------

new_list.append(['a','b'])
#print(new_list)


#------------------------------------------------------------------------------------
# As lists are mutable, we can change them. For example, we can change the first 
# element as follows:
#------------------------------------------------------------------------------------

A = ["disco", 10, 1.2]
#print('Before change:', A)
A[0] = "hard rock"
#print('After change:', A)


#------------------------------------------------------------------------------------
# We can also delete an element of a list using the del command:
#------------------------------------------------------------------------------------

#print('Before change:', A)
del(A[0])
#print('After change:', A)


#------------------------------------------------------------------------------------
# We can convert a string to a list using split. For example, the method split 
# translates every group of characters separated by a space into an element in a list:
#------------------------------------------------------------------------------------

#print('hard rock'.split())


#------------------------------------------------------------------------------------
# We can use the split function to separate strings on a specific character which we 
# call a delimiter. We pass the character we would like to split on into the argument, 
# which in this case is a comma. The result is a list, and each element corresponds to 
# a set of characters that have been separated by a comma:
#------------------------------------------------------------------------------------

#print('A,B,C,D'.split(','))


#------------------------------------------------------------------------------------
# Copy and Clone List:
#------------------------------------------------------------------------------------

R = ["hard rock", 10, 1.2]
S = R
#print('R:', R)
#print('S:', S)


#------------------------------------------------------------------------------------
# Initially, the value of the first element in S is set as "hard rock". If we change 
# the first element in R to "banana", we get an unexpected side effect. As R and S are 
# referencing the same list, if we change list R, then list S also changes. If we 
# check the first element of S we get "banana" instead of "hard rock":
#------------------------------------------------------------------------------------

#print('S[0]:', S[0])
#R[0] = "banana"
#print('S[0]:', S[0])


#------------------------------------------------------------------------------------
# You can clone list R by using the following syntax:
#------------------------------------------------------------------------------------

S = R[:]
#print(S)

#print('S[0]:', S[0])
R[0] = "hard rock"
#print('S[0]:', S[0])










#------------------------------------------------------------------------------------
# Sets:
#------------------------------------------------------------------------------------

album_list = [ "The Bodyguard", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
#print(album_set)

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)