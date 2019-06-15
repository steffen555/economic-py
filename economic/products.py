import api_communicator
import departmental_distributions


class Product:
    def __init__(self):
        self.bar_code = None
        self.barred = None
        self.cost_price = None
        self.departmental_distribution = None
        self.description = None
        self.inventory = None
        self.last_updated = None
        self.name = None
        self.product_group = None
        self.product_number = None
        self.recommended_price = None
        self.sales_price = None
        self.unit = None

    def to_dict(self):
        dict = {}

        if self.bar_code:
            dict['barCode'] = self.bar_code
        if self.barred:
            dict['barred'] = self.barred
        if self.cost_price:
            dict['costPrice'] = self.cost_price
        if self.departmental_distribution:
            dict['departmentalDistribution'] = self.departmental_distribution.to_dict()
        if self.description:
            dict['description'] = self.description
        if self.inventory:
            dict['inventory'] = self.inventory
        if self.last_updated:
            dict['lastUpdated'] = self.last_updated
        if self.name:
            dict['name'] = self.name
        if self.product_group:
            dict['productGroup'] = self.product_group.to_dict()
        if self.product_number:
            dict['productNumber'] = self.product_number
        if self.recommended_price:
            dict['recommendedPrice'] = self.recommended_price
        if self.sales_price:
            dict['sales_price'] = self.sales_price
        if self.unit:
            dict['unit'] = self.unit.to_dict()

        return dict


def parse_json(json_obj):
    if not json_obj:
        return None
    product = Product()
    product.bar_code = json_obj.get('barCode')
    product.barred = json_obj.get('barred')
    product.cost_price = json_obj.get('costPrice')
    product.departmental_distribution = departmental_distributions.parse_json(json_obj.get('departmentalDistribution'))
    product.description = json_obj.get('description')
    product.inventory = json_obj.get('inventory')
    product.last_updated = json_obj.get('lastUpdated')
    product.name = json_obj.get('name')
    product.product_group = None  # TODO
    product.product_number = json_obj.get('productNumber')
    product.recommended_price = json_obj.get('recommendedPrice')
    product.sales_price = json_obj.get('salesPrice')
    product.unit = None  # TODO

    return product


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'products', filters, sort_by)


def get(auth,
        product_number):
    return api_communicator.get_single_object(auth, parse_json, 'products', product_number)
