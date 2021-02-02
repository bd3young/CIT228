import random

rounds = 0

keepPlaying = True
anotherRound = ''

while keepPlaying and anotherRound != 'q':
    problems = int(input('how many problems would you like to practice? '))
    incorectAns = 0
    counter = 0
    numberCorrect = 0 
    while counter < problems:
        randNumber1 = random.randrange(1,1000)
        randNumber2 = random.randrange(1,1000)
        correctAnswer = int(randNumber1 + randNumber2)
        yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}? "))
        if correctAnswer == yourAnswer:
            print('That it correct!!!')
            numberCorrect += 1
        else:
            print('That is incorect.')
            incorectAns += 1
        if incorectAns > 5:
            print('You need to find a tutor!!')
            keepPlaying = False
            break
        counter += 1
    if keepPlaying:          
            anotherRound = input('Would you like to play another round? if not type q.')
            break
    rounds += 1

print(f"You answered {numberCorrect} questions correctly!")
print('thanks for playing')