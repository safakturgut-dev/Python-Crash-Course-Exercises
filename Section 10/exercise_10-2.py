# 10-2
filename = 'glossory_python.txt'

with open(filename) as f:
    lines = f.readlines()

# replace colon with arrow
for line in lines:
    line = line.replace(': ', ' -> ')
    print(line.rstrip())
