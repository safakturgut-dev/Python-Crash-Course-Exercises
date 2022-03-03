# 8-5
def describe_city(name, country='Germany'):
    print(f"{name.title()} is in {country.title()}.")


describe_city('berlin')
describe_city('hamburg')
describe_city('frankfurt')

describe_city('new york', 'US')
describe_city('chicago', 'US')
describe_city('los angeles', 'US')
