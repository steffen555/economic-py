import api_communicator


class Department:
    department_number = None
    name = None

    def __init__(self, departmentNumber):
        self.department_number = departmentNumber


def parse_json(json_obj):
    department = Department(json_obj.get('departmentNumber'))
    department.name = json_obj.get('name')
    return department


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'departments', filters, sort_by)
