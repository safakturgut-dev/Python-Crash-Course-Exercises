# 6-11
cities = {
    'istanbul': {
        'country': 'turkey',
        'population': 15_636_000,
        'is_capital': False
    },

    'london': {
        'country': 'england',
        'population': 9_540_000,
        'is_capital': True
    },

    'new york city': {
        'country': 'united states',
        'population': 19_223_000,
        'is_capital': False
    }
}

for key, value in cities.items():
    print(key.title() + ': ')
    print(f"\tIt is in {value['country'].title()}.")
    print(
        f"\tIt's approximate population is {str(value['population']).title()}.")
    if value['is_capital']:
        print(f"\tIt's the capital city.")
    else:
        print(f"\tIt's NOT the capital city.")
