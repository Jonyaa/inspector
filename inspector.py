from inspections.inspection import InspectionList


class Inspector:
    def __init__(self, data):
        self.inspections = InspectionList.inspections
        self.data = data
        self.inspections_results = {}

    def inspect(self):
        for project in self.data:
            self.inspections_results[project['metadata']['name']] = {
                inspection.name: inspection.check(project) for inspection in self.inspections}
        print(self.inspections_results)
