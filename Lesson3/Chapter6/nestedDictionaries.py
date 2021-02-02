videoGames = {
    'Destiny 2' : {
        'Genre' : 'Shooter',
        'Price' : 'Free to Play',
        'Console' : 'PC'
    },
    'Monster Hunter World' : {
        'Genre' : 'RPG',
        'Price' : '59.99',
        'Console' : 'PC'
    },
    'Mario Odyssey' : {
        'Genre' : 'Platformer',
        'Price' : '59.99',
        'Console' : 'Nintendo Switch'
    }
}

for game, info in videoGames.items():
    print(f"\nGame: {game}")

    print(f"\tGenre : {info['Genre']}")
    print(f"\tPrice : {info['Price']}")
    print(f"\tConsole: {info['Console']}")