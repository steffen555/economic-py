import api_communicator


class Employee:

    def __init__(self):
        self.barred = None
        self.email = None
        self.employee_group = None
        self.employee_number = None
        self.name = None
        self.phone = None


class EmployeeGroup:

    def __init__(self):
        self.employee_group_number = None
        pass


def parse_json(json_obj):
    employee = Employee()
    employee.barred = json_obj.get('barred')
    employee.email = json_obj.get('email')
    employee.employee_group = parse_json_employee_group(json_obj.get('employeeGroup'))
    employee.employee_number = json_obj.get('employeeNumber')
    employee.name = json_obj.get('name')
    employee.phone = json_obj.get('phone')
    return employee


def parse_json_employee_group(json_obj):
    employee_group = EmployeeGroup()
    employee_group.employee_group_number = json_obj.get('employeeGroupNumber')
    return employee_group


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'employees', filters, sort_by)
