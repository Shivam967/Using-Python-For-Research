#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 00:40:40 2017

@author: shivamchaturvedi
"""

'''
====================================================
Case Study 2 - Word Frequency Distribution in Hamlet
====================================================
'''

#In this case study, we will find and plot the distribution of word frequencies for each translation of Hamlet. 
#Perhaps the distribution of word frequencies of Hamlet depends on the translation --- let's find out!

#For these exercises, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x).

#Define functions
#------------------

from collections import Counter

def count_words_fast(text):
    """count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations"""
    text = text.lower() #lowercase for the counting letters so the function can cont the same words whether it's capatilised or not
    skips = [".", ",", ";", ":", "'", '"'] #skipping all the punctuations to not be counted with the words that come bfore them
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts

#------------------
def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

#------------------
def word_stats(word_counts):
   """return the number of unique words and word frequencies"""
   num_unique = len(word_counts) #calculate the number of unique words in the text
   counts = word_counts.values() #calculate the frequency of each word in the text
   return(num_unique,counts)

#----------------------------------------------------------------------------------------------------------------


# Exercise 1
#-----------

#TODO: Write a function word_count_distribution(text) that takes a book string and returns a dictionary with items 
#corresponding to the count of times a collection of words appears in the translation, and values corresponding to 
#the number of number of words that appear with that frequency.

#TODO: First use count_words_fast(text) to create a dictionary called word_counts with unique words in the dictionary 
#as keys and their frequency in the book as values.

#TODO: Next, create and return a new dictionary count_distribution with unique values from word_counts as keys and their 
#frequency as values. For example, 'you are what you eat' contains three words that occur once and one word that occurs twice, 
#so word_count_distribution('you are what you eat') should return a dictionary {1:3, 2:1}.

def word_count_distribution(text):
    word_counts = count_words_fast(text)
    count_distribution = dict(Counter(word_counts.values()))
    return count_distribution

#TODO: 'Romeo and Juliet' is preloaded as text. Call word_count_distribution(text), and save the result as distribution.

distribution = word_count_distribution(text) 

print(distribution)
#------------------------------------------------------------------------------

# Exercise 2
#-----------

#TODO: Create a function more_frequent(distribution) that takes a word frequency dictionary (like that made in Exercise 1)
# and outputs a dictionary with the same keys as those in distribution 
# (the number of times a group of words appears in the text), and values corresponding to the fraction of words that occur 
# with more frequency than that key.

import numpy as np

def more_frequent(distribution):
    counts = list(distribution.keys())
    frequency_of_counts = list(distribution.values())
    cumulative_frequencies = np.cumsum(frequency_of_counts)
    more_frequent = 1 - cumulative_frequencies / cumulative_frequencies[-1] #To obtain the fraction of words more frequent than this,
    #divide this cumulative sum by its maximum, and subtract this value from 1. 
    return dict(zip(counts, more_frequent))
    

#TODO: Call more_frequent(distribution).

more_frequent(distribution)   

#------------------------------------------------------------------------------

# Exercise 3
#-----------

#Edit the code used to read though each of the books in our library, and store 
#the word frequency distribution for each translation of William Shakespeare's 
#"Hamlet" as a Pandas dataframe hamlets with columns named "language" and 
#"distribution". word_count_distribution is preloaded from Exercise 1. 
#How many translations are there? Which languages are they translated into?

import pandas as pd

hamlets = pd.DataFrame(columns=('language','distribution'))

book_dir = "Books"
title_num = 1

for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text) 
                hamlets.loc[title_num] = language, distribution
                title_num += 1
                
#There are three translations: English, German, and Portuguese.

#------------------------------------------------------------------------------

# Exercise 4
#-----------

#Plot the word frequency distributions of each translations on a single log-log plot. 
#Note that we have already done most of the work for you. Do the distributions of each translation differ?

import matplotlib.pyplot as plt

colors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index+1], hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())),sorted(list(dist.values()),
        reverse = True), color = colors[index], linewidth = 2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim    = [0, 2e3]
xlabel  = "Frequency of Word $W$"
ylabel  = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc = "upper right", numpoints = 1)
plt.show()


#The distributions differ somewhat, but their basic shape is the same. 
#By the way, distributions that look like a straight line like these are called 
#'scale-free,' because the line looks the same no matter where on the x-axis you look!