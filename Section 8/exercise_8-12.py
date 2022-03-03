# 8-12
def make_sandwich(*ingredients):
    print("\nMaking sandwich with following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")


make_sandwich('cheese', 'ham', 'tuna')
make_sandwich('bacon', 'tomato')
make_sandwich('egg', 'turkey', 'cheese', 'lettuce')
