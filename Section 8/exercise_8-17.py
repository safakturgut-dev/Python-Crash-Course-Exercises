# 8-17
def make_sandwich(*ingredients):
    '''Make a sandwich with given ingredients.'''
    print("\nMaking sandwich with following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")
