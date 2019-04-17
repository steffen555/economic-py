import pagination


class CustomerGroup:
    customer_group_number = None
    name = None
    __account = None
    __layout = None

    def __init__(self, customer_group_number):
        self.customer_group_number = customer_group_number

    def get_account(self):
        pass

    def get_layout(self):
        pass


def parse_json(json_obj):
    customer_group = CustomerGroup(json_obj.get('customerGroupNumber'))
    customer_group.name = json_obj.get('name')
    return customer_group


def get_all(auth,
            filters=None,
            sort_by=None):
    return pagination.get_all_objects(auth, parse_json, 'customer-groups', filters, sort_by)
