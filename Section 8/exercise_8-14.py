# 8-14
def make_car(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs


car = make_car('ford', 'ranger', color='red', price=25500)

for key, value in car.items():
    print(f"{key.title()}: {value}")
