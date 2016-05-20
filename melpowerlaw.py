#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kody <kody@kodick>
#
# Distributed under terms of the MIT license.

""" Using the powerlaw package to do analysis of The Anatomy of Melancholy. """
""" We use the steps given in Clauset,Shalizi,Newman (2007) for the analysis."""

from collections import Counter
from math import log
import powerlaw
import numpy as np
import matplotlib.pyplot as plt

file = "TAM.txt"

with open(file) as mel:
    contents = mel.read()
    words = contents.split()

""" Gives a list of tuples of most common words with frequencies """
comm = Counter(words).most_common(20000)

""" Isolate the words and frequencies and also assign ranks to the words """
labels = [i[0] for i in comm]
values = [i[1] for i in comm]
ranks = [labels.index(i)+1 for i in labels]

""" Step 1 : Estimate x_min and alpha """
fit= powerlaw.Fit(values, discrete=True)
alpha = fit.alpha
x_min = fit.xmin
print("\nxmin is: " ,x_min,)
print("Scaling parameter is: ",alpha,)

""" Step 1.5 : Visualization by plotting PDF, CDF and CCDF """
fig = fit.plot_pdf(color='b',original_data=True,linewidth=1.2)
fit.power_law.plot_pdf(color='b',linestyle='--',ax=fig)
fit.plot_ccdf(color='r', linewidth=1.2, ax=fig)
fit.power_law.plot_ccdf(color='r',linestyle='--',ax=fig)
plt.ylabel('PDF and CCDF')
plt.xlabel('Word Frequency')
plt.show()

""" Step 2&3 : Evaluating goodness of fit by this with candidate distribitions """
R1,p1 = fit.distribution_compare('power_law','stretched_exponential',normalized_ratio=True)
R2,p2 = fit.distribution_compare('power_law','exponential',normalized_ratio=True)
R3,p3 = fit.distribution_compare('power_law','lognormal_positive',normalized_ratio=True)
R4,p4 = fit.distribution_compare('power_law','lognormal',normalized_ratio=True)

print("Loglikelihood and p-value for stretched exponential: ",R1," ",p1,) 
print("Loglikelihood and p-value for exponential: ",R2," ",p2,)
print("Loglikelihood and p-value for lognormal positive: ",R3," ",p3,)
print("Loglikelihood and p-value for lognormal: ",R4," ",p4,)

""" One notices that lognormal and power_law are very close in their fit for the data."""
fig1 = fit.plot_ccdf(linewidth=2.5)
fit.power_law.plot_ccdf(ax=fig1,color='r',linestyle='--')
fit.lognormal.plot_ccdf(ax=fig1,color='g',linestyle='--')
plt.xlabel('Word Frequency')
plt.ylabel('CCDFs of data, power law and lognormal.')
plt.title('Comparison of CCDFs of data and fitted power law and lognormal distribitions.')
plt.show(fig1)