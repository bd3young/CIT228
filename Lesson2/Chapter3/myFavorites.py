print("--------------------------Hands on 1------------------------------")
print()
favFoods = ['pizza', 'spagetti', 'hamburger', 'peanutbutter chicken', 'sesame chicken', 'burito']
favNumbers = [6, 16, 26, 36, 46, 56, 66]
favMovies = ['Step Brothers', 'Transformers', 'Star Wars']
comboList = [favFoods[0], favFoods[2], favNumbers[0], favNumbers[2], favMovies[0], favMovies[2]]

print(f'Favorite Foods: {favFoods}')
print(f'Favorite Numbers: {favNumbers}')
print(f'Favorite Movies: {favMovies}')
print(f'Combo List: {comboList}')
print(f'Last Favorite Foods: {favFoods[5]}')
print(f'2nd, 4th and 6th numbers: {favNumbers[1], favNumbers[3], favNumbers[5]}')
print(f'All Movies: {favMovies}')
print(f'First Food, First Number and first Movie: {favFoods[0], favNumbers[0], favMovies[0]}')
print()
print("--------------------------Hands on 2------------------------------")
print()
favMovies.append('Pineapple Express')
print(f'Added movie: {favMovies}')
favNumbers.insert(3, 55)
print(f'Added Number at sub 3: {favNumbers}')
favFoods.insert(5, 'quesadilla')
print(f'Added food at sub 5: {favMovies}')
del favFoods[6]
print(f'Deleted food[6]: {favFoods}')
favNumbers.pop()
print(f'Deleted last number: {favNumbers}')
favNumbers.pop(2)
print(f'Deleted number at sub 2: {favNumbers}')
print()
print("--------------------------Hands on 3------------------------------")
print()
favMovies.sort()
print(f'Sorted List: {favMovies}')
favFoods.sort()
print(f'Sorted List: {favFoods}')
print(f'Temp Sorted List: {sorted(favNumbers)}')
print(f'Unsorted List: {favNumbers}')
favMovies.reverse()
print(f'Sorted in Reverse: {favMovies}')
print()