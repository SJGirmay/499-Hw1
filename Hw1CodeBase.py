from nltk.tokenize import sent_tokenize, word_tokenize
import re
from operator import itemgetter
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
from itertools import islice

with open("hamlet.txt") as inp:
    lines = inp.readlines()

#1.A#Ans:2355
listToStr = ' '.join([str(elem) for elem in lines]) 
#print(len(sent_tokenize(listToStr)))
#1.B #Ans:29605
splitLines = listToStr.strip().split()
#print(len(splitLines))
#1.C#Ans:36421
wordTok = word_tokenize(listToStr)
#print(len(word_tokenize(listToStr)))
#1.D#Ans:#Tokens:36421#Types:4807
listToStr = listToStr.lower()
wordTok = word_tokenize(listToStr)
#print(len(set(wordTok)))

#build dict of words based on frequency
frequency = {}
for word in wordTok:
    count = frequency.get(word,0)
    frequency[word] = count + 1

n = 1000
frequency = {key:value for key,value in islice(frequency.items(), 0, n)}
s = np.fromiter(frequency.values(), dtype=float)

#Calculate zipf and plot the data
a = 2. #  distribution parameter
count, bins, ignored = plt.hist(s[s<30], 30, density=True)
x = np.arange(1., 50.)
y = x**(-a) / special.zetac(a)
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()





