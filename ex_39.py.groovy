sates = {
    'Tamilnadu' : 'TN'
    'california' : 'CN'
    'kerala' : 'kl'
    'New York' : 'NY'
}

cities = {
    'namakkal' : ' NKL'
    'salem' : 'SLM'
    'san fransisco' : 'SN'
}

cities['TN']
cities['NY']

print('-'*10)

print("NY state has :",cites['NY'])
print("TN state has :", cities['TN'])

print('-' *10)
print("New york abeviation is :", states [new york])
print("kerala abreviation is : ", states[kerala])

print('-' *10)
print("Tamilnadu has:", cities[states[states['tamilnadu']]])
print("kerala has :" , cities[states['kerala']])

print('-'*10)
for state , abrev in list(states.items()):
print(f"{state} state is abbreviated {abbbrev}")
print(f"and had city {cities[abbrev]}")

print('-'*10)
state = stetes.get('texas.')

if not state:
    print("sorry, no texas.")

ciy = cities.get('tx' , 'does not exist')
print(f"the city for the state 'tx' is : {city}")
