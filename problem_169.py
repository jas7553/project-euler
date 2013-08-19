from math import *

# 10
'1010'
'0210'
'0202'
'1002'
'0122'

# 11
'1011'
'0211'

# 12
'1100'
'1020'
'0220'
'1012'
'0212'

seen = []

def binaryCombinations(number):
    binstr = bin(number)[2:]
    if len(binstr) < 2:
        return 1
    else:
        return binaryCombinationsHelper(binstr)

def binaryCombinationsHelper(binstr):
    count = 1
    print(binstr)

    if ((binstr.rfind('10') != -1)):
        if (binstr in seen):
            count -= 1
        seen.append(binstr)
        count += binaryCombinationsHelper(binstr.replace('10', '02', 1))
        

    if ((binstr.rfind('20') != -1)):
        if (binstr in seen):
            count -= 1
        seen.append(binstr)
        count += binaryCombinationsHelper(binstr.replace('20', '12', 1))

    if ((binstr.rfind('100') != -1)):
        print('here')
        if (binstr in seen):
            count -= 1
        else:
            seen.append(binstr)
        count += binaryCombinationsHelper(binstr.replace('100', '012', 1))
        

    #print(seen)
    #return count
    return len(seen)

print(binaryCombinations(10))
#print(binaryCombinations(int(pow(10, 25))))

