print("--------------------------Chapter 4, Hands on 1------------------------------")
print()
favFoods = ['pizza', 'spagetti', 'hamburger', 'peanutbutter chicken', 'sesame chicken', 'burito']
favNumbers = [6, 16, 26, 36, 46, 56, 66]
favMovies = ['Step Brothers', 'Transformers', 'Star Wars']
comboList = [favFoods[0], favFoods[2], favNumbers[0], favNumbers[2], favMovies[0], favMovies[2]]

print('Food List')
print('-------------------------------------------------')
for food in favFoods:
    print(food)
print()
print('number List')
print('-------------------------------------------------')
for num in favNumbers:
    print(num)
print()
print('Movie List')
print('-------------------------------------------------')
for movie in favMovies:
    print(movie)
print()
print('Combo List')
print('-------------------------------------------------')
for item in comboList:
    print(item)