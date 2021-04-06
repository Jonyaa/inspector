from inspector import Inspector
# from inspections.inspections import isDigitInspection

inspector = Inspector([{'id': 'asdf1234', 'metadata': {'name': 'project1'}},{'id': '2345', 'metadata': {'name': 'project2'}}])
# inspector.register_inspection(isDigitInspection)
inspector.inspect()