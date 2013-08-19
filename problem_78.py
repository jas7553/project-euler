def findthefirstpnaboveamillion():
    num = 0
    current = 9
    while num < 1000000:
        current += 1
        num = dopn(current)
    print(current)

def dopn(num):
    count = 2
    banana = [num - 1, 1]
    while banana[0] != 1 or banana[1] != 1:
        if banana[1] == 2:
            banana[1] = 1
            count += 1
        elif banana[0] == 2:
            banana[0] = 1
            count += 1
        elif banana[0] > 1 and banana[1] == 1:
            banana[0] -= 1
            banana[1] = 2
            count += 1
    return count

print(dopn(500000))
#findthefirstpnaboveamillion()
