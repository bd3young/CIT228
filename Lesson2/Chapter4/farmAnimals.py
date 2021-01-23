animals= ['pig', 'chicken', 'goat', 'llama', 'alpaca', 'cow']

newAnimals = animals[:]
newAnimals.append('dog')
newAnimals.append('cat')
newAnimals.append('horse')
newAnimals.append('sheep')

print('---------------------Original List-------------------------')
for animal in animals:
    print(animal)
print('---------------------New List-------------------------')
for animal in newAnimals:
    print(animal)
print(f'The first 3 animals in the new list are: {newAnimals[0:3]}')
print(f'The middle 3 animals in the new list are: {newAnimals[3:6]}')
print(f'The last 3 animals in the new list are: {newAnimals[7:10]}')