import json

def menu():
    selection = int(input('(1 - Create File )( 2 - Read File )'))

glossary = {
    'integer' : 'a whole number; a number that is not a fraction.',
    'string' : 'a series of characters.',
    'float' : 'any number with a decimal point.',
    'list' : 'collection of items in a particular order.',
    'bool' : 'true or false variable.'
}