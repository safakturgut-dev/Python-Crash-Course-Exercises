# 6-4
glossary = {
    'list': 'A list in Python is an ordered, mutable collection of objects.',
    'literals': 'Literals are data items that have a fixed value.',
    'loop': 'A loop is used for iterating over a sequence (like list, tuple, string, dictionary, set).',
    'slicing': 'It refers to accessing a particular part of a sequence, like lists, tuples, and strings.',
    'string': 'A string is a sequence of characters.',
    'set': 'A set is an unordered collection of data that allows only unique values.',
    'tuple': 'A tuple is an ordered, immutable collection of data.',
    'variable': 'A variable in Python is a named memory location that stores a value.',
    'zen of python': 'The philosophy which Python believes.'
}

for key, value in glossary.items():
    print(f"{key.title()}: \n\t{value}\n")
