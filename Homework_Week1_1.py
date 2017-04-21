#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:40:55 2017

@author: shivamchaturvedi
"""

#In this five-part exercise, we will count the frequency of each letter in a given string.

#-------------------------------------------------

#1a
#The lower and upper cases of the English alphabet is stored as alphabet using the attribute ascii_letters
#from string library (module) where we will store them in alphabet after defining a given sentence

import string

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

alphabet = string.ascii_letters
#-------------------------------------------------

#1b
#Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'. 
#Create a dictionary count_letters with keys consisting of each unique letter in the sentence
#and values consisting of the number of times each letter is used in this sentence.

count_letters = {}
          
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

#print(count_letters.keys())
#print(count_letters.values())
#-------------------------------------------------

#1c 
#Rewrite your code from 1b to make a function called counter that takes a string input_string 
#and returns a dictionary of letter counts count_letters. If you were unable to complete 1b, 
#you can use the solution by selecting Show Answer. Use your function to call counter(sentence).

def counter (input_string):
    count_letters = {}
    for letter in input_string:
        if letter in count_letters:
                count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters

        #print(counter(sentence))

#-------------------------------------------------

#1d
#Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address 
#has been stored as address, and the counter function defined in part 1c has been loaded. 
#Use these to return a dictionary consisting of the count of each letter in this address, 
#and save this as address_count. Print address_count.

address = '1863 Gettysburg'

address_count = counter(address)

#print(address_count)

#-------------------------------------------------

#1e
#What is the most common letter used in the Gettysburg Address?
#Store this letter as most_frequent_letter, and print your answer.

from collections import Counter

most_frequent_letter = Counter(address).most_common(1)

print(most_frequent_letter)



#Another way to solve it (this solution returns the most common LETTER only without its iteration number)

maximum = 0
letter_maximum = ""
for letter in address_count:
    if address_count[letter] > maximum:
        maximum = address_count[letter]
        most_frequent_letter = letter

print(most_frequent_letter)
