import pagination


class Account:
    account_number = None
    account_type = None
    balance = None
    barred = None
    block_direct_entries = None
    contra_account = None
    debit_credit = None
    draft_balance = None
    name = None
    total_from_account = None
    vat_account = None

    def __init__(self,
                 account_number):
        self.account_number = account_number

    def get_accounting_years(self):
        raise NotImplementedError


def parse_json(json_obj):
    account = Account(json_obj.get('accountNumber'))
    account.account_type = json_obj.get('accountType')
    account.balance = json_obj.get('balance')
    account.barred = json_obj.get('barred')
    account.block_direct_entries = json_obj.get('blockDirectEntries')
    contra_account = json_obj.get('contraAccount')
    if contra_account:
        account.contra_account = contra_account.get('accountNumber')
    account.debit_credit = json_obj.get('debitCredit')
    account.draft_balance = json_obj.get('draftBalance')
    account.name = json_obj.get('name')
    total_from_account = json_obj.get('totalFromAccount')
    if total_from_account:
        account.total_from_account = total_from_account.get('accountNumber')
    vat_account = json_obj.get('vatAccount')
    if vat_account:
        account.vat_account = vat_account.get('vatCode')
    return account


def get_all(auth,
            filters=None,
            sort_by=None):
    return pagination.get_all_objects(auth, parse_json, 'accounts', filters, sort_by)
