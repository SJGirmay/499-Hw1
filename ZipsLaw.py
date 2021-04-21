import re
from operator import itemgetter
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
from itertools import islice
from nltk.tokenize import sent_tokenize, word_tokenize

with open("gazetteer.eng-kin.txt", encoding="utf8") as inp:
    lines = inp.readlines()

engArr = []
kinArr = []

for l in lines:
    l = l.strip ().split('|||')
    eng = l[0].strip()
    engArr.append(eng)
    kin = l[1].strip()
    kinArr.append(kin)


 
def editDistance(eng, kin, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
 
    # If last characters of two strings are same, do nothing
    if eng[m-1] == kin[n-1]:
        return editDistance(eng, kin, m-1, n-1)
 
    # If last characters are not same, consider all 3
    return 1 + min(
                    editDistance(eng, kin, m, n-1),    # Insert
                    editDistance(eng, kin, m-1, n),    # Remove
                    editDistance(eng, kin, m-1, n-1)   # Replace
                   )
 
eng = "iran"
kin = "irani"
#print(editDistance(eng, kin, len(eng), len(kin)))



def AverageEditDistance():
    ED = 0
    count = 0
    for l in lines:
        l = l.strip ().split('|||')
        eng = l[0].strip()
        kin = l[1].strip()
        ED = ED + editDistance(eng, kin, len(eng), len(kin))
        count = count + 1
        print(ED)
        print(count)
    return (ED/count)
print(AverageEditDistance())


maxED = 0
minED = 0
def MaxMinEditDistance(maxED,minED):
    for l in lines:
        l = l.strip ().split('|||')
        eng = l[0].strip()
        kin = l[1].strip()
        ED = editDistance(eng, kin, len(eng), len(kin))
        if(ED > maxED):
            maxED=ED
        if(ED == minED):
            minED=ED
MaxMinEditDistance(maxED,minED)
#print(maxED,minED)


maxC = 0
minC = 0
def CountEditDistance(maxED,minED,maxC,minC):
    for l in lines:
        l = l.strip ().split('|||')
        print(l)
        eng = l[0].strip()
        kin = l[1].strip()
        ED = editDistance(eng, kin, len(eng), len(kin))
        if(ED == maxED):
            maxC = maxC + 1
        if(ED == minED):
            minC = minC + 1
#print(maxC,minC)
cED = 0
avgED = 0
        

    