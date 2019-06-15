import api_communicator
import departments


class DepartmentalDistribution:

    def __init__(self):
        self.departmental_distribution_number = None
        self.distributions = []
        self.distribution_type = None
        self.name = None

    def to_dict(self):
        dict = {}
        if self.departmental_distribution_number:
            dict['departmentalDistributionNumber'] = self.departmental_distribution_number
        if self.distributions:
            dict['distributions'] = [distribution.to_dict() for distribution in self.distributions]
        if self.distribution_type:
            dict['distributionType'] = self.distribution_type
        if self.name:
            dict['name'] = self.name
        return dict


class Distribution:

    def __init__(self):
        self.department = None
        self.percentage = None

    def to_dict(self):
        dict = {}

        if self.department:
            dict['department'] = self.department.to_dict()
        if self.percentage:
            dict['percentage'] = self.percentage

        return dict


def parse_json_distribution(json_obj):
    if not json_obj:
        return None
    distribution = Distribution
    distribution.department = departments.parse_json(json_obj.get('department'))
    distribution.percentage = json_obj.get('percentage')


def parse_json_distributions(json_obj):
    if not json_obj:
        return None
    return [parse_json_distribution(o) for o in json_obj]


def parse_json(json_obj):
    if not json_obj:
        return None
    departmental_distribution = DepartmentalDistribution()
    departmental_distribution.departmental_distribution_number = json_obj.get('departmentalDistributionNumber')
    departmental_distribution.distributions = parse_json_distributions(json_obj.get('distributions'))
    return departmental_distribution


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth,
                                            parse_json,
                                            'departmental-distributions',
                                            filters,
                                            sort_by)


def get(auth,
        departmental_distribution_number):
    return api_communicator.get_single_object(auth,
                                              parse_json,
                                              'departmental-distributions',
                                              departmental_distribution_number)
