class VatZone:
    def __init__(self):
        self.enabled_for_customer = None
        self.enabled_for_supplier = None
        self.name = None
        self.vat_zone_number = None

    def to_dict(self):
        dict = {}
        if self.enabled_for_customer:
            dict['enabledForCustomer'] = self.enabled_for_customer
        if self.enabled_for_supplier:
            dict['enabledForSupplier'] = self.enabled_for_supplier
        if self.name:
            dict['name'] = self.name
        if self.vat_zone_number:
            dict['vatZoneNumber'] = self.vat_zone_number
        return dict


def parse_json(json_obj):
    if not json_obj:
        return None
    vat_zone = VatZone()
    vat_zone.enabled_for_customer = json_obj.get('enabledForCustomer')
    vat_zone.enabled_for_supplier = json_obj.get('enabledForSupplier')
    vat_zone.name = json_obj.get('name')
    vat_zone.vat_zone_number = json_obj.get('vatZoneNumber')
    return vat_zone
