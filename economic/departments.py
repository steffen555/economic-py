import api_communicator


class Department:

    def __init__(self, department_number):
        self.name = None
        self.department_number = department_number

    def to_dict(self):
        dict = {}
        if self.department_number:
            dict['departmentNumber'] = self.department_number
        if self.name:
            dict['name'] = self.name

        return dict


def parse_json(json_obj):
    department = Department(json_obj.get('departmentNumber'))
    department.name = json_obj.get('name')
    return department


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'departments', filters, sort_by)
