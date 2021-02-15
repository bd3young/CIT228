print('Try it Yourself 10-2')

with open('learningPython.txt') as txtFile:
    myTxt = txtFile.read()
print('-------------------------Output from read()--------------------------')
print(myTxt)

print('-------------------------Output from for loop inside with...open--------------------------')
with open('learningPython.txt') as txtFile:
    for line in txtFile:
        print(line)

print('-------------------------Output from readlines()--------------------------')
with open('learningPython.txt') as txtFile:
    myTxt = txtFile.readlines()
print(f'Original List = {myTxt}')
for line in myTxt:
    print(line)

print()
print('Try it Yourself 10-2')
print('-------------------------Output from readlines()--------------------------')
with open('learningPython.txt') as txtFile:
    for line in txtFile:
        print(f'Original: {line}')
        print(f'Modified: {line.replace("zz", "t")}')