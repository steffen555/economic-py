import api_communicator
import customer_groups
import vat_zones
import layouts


class Customer:
    def __init__(self,
                 currency,
                 customer_group,
                 name,
                 payment_terms,
                 vat_zone):

        self.address = None
        self.attention = None
        self.balance = None
        self.barred = None
        self.city = None
        self.corporate_identification_number = None
        self.country = None
        self.credit_limit = None
        self.customer_contact = None
        self.customer_number = None
        self.default_delivery_location = None
        self.ean = None
        self.email = None
        self.last_updated = None
        self.layout = None
        self.mobile_phone = None
        self.p_number = None
        self.public_entry_number = None
        self.sales_person = None
        self.telephone_and_fax_number = None
        self.templates = None
        self.totals = None
        self.vat_number = None
        self.website = None
        self.zip = None
        self.currency = currency
        self.customer_group = customer_group
        self.name = name
        self.payment_terms = payment_terms
        self.vat_zone = vat_zone

    def to_dict(self):
        dict = {}
        if self.address:
            dict['address'] = self.address
        if self.attention:
            dict['attention'] = self.attention.to_dict()
        if self.balance:
            dict['balance'] = self.balance
        if self.barred:
            dict['barred'] = self.barred
        if self.city:
            dict['city'] = self.city
        if self.corporate_identification_number:
            dict['corporateIdentificationNumber'] = self.corporate_identification_number
        if self.country:
            dict['country'] = self.country
        if self.customer_group:
            dict['customerGroup'] = self.customer_group.to_dict()
        if self.customer_number:
            dict['customerNumber'] = self.customer_number
        if self.ean:
            dict['ean'] = self.ean
        if self.email:
            dict['email'] = self.email
        if self.layout:
            dict['layout'] = self.layout.to_dict()
        if self.mobile_phone:
            dict['mobilePhone'] = self.mobile_phone
        if self.name:
            dict['name'] = self.name
        if self.payment_terms:
            dict['paymentTerms'] = self.payment_terms.to_dict()
        if self.p_number:
            dict['pNumber'] = self.p_number
        if self.public_entry_number:
            dict['publicEntryNumber'] = self.public_entry_number
        if self.sales_person:
            dict['salesPerson'] = self.sales_person.to_dict()
        if self.telephone_and_fax_number:
            dict['telephoneAndFaxNumber'] = self.telephone_and_fax_number
        if self.vat_number:
            dict['vatNumber'] = self.vat_number
        if self.vat_zone:
            dict['vatZone'] = self.vat_zone.to_dict()
        if self.website:
            dict['website'] = self.website
        if self.zip:
            dict['zip'] = self.zip
        return dict


class Attention:

    def __init__(self):
        self.customer_contact_number = None

    def to_dict(self):
        pass


class CustomerContact:

    def __init__(self):
        self.customer_contact_number = None


class DeliveryLocation:

    def __init__(self):
        self.delivery_location_number = None


class PaymentTerms:

    def __init__(self):
        self.payment_terms_number = None

    def to_dict(self):
        dict = {}
        if self.payment_terms_number:
            dict['paymentTermsNumber'] = self.payment_terms_number
        return dict


def parse_json(json_obj):
    if not json_obj:
        return None
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
    customer.layout = layouts.parse_json(json_obj.get('layout'))
    customer.mobile_phone = json_obj.get('mobilePhone')
    customer.payment_terms = parse_json_payment_terms(json_obj.get('paymentTerms'))
    customer.p_number = json_obj.get('pNumber')
    customer.public_entry_number = json_obj.get('publicEntryNumber')
    customer.sales_person = None  # TODO: When employees are done
    customer.telephone_and_fax_number = json_obj.get('telephoneAndFaxNumber')
    customer.vat_number = json_obj.get('vatNumber')
    customer.vat_zone = vat_zones.parse_json(json_obj.get('vatZone'))
    customer.website = json_obj.get('website')
    customer.zip = json_obj.get('zip')
    return customer


def parse_json_attention(json_obj):
    if not json_obj:
        return None
    attention = Attention()
    attention.customer_contact_number = json_obj.get('customerContactNumber')
    return attention


def parse_json_customer_contact(json_obj):
    if not json_obj:
        return None
    customer_contact = CustomerContact()
    customer_contact.customer_contact_number = json_obj.get('customerContactNumber')
    return customer_contact


def parse_json_delivery_location(json_obj):
    if not json_obj:
        return None
    delivery_location = DeliveryLocation()
    delivery_location.delivery_location_number = json_obj.get('deliveryLocationNumber')
    return delivery_location


def parse_json_payment_terms(json_obj):
    if not json_obj:
        return None
    payment_terms = PaymentTerms()
    payment_terms.payment_terms_number = json_obj.get('paymentTermsNumber')
    return payment_terms


def get(auth, customer_number):
    return api_communicator.get_single_object(auth, parse_json, 'customers', customer_number)


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'customers', filters, sort_by)


def get(auth,
        customer_number):
    return api_communicator.get_single_object(auth, parse_json, 'customers', customer_number)
