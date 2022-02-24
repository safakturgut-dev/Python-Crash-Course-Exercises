# 3-10
countries = ['germany', 'france', 'egypt', 'turkey', 'united kingdom']

print(countries)
countries[0] = 'sweden'
print(countries)
countries.append('norway')
print(countries)
countries.insert(3, 'denmark')
print(countries)
del countries[5]
print(countries)
countries.pop()
print(countries)
countries.remove('egypt')
print(countries)
print(sorted(countries))
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
print(len(countries))
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
