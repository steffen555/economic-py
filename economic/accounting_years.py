import api_communicator


class AccountingYear:
    def __init__(self, from_date, to_date, closed, year):
        self.fromDate = from_date
        self.toDate = to_date
        self.closed = closed
        self.year = year

    def get_entries(self):
        raise NotImplementedError

    def get_periods(self):
        raise NotImplementedError

    def get_totals(self):
        raise NotImplementedError

    def get_vouchers(self):
        raise NotImplementedError


def parse_json(json_obj):
    return AccountingYear(from_date=json_obj.get('fromDate'),
                          to_date=json_obj.get('toDate'),
                          closed=json_obj.get('closed'),
                          year=json_obj.get('year'))


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'accounting-years', filters, sort_by)
