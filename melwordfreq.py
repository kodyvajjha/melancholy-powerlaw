"""Let us look at the word frequency in The Anatomy of Melancholy"""

from collections import Counter
from math import log
import numpy as np
import matplotlib.pyplot as plt

file = "TAM.txt"

with open(file) as mel:
       contents = mel.read()
       words = contents.split()

"""gives a list of tuples of most common words with frequencies."""
comm = Counter(words).most_common(1000)

""" Isolate the words and frequencies and also assign ranks to the words. """
labels = [i[0] for i in comm]
values = [i[1] for i in comm]
ranks = [labels.index(i)+1 for i in labels]


indexes = np.arange(len(labels))
width = 0.2

"""Histogram of word frequencies"""
plt.title("Frequency of words in 'The Anatomy of Melancholy' ")
plt.xlabel("Ranked words")
plt.ylabel("Frequency")
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels, rotation='vertical')
plt.show()

""" Log-Log graph of ranks and frequencies """

logvals=[log(x) for x in values]
logranks=[log(x) for x in ranks]

plt.title("Log-Log graph of ranks and frequencies of words in 'The Anatomy of Melancholy' ")
plt.xlabel("logranks")
plt.ylabel("logvals")
plt.scatter(logranks,logvals)
plt.show()
