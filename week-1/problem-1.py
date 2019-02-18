# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:22:28 2019

@author: Daniil Merkulov
"""
s = "azcbobobegghakl"

count_vowels = 0
for letter in s:
    count_vowels += 1 if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" else 0

print("Number of vowels:", count_vowels)