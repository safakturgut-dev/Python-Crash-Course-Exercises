# 8-13
def build_profile(fname, lname, **kwargs):
    kwargs['first_name'] = fname
    kwargs['last_name'] = lname
    return kwargs


person_1 = build_profile('safak', 'turgut', age=28,
                         weight=72, location='turkey')

print(person_1)
