rivers = {
    'Danube' : ['Germany', 'Austria', 'Slovakia', 'Hungary', 'Coratia', 'Serbia', 'Romania', 'Bulgaria', 'Moldova', 'Ukraine'],
    'Mississippi' : 'United States',
    'Amazon' : ['Brazil', 'Bolivia', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana']
}


for key, value in rivers.items():
    if type(value) == list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t",v)
    else:    
        print(f"The {key.title()} river flows through {value.title()}")