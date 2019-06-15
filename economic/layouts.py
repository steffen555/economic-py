class Layout:
    def __init__(self):
        self.deleted = None
        self.layout_number = None
        self.name = None

    def to_dict(self):
        dict = {}
        if self.deleted:
            dict['deleted'] = self.deleted
        if self.layout_number:
            dict['layoutNumber'] = self.layout_number
        if self.name:
            dict['name'] = self.name
        return dict


def parse_json(json_obj):
    if not json_obj:
        return None
    layout = Layout()
    layout.deleted = json_obj.get('deleted')
    layout.layout_number = json_obj.get('layoutNumber')
    layout.name = json_obj.get('name')
    return layout
