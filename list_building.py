# Author: Henri Nzatse
# Date: 09/23/2022
'''
Write a program that reflects these changes and lets you 
practice with the concept of lists. Your task is to:
1) step 1: create an empty list named beatles;
2) step 2: use the append() method to add the following members of the band 
 to the list: John Lennon, Paul McCartney, and George Harrison;
3) step 3: use the for loop and the append() method to prompt the user to 
 add the following members of the band to the list: 
 Stu Sutcliffe, and Pete Best;
4)step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
5) step 5: use the insert() method to add Ringo Starr to the beginning of the list.
6) By the way, are you a Beatles fan? 
    (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?)
'''


beatles = [] # Creates an empty List
print("Step 1:", beatles)

# Append values to the list
beatles.append("John Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Creates an iteration to add input to a list
for i in range(2):
    i = input("Enter a word: ")
    beatles.append(i)
print("Step 3:", beatles)

# Delete a list
del beatles[-2:]
print("Step 4:", beatles)

# insert at the beginning of the list
beatles.insert(0,'Ringo Star')
print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))

# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list

# print(create_list(5))