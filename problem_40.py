'''Jason A Smith'''
fract = ''
count = 1
while len(fract) < 1000000:
    fract += str(count)
    count += 1

print(int(fract[1 - 1]) * int(fract[10 - 1]) * int(fract[100 - 1]) * int(fract[1000 - 1]) * int(fract[10000 - 1]) * int(fract[100000 - 1]) * int(fract[1000000 - 1]))
