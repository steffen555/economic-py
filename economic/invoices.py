import api_communicator

url = 'invoices/drafts'


class DraftInvoice:
    # If the values are none, they will be extracted from the customer.
    def __init__(self, customer, date, currency=None, layout=None, payment_terms=None, recipient=None):
        self.cost_price_in_base_currency = None
        self.delivery = None
        self.delivery_location = None
        self.due_date = None
        self.exchange_rate = None
        self.gross_amount = None
        self.gross_amount_in_base_currency = None
        self.lines = []
        self.margin_in_base_currency = None
        self.margin_percentage = None
        self.net_amount = None
        self.net_amount_in_base_currency = None
        self.notes = None
        self.project = None
        self.references = None
        self.rounding_amount = None
        self.soap = None
        self.templates = None
        self.vat_amount = None
        self.customer = customer
        self.date = date
        if currency:
            self.currency = currency
        else:
            self.currency = customer.currency

        if layout:
            self.layout = layout
        else:
            self.layout = customer.layout

        if payment_terms:
            self.payment_terms = payment_terms
        else:
            self.payment_terms = customer.payment_terms

        if recipient:
            self.recipient = recipient
        else:
            new_recipient = Recipient()
            new_recipient.address = customer.address
            new_recipient.attention = customer.attention
            new_recipient.city = customer.city
            new_recipient.country = customer.country
            new_recipient.ean = customer.ean
            new_recipient.mobile_phone = customer.mobile_phone
            new_recipient.name = customer.name
            new_recipient.public_entry_number = customer.public_entry_number
            new_recipient.vat_zone = customer.vat_zone
            new_recipient.zip = customer.zip
            self.recipient = new_recipient

    def post(self, auth):
        return api_communicator.post_object(auth, url, self)

    def to_dict(self):
        dict = {}

        if self.cost_price_in_base_currency:
            dict['costPriceInBaseCurrency'] = self.cost_price_in_base_currency
        if self.currency:
            dict['currency'] = self.currency
        if self.customer:
            dict['customer'] = self.customer.to_dict()
        if self.date:
            dict['date'] = self.date
        if self.delivery:
            dict['delivery'] = self.delivery.to_dict()
        if self.delivery_location:
            dict['deliveryLocation'] = self.delivery_location.to_dict()
        if self.due_date:
            dict['dueDate'] = self.due_date
        if self.exchange_rate:
            dict['exchangeRate'] = self.exchange_rate
        if self.gross_amount:
            dict['grossAmount'] = self.gross_amount
        if self.gross_amount_in_base_currency:
            dict['grossAmountInBaseCurrency'] = self.gross_amount_in_base_currency
        if self.layout:
            dict['layout'] = self.layout.to_dict()
        if self.lines:
            dict['lines'] = [line.to_dict() for line in self.lines]
        if self.margin_in_base_currency:
            dict['marginInBaseCurrency'] = self.margin_in_base_currency
        if self.margin_percentage:
            dict['marginPercentage'] = self.margin_percentage
        if self.net_amount:
            dict['netAmount'] = self.net_amount
        if self.notes:
            dict['notes'] = self.notes.to_dict()
        if self.payment_terms:
            dict['paymentTerms'] = self.payment_terms.to_dict()
        if self.project:
            dict['project'] = self.project.to_dict()
        if self.recipient:
            dict['recipient'] = self.recipient.to_dict()
        if self.references:
            dict['references'] = self.references.to_dict()
        if self.rounding_amount:
            dict['roundingAmount'] = self.rounding_amount
        if self.vat_amount:
            dict['vatAmount'] = self.vat_amount

        return dict


class Recipient:
    def __init__(self):
        self.address = None
        self.attention = None
        self.city = None
        self.country = None
        self.ean = None
        self.mobile_phone = None
        self.name = None
        self.nem_handel_type = None
        self.public_entry_number = None
        self.vat_zone = None
        self.zip = None

    def to_dict(self):
        dict = {}
        if self.address:
            dict['address'] = self.address
        if self.attention:
            dict['attention'] = self.attention.to_dict()
        if self.city:
            dict['city'] = self.city
        if self.country:
            dict['country'] = self.country
        if self.ean:
            dict['ean'] = self.ean
        if self.mobile_phone:
            dict['mobilePhone'] = self.mobile_phone
        if self.name:
            dict['name'] = self.name
        if self.nem_handel_type:
            dict['nemHandelType'] = self.nem_handel_type
        if self.public_entry_number:
            dict['publicEntryNumber'] = self.public_entry_number
        if self.vat_zone:
            dict['vatZone'] = self.vat_zone.to_dict()
        if self.zip:
            dict['zip'] = self.zip
        return dict


class Line:
    def __init__(self):
        self.accrual = None
        self.departmental_distribution = None
        self.description = None
        self.discount_percentage = None
        self.line_number = None
        self.margin_in_base_currency = None
        self.margin_percentage = None
        self.product = None
        self.quantity = None
        self.sort_key = None
        self.unit = None
        self.unit_cost_price = None
        self.unit_net_price = None

    def to_dict(self):
        dict = {}
        if self.accrual:
            dict['accrual'] = self.accrual.to_dict()
        if self.departmental_distribution:
            dict['departmentalDistribution'] = self.departmental_distribution.to_dict()
        if self.description:
            dict['description'] = self.description
        if self.discount_percentage:
            dict['discountPercentage'] = self.discount_percentage
        if self.line_number:
            dict['lineNumber'] = self.line_number
        if self.margin_in_base_currency:
            dict['marginInBaseCurrency'] = self.margin_in_base_currency
        if self.margin_percentage:
            dict['marginPercentage'] = self.margin_percentage
        if self.product:
            dict['product'] = self.product.to_dict()
        if self.quantity:
            dict['quantity'] = self.quantity
        if self.sort_key:
            dict['sortKey'] = self.sort_key
        if self.unit:
            dict['unit'] = self.unit.to_dict()
        if self.unit_cost_price:
            dict['unitCostPrice'] = self.unit_cost_price
        if self.unit_net_price:
            dict['unitNetPrice'] = self.unit_net_price
        return dict


def parse_json(json_obj):
    pass  # TODO


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, url, filters, sort_by)
