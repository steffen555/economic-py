import api_communicator
import accounts


class CustomerGroup:
    customer_group_number = None
    name = None
    account = None
    layout = None

    def __init__(self, customer_group_number):
        self.customer_group_number = customer_group_number

    def get_customers(self):
        raise NotImplementedError


def parse_json(json_obj):
    customer_group = CustomerGroup(json_obj.get('customerGroupNumber'))
    customer_group.name = json_obj.get('name')
    customer_group.account = accounts.parse_json(json_obj.get('account'))
    customer_group.layout = None  # TODO: when layouts are done.
    return customer_group


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'customer-groups', filters, sort_by)
