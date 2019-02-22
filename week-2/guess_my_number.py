# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:40:10 2019

@author: Nain
"""


low = 0
high = 100
guessed = False


print("Please think of a number between 0 and 100!")

while not guessed:
    
    ans = int((high+low)/2)
    
    print(f"Is your secret number {ans}?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if user_input == "c":
        print("Game over. Your secret number was:", ans)
        guessed = True
    elif user_input == "h":
        high = ans
    elif user_input == "l":
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    