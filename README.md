# melancholy-powerlaw

This is an attempt to check if the distribution of the frequency of words in Richard Burton's "The Anatomy of Melancholy" follows
a power law such a Zipf's law. 

All the statistics has been inspired by Clauset,Shalizi,Newman (2007). The python package 'python-powerlaw' has been used. 

In conclusion it has been noted that for the observed data, a power-law with a scaling factor of approximately 2.10 performs only
slightly better than a lognormal distribution.  

The files are as follows :

melancholy.py is an interactive toy script which gives you the option of seeing the most frequent words in The Anatomy of Melancholy.

melwordfreq.py gives the initial investigation into the data with a histogram of the word frequencies as well as a log-log plot.

melpowerlaw.py contains most of the hardcore stat with an estimation of the quantity x_min and the scaling parameter alpha. It also contains plots for the Complementary Cumulative Distribution Function for the fitted power law. Also, as a final step, it includes by comparing the fitted power law with other distributions such as exponential, stretched exponential, positive lognormal and lognormal respectively. From this it is concluded that the lognormal distribution is the one which comes closest to the fitted power law.
