# Author: Henri Nzatse
# Date: 09/25/2022
'''
In 1937, a German mathematician named Lothar Collatz 
formulated an intriguing hypothesis (it still remains unproven) 
which can be described in the following way:
'''

user_input = int(input('Enter a non_negative/non_zero nuber: '))
c0 = user_input
count = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0/2)
        count += 1
        print(c0)
    else:
        c0 = int((3*c0) + 1)
        count += 1
        print(c0)
print("Steps = ", count)