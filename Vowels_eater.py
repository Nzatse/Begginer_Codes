# Author: Henri Nzatse
# Date: 09/23/2022
# This program removes vowels from words and print the result without vowels

# Create a variable to contain the words without vowels
# Create a variable to prompt the user to input the word
# Create another variable to host vowels

words_without_vowels = ""
user_input = input("Input a word: ")
vowels = ("a,e,i,o,u")

# Create a loop to run through the word
# create a condition that will catch vowels and continue if successful
# Continue without making another iteration 
# Assign the uncaught letter to words_without_vowels variable

for letter in user_input:
    if letter in vowels:
        continue
    words_without_vowels += letter
    
print(words_without_vowels)