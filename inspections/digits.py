from .inspection import make_inspection
print('inspections/digits.py')


@make_inspection
def isDigitInspection(data):
    if data['id'].isdigit():
        return True
    else:
        return False
