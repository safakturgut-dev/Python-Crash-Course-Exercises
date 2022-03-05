# 10-10
filename = 'moby_dick.txt'

with open(filename, encoding='utf-8') as f:
    content = f.read()

print(content.count('the'))
print(content.count('the '))

print(content.lower().count('the'))
print(content.lower().count('the '))

print(content.count('ship '))
print(content.lower().count('ship '))
