# Author: Henri Nzatse
# Date: 09/23/2022
# This Program determines the year in which we are in 

year = int(input('Enter a year: '))

while year != 0:
    if year <= -45:
        print('The leap year calendar was not yet created')
    elif year % 4 == 0 : 
        print('Leap Year')
    elif year % 400 == 0 :
        print('Leap Year')
    else:
        print('not a Leap Year')
    break

# num = int(input(">: "))

# # Even number
# for i in range(1,num +1):
#     if i % 2 == 0:
#         print(i)
        
# # Odd numbers
# for i in range(1,num +1):
#     if i % 2 == 1:
#         print(i)
        
# # Prime numbers
# for i in range(1,num +1):
#     if num % i == 0:
#         print(i)
#     else:
#         print("False")

# # break statement
# for ch in "john.smith@pythonistitute.org":
#     if ch == "@":
#         break
#     print(ch)
