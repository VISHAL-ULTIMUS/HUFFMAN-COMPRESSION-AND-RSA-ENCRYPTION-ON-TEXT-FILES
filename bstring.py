from array import *
from Tree import *
from decrypt_tree import *

def genBinaryString(paths, filepath):
    string = ""
    with open(filepath,'r') as f:
        info = f.read()
        for i in info:
            string += paths[i]
    return string

def genByteArr(bstring):
    barray = array('B')
    index = 0
    length = len(bstring)
    bstring +=  (8 - (length % 8)) * '0'
    lengthbstring = len(bstring)
    while(index < lengthbstring):
        barray.append(int(bstring[index:index + 8],2))
        index += 8
    return barray, length

def binaryList(restOfInput):
    binlist = []    
    for i in restOfInput:
        binlist.append((ord(i)))
    return binlist

def binary(x):
    st = bin(x)[2:]
    st = st[::-1]
    st += (8 - len(st)) * '0'
    st = st[::-1]
    return st

def genBinString(blist, binstrlen):
    binstr = ""
    for i in blist:
        binstr += binary(i)
    binstr = binstr[:binstrlen]
    return binstr


def genFile(binstring, convdict):
    l = []
    genList(l, maxlength(convdict))
    fillList(l, convdict)
    output = ""
    j = l
    for i in binstring:
        j = j[int(i)]
        if(type(j[-1]) == str):
            output += j[-1]
            j = l
    return output
