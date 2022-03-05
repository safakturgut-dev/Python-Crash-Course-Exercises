# 10-1
# I used 'glossory_python' file.

filename = 'glossory_python.txt'

# with open(filename) as f:
#     contents = f.read().rstrip()

# print(contents)

# with open(filename) as f:
#     for line in f:
#         print(line.rstrip())

with open(filename) as f:
    lines = f.readlines()

print(lines)

for line in lines:
    print(line.rstrip())
