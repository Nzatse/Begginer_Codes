# Author: Henri Nzatse
# Date: 09/27/2022
# This program enlist the number of prime number in a list

def is_prime(num):
    if num > 1:
        for x in range(2,num):
            if num % x == 0:
                return False
    else:
        return False
    return True

number = int(input('Enter a number: '))
for i in range(1, number):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


# number = int(input('Insert an Number: '))
# flag = False

# if number > 1:  
#     for i in range(2,number):
#         if (number % i) == 0:
#             flag = True
#             break
#     if flag:
#         print('Not Prime Number')
#     else:
#         print('Prime Number')