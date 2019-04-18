import api_communicator
import customer_groups


class Customer:
    address = None
    attention = None
    balance = None
    barred = None
    city = None
    corporate_identification_number = None
    country = None
    credit_limit = None
    currency = None
    customer_contact = None
    customer_group = None
    customer_number = None
    default_delivery_location = None
    ean = None
    email = None
    last_updated = None
    layout = None
    mobile_phone = None
    name = None
    payment_terms = None
    p_number = None
    public_entry_number = None
    sales_person = None
    telephone_and_fax_number = None
    templates = None
    totals = None
    vat_number = None
    vat_zone = None
    website = None
    zip = None

    def __init__(self,
                 currency,
                 customer_group,
                 name,
                 payment_terms,
                 vat_zone):
        self.currency = currency
        self.customer_group = customer_group
        self.name = name
        self.payment_terms = payment_terms
        self.vat_zone = vat_zone


class Attention:
    customer_contact_number = None

    def __init__(self):
        pass


class CustomerContact:
    customer_contact_number = None

    def __init__(self):
        pass


class DeliveryLocation:
    delivery_location_number = None

    def __init__(self):
        pass


class Layout:
    layout_number = None

    def __init__(self):
        pass


class PaymentTerms:
    payment_terms_number = None

    def __init__(self):
        pass


def parse_json(json_obj):
    customer = Customer(json_obj.get('currency'),
                        customer_groups.parse_json(json_obj.get('customerGroup')),
                        json_obj.get('name'),
                        None,  # TODO: When payment terms are done
                        None)  # TODO: When VAT zones are done
    customer.address = json_obj.get('address')
    customer.attention = parse_json_attention(json_obj.get('attention'))
    customer.balance = json_obj.get('balance')
    customer.barred = json_obj.get('barred')
    customer.city = json_obj.get('city')
    customer.corporate_identification_number = json_obj.get('corporateIdentificationNumber')
    customer.country = json_obj.get('country')
    customer.credit_limit = json_obj.get('creditLimit')
    customer.customer_contact = parse_json_customer_contact(json_obj.get('customerContact'))
    customer.customer_number = json_obj.get('customerNumber')
    customer.default_delivery_location = parse_json_delivery_location(json_obj.get('default_delivery_location'))
    customer.ean = json_obj.get('ean')
    customer.email = json_obj.get('email')
    customer.last_updated = json_obj.get('lastUpdated')
    customer.layout = parse_json_layout(json_obj.get('layout'))
    customer.mobile_phone = json_obj.get('mobilePhone')
    customer.payment_terms = parse_json_payment_terms(json_obj.get('paymentTerms'))
    customer.p_number = json_obj.get('pNumber')
    customer.public_entry_number = json_obj.get('publicEntryNumber')
    customer.sales_person = None  # TODO: When employees are done
    customer.telephone_and_fax_number = json_obj.get('telephoneAndFaxNumber')
    customer.vat_number = json_obj.get('vatNumber')
    customer.vat_zone = None  # TODO: when VAT zones are done
    customer.website = json_obj.get('website')
    customer.zip = json_obj.get('zip')


def parse_json_attention(json_obj):
    attention = Attention()
    attention.customer_contact_number = json_obj.get('customerContactNumber')
    return attention


def parse_json_customer_contact(json_obj):
    customer_contact = CustomerContact()
    customer_contact.customer_contact_number = json_obj.get('customerContactNumber')
    return customer_contact


def parse_json_delivery_location(json_obj):
    delivery_location = DeliveryLocation()
    delivery_location.delivery_location_number = json_obj.get('deliveryLocationNumber')
    return delivery_location


def parse_json_layout(json_obj):
    layout = Layout()
    layout.layout_number = json_obj.get('layoutNumber')
    return layout


def parse_json_payment_terms(json_obj):
    payment_terms = PaymentTerms()
    payment_terms.payment_terms_number = json_obj.get('paymentTermsNumber')
    return payment_terms


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'customers', filters, sort_by)
