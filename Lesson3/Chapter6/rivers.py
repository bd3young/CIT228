rivers = {
    'Danube' : ['Germany', 'Austria', 'Slovakia', 'Hungary', 'Coratia', 'Serbia', 'Romania', 'Bulgaria', 'Moldova', 'Ukraine'],
    'Mississippi' : 'United States',
    'Amazon' : ['Brazil', 'Bolivia', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana']
}

print('------------------Rivers & Countries-------------------------------')
for river in rivers:   
    print(f"the {river} river flows through : {rivers[river]}")

print('------------------Rivers-------------------------------')
for river in rivers:   
    print(river)

print('------------------Countries-------------------------------')
for river in rivers:
    print(rivers[river])