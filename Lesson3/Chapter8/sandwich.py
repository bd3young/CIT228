def makeSandwich(*items):
    print('Makeing your sub with the following items. ')
    for item in items:
        print(f'- {item}')
    
makeSandwich('bread', 'cheese', 'turkey', 'ham', 'salami')
makeSandwich('bread', 'cheese', 'turkey')
makeSandwich('bread', 'cheese', 'turkey', 'ham', 'salami', 'lettuce', 'tomato')