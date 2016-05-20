#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kody <kody@kodick>
#
# Distributed under terms of the MIT license.

"""
A series of experiments on Robert Burton's "The Anatomy of Melancholy"
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def anatomy(file):

    """"Count all words and count instances of a particular word."""
    print("To find the total number of words in TAM, press 1.")
    print("To find the total number of occurences of a particular word in TAM, press 2.")
    print("To find most common words in TAM, press 3.")

    try:
        with open(file) as mel:
            contents = mel.read()
    except FileNotFoundError:
            print("Sorry couldn't find the file!")
    else:
        words = contents.split()
        try:
            start=words.index("EDITION")
        except ValueError:
            print("Starting from the beginning")
            start=0
        num=int(input("\nEnter a number. "))
        if num == 1:
            print("Your book has about " + str(len(words[start:])) +" number of words.")
        if num == 2:
            givword=input("\nEnter a word you want to find the number of occurences of.\n")
            occs=words.count(givword)
            print("\n Your book has about " + str(occs) + " occurences of the word " + str(givword))
        if num == 3:
            lim=int(input("Enter the limit to the most common words."))
            l=Counter(words).most_common(lim)
            print(l)

filenames = ["TAM.txt"]

for file in filenames:
    anatomy(file)

