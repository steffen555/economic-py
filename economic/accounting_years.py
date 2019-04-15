import requests
import json
import exceptions


class AccountingYear:
    fromDate = None
    toDate = None
    closed = None
    year = None
    __periods = None
    __entries = None
    __totals = None
    __vouchers = None

    def __init__(self, from_date, to_date, closed, year):
        self.fromDate = from_date
        self.toDate = to_date
        self.closed = closed
        self.year = year


def parse_json(json_obj):
    return AccountingYear(from_date=json_obj.get('fromDate'),
                          to_date=json_obj.get('toDate'),
                          closed=json_obj.get('closed'),
                          year=json_obj.get('year'))


def get_accounting_years(filters=None,
                         sort_by=None):
    r = requests.get('https://restapi.e-conomic.com/accounting-years',
                     headers={'X-AgreementGrantToken': 'demo',
                              'X-AppSecretToken': 'demo'},
                     data='',
                     params={'filters': filters, 'sort': sort_by})
    exceptions.is_ok_or_throw_exception(r)

    j = json.loads(r.text)
    json_list = j['collection']
    obj_list = [parse_json(o) for o in json_list]
    return r.text
