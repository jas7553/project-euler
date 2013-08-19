'''Jason A Smith, Jeremy Shulman'''
#from itertools import product
#allcomb = [''.join(i) for i in list(product('ola', repeat=30))]
#somecomb = [i for i in allcomb if ((i.find('l') == i.rfind('l')) and (not 'aaa' in i))]
#print(len(allcomb))

# 0 = L, 1 = A, 2 = O

def numberInBaseThree(num):
    ret = ''
    current = num
    while current != 0:
        remainder = current % 3
        current = current // 3
        ret = str(remainder) + ret
    return ret.zfill(30)

def ternaryGenerator():
    count = 0
    while count < 3 ** 30:
        strNum = numberInBaseThree(count)
        if isValid(strNum):
            yield strNum
        count += 1

def isValid(strNumber):
    if (not '111' in strNumber) and (strNumber.find('0') == strNumber.rfind('0')):
        return True
    else:
        return False

count = 0
t = ternaryGenerator()
while 1:
    try:
        next(t)
        count += 1
    except StopIteration:
        break

print(count)
