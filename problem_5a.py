''' Jason A Smith'''
number = 20
while True:
    for i in range(20, 10, -1):
        if not number % i == 0:
            break
    else:
        print('found it: ' + str(number))
        break
    number += 20
