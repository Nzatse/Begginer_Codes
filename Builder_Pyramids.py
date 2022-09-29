# Author: Henri Nzatse
# Date: 09/23/2022
"""
Your task is to write a program which 
reads the number of blocks the builders have, 
and outputs the height of the pyramid that can be 
built using these blocks.
"""
# Create Local variable and assign values to them
blocks = int(input("Enter the number of blocks: "))
height = 0
layers = 1

# Create a loop that will iterate through the number of blocks
while layers <= blocks:
    height += 1
    blocks -= layers
    layers += 1
    
# Print the result
print("The height of the pyramid:", height)