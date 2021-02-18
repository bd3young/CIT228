while True:

    try:
        numberOne = int(input('enter your first number. '))
        numberTwo = int(input('enter your second number. '))
    except:
        print('Please enter a whole number.')
    else:
        print(f'{numberOne} + {numberTwo} = {numberOne + numberTwo}')


