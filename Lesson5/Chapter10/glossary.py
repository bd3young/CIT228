import json

def menu():
    selection = int(input('(1 - Create File )( 2 - Read File )( 3 - Add to File )(4 - Quit ) '))
    while selection != 1 and selection != 2 and selection !=  3 and selection != 4:
        print('Please enter a valid selection.')
        selection = int(input('(1 - Create File )( 2 - Read File )( 3 - Add to File )(4 - Quit ) '))
    return selection

def create(glossary):
    overwrite = input('You are creating a new file, your current file will be overwritten ( ender q to quit , or any key to continue) ')
    if overwrite != 'q':
        with open('Lesson5\Chapter10\glossaryBook.json', 'w') as writeFile:
            json.dump(glossary, writeFile, indent=4, sort_keys=True)
            print('glossaryBook.json has been created')

def append(newEntry):
    with open('Lesson5\Chapter10\glossaryBook.json', 'r+') as addFile:
        animalDict = json.load(addFile)
        animalDict.update(newEntry)
        addFile.seek(0)
        json.dump(animalDict, addFile, indent=4, sort_keys=True)
        print('Data has been added to glossaryBook.json')

def read():
    try:
        with open('Lesson5\Chapter10\glossaryBook.json') as readFile:
            animalDict = json.load(readFile)
    except FileNotFoundError:
        print('File does not exist.')
        print('Pleas make a different selection in the menu')
    else:
        print('   Anmial  |   Description')
        print('----------------------------')
        for key, value in animalDict.items():
            print(f'{key.title()} - {value}') 

def getAnimal():
    animal = input('Enter an animal ')
    return animal

def getDescription():
    description = input('Decribe the Animal ')
    return description

glossary = {
    'cat' : 'Is a furry animal that has a long tail and sharp claws. Cats are often kept as pets',
    'dog' : 'Are domesticated mammals, not natural wild animals. They were originally bred from wolves.',
    'frog' : 'Are amphibians that are known for their jumping abilities, croaking sounds, bulging eyes and slimy skin',
    'whale' : 'Are large, intelligent, aquatic mammals. They breathe air through blowhole(s) into lungs.',
    'elephant' : 'Largest living land animal, characterized by its long trunk, columnar legs, and huge head with temporal glands and wide, flat ears.'
}

menuSelection = menu()
while menuSelection != 4:
    if menuSelection == 1:
        create(glossary)
    elif menuSelection == 2:
        read()
    else:
        animal = getAnimal()
        description = getDescription()
        tempDict = {animal : description}
        append(tempDict)
    menuSelection = menu()