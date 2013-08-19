'''Jason A Smith'''
def nameScore(name):
    return sum([ord(char.lower()) - 96 for char in name])

names = open('names.txt').readline()[1:-1].split('","')
names.sort()

result = sum([nameScore(names[index]) * (index + 1) for index in range(len(names))])
print(result)
