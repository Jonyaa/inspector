print('inspections/inspection.py')


class Inspection:
    def __init__(self, name, checkfunc):
        self.name = name
        self.checkfunc = checkfunc

    def check(self, data):
        return self.checkfunc(data)


class InspectionList:
    inspections = []

    def __init__(self):
        pass


def make_inspection(func):
    new_inspection = Inspection(func.__name__, func)
    InspectionList.inspections.append(new_inspection)
