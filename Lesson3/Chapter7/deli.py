sandwichOrders = ['Vegan', 'Italian', 'Steak', 'Pastrami', 'Greek', 'Italian', 'Pastrami', 'Tuna', 'Steak', 'Pastrami']
finishedSandwichs = []
print('I am sorry, we are out of Pastrami')
while sandwichOrders.__contains__('Pastrami'):
    sandwichOrders.remove('Pastrami')
while sandwichOrders:
    currentSandwich = sandwichOrders.pop()
    print(f'I made your {currentSandwich} sandwich')
    finishedSandwichs.append(currentSandwich)

print('sandwichs that were made today include:')
for sandwich in finishedSandwichs:
    print(sandwich)
