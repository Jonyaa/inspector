from .inspection import make_inspection
print('inspections/names.py')


@make_inspection
def hasNameInspection(data):
    if 'name' in data['metadata']:
        return True
    else:
        return False
