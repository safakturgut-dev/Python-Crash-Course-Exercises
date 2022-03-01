# 6-5
rivers = {
    'nile': 'egypt',
    'mississipi': 'united states',
    'yangtze': 'china',
    'yenisey': 'russia',
    'mackenzie': 'canada'
}

for key, value in rivers.items():
    print(f"{key.title()} runs through {value.title()}.")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)
