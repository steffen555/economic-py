import requests
from exceptions import is_ok_or_throw_exception
import json


def get_all_objects(auth, parse_fun, url,
                    filters=None,
                    sort_by=None,
                    page=0):
    r = requests.get('https://restapi.e-conomic.com/%s' % url,
                     headers=auth.get_request_headers(),
                     data='',
                     params={'filters': filters,
                             'sort': sort_by,
                             'skippages': page,
                             'pageSize': 100})
    is_ok_or_throw_exception(r)

    j = json.loads(r.text)
    json_list = j.get('collection')
    obj_list = [parse_fun(o) for o in json_list]
    if j.get('pagination').get('nextPage'):
        obj_list.extend(get_all_objects(auth, parse_fun, url, filters=filters, sort_by=sort_by, page=page + 1))
    return obj_list
