# 6-10
favorite_numbers = {
    'mary': [3, 52, 34],
    'john': [7, 15, 28],
    'matthew': [9, 11, 45],
    'william': [11, 73, 58],
    'judy': [15, 67, 94]
}

for key, value in favorite_numbers.items():
    msg = f"{key.title()}'s favorite numbers are: "
    for i in value:
        if i == value[-1]:
            msg += f"{str(i)}."
        else:
            msg += f"{str(i)}, "

    print(msg)
