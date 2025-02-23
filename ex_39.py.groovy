states = {
    'Tamilnadu' : 'TN',
    'kerala' : 'KL',
    'California' : 'CA',
    'New York' : 'NY',
    'Goa' : 'GA'
}

cities = {
    'CA' : 'San Francisco',
    'GA' : 'Detroit',
    'KL' : 'kochi'
}

cities['NY'] = 'New York'
cities['TN'] = 'Tamilnadu'


print('-' * 10)
print("NY state has: ", cities['NY'])
print("TN state has: ", cities['TN'])


print('-' * 10)
print("Goa has: ", cities[states['Goa']])
print("kerala has: ", cities[states['kerala']])


print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")


print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")


print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev} and has city {cities[abbrev]}")


print('-' * 10)
state = states.get('Texas', None)

if not state:
    print('Sorry, no Texas.')

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
