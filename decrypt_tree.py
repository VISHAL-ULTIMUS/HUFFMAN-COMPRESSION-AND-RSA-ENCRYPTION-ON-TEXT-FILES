def maxlength(convdict):
    maxi = -1
    for i in convdict:
        if(len(convdict[i]) > maxi):
            maxi = len(convdict[i])
    return maxi

def genList(l,maxlength):
    if(maxlength == 0):
        return
    else:
        l.append([])
        l.append([])
        genList(l[0], maxlength - 1)
        genList(l[1], maxlength - 1)

def fillList(l, convdict):
    for key,values in convdict.items():
        j = l
        while(len(values) > 0):
            j = j[int(values[0])]
            if(len(values) == 1):
                break
            values = values[1:]
        j.append(key)
