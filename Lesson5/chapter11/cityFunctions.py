def CityCountry(city, country, population = ''):
    if population:
        cityCountry = city + ', ' + country + ' - ' + population
    else:
        cityCountry = city + ', ' + country
    return cityCountry