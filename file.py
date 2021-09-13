import sys

def genCount(l):
    occurences = {}
    for i in l:
        if(i not in occurences):
            occurences[i] = 1
        else:
            occurences[i] += 1
    return occurences

