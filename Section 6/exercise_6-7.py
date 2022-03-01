# 6-7
people = [
    {
        'fname': 'sarah',
        'lname': 'watson',
        'city': 'paris'
    },

    {
        'fname': 'michael',
        'lname': 'jackson',
        'city': 'new york'
    },

    {
        'fname': 'patricia',
        'lname': 'atherton',
        'city': 'london'
    }
]

for person in people:
    print(
        f"{person['fname'].title()} {person['lname'].title()} lives in {person['city'].title()}.")
