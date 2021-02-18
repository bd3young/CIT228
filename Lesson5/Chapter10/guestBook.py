import os
from datetime import datetime

guest = ''

print('Try it Yourself 10-3 and 10-4')

with open('Lesson5\Chapter10\guest.txt', 'w') as guestBook:
    guest = input('What is your Name? ( enter q to quit ) ')
    while(guest != 'q'):
        time = "{:%B %d, %Y}".format(datetime.now())
        print(f'Hello {guest}, you have registered at {time}')
        guestBook.write(f'{guest} has been registered at {time} \n')
        guest = input('What is your Name? ( enter q to quit ) ')

with open('Lesson5\Chapter10\guest.txt') as guestBook:
    print('--------------- Registered Names and Times -------------------')
    for line in guestBook:
        print(line)

        
