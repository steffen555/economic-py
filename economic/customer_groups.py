import api_communicator
import accounts
import layouts


class CustomerGroup:

    def __init__(self, customer_group_number):
        self.name = None
        self.account = None
        self.layout = None
        self.customer_group_number = customer_group_number

    def to_dict(self):
        dict = {}
        if self.customer_group_number:
            dict['customerGroupNumber'] = self.customer_group_number
        if self.name:
            dict['name'] = self.name
        if self.account:
            dict['account'] = self.account.to_dict()
        if self.layout:
            dict['layout'] = self.layout.to_dict()
        return dict


def parse_json(json_obj):
    customer_group = CustomerGroup(json_obj.get('customerGroupNumber'))
    customer_group.name = json_obj.get('name')
    customer_group.account = accounts.parse_json(json_obj.get('account'))
    customer_group.layout = layouts.parse_json(json_obj.get('layout'))
    return customer_group


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'customer-groups', filters, sort_by)


def get(auth,
        customer_group_number):
    return api_communicator.get_single_object(auth, parse_json, 'customer-groups', customer_group_number)
