# Author: Henri Nzatse
# Date: 09/23/2022
# This program ask a user the number of items he wishes to have in hi/her list
# Iterate in the list and find the desired location where the number being search is found.

list = []
len_num = int(input('Enter the length of data: '))
for i in range(len_num):
    i = int(input('Enter a number: '))
    list.append(i)
to_find = int(input("Enter a number to find: "))
found = False
for x in range(len(list)):
    found = list[x] == to_find
    if found:
        break
if found:
    print('Element found at index', x)
else:
    print('Absent')
    
# This program will tell the number of time you have correct
# This can be a sample skeleton

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)

# Remove duplicate
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# rmv_list = []

# for i in my_list:
#     if i not in rmv_list:
#         rmv_list.append(i)
# my_list = rmv_list
# #
# print("The list with unique elements only:")
# print(my_list)
