'''Jason A Smith'''
def alphabetPosition(letter):
    letter = letter.upper()
    return ord(letter) - 64

def getAllTriangleNumbersUnder(number):
    ret = []
    for i in range(1, number + 1):
        ret.append(int(0.5 * i * (i + 1)))
    return ret

words = open('problem_42_words.txt').readline()
words = words.replace('"','')
words = words.split(',')

count = 0
triangleNumbers = getAllTriangleNumbersUnder(364)

for word in words:
    if sum([alphabetPosition(letter) for letter in word]) in triangleNumbers:
        count += 1

print(count)
