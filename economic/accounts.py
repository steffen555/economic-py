import api_communicator


class Account:
    account_number = None
    accounts_summed = []
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


class AccountSummed:
    from_account = None
    to_account = None

    def __init__(self):
        pass


def parse_json(json_obj):
    if not json_obj:
        return None
    account = Account(json_obj.get('accountNumber'))
    account.accounts_summed = parse_json_accounts_summed(json_obj.get('accountsSummed'))
    account.account_type = json_obj.get('accountType')
    account.balance = json_obj.get('balance')
    account.barred = json_obj.get('barred')
    account.block_direct_entries = json_obj.get('blockDirectEntries')
    account.contra_account = parse_json(json_obj.get('contraAccount'))
    account.debit_credit = json_obj.get('debitCredit')
    account.draft_balance = json_obj.get('draftBalance')
    account.name = json_obj.get('name')
    account.total_from_account = parse_json(json_obj.get('accountNumber'))
    account.vat_account = None  # TODO: When VAT accounts are done
    return account


def parse_json_accounts_summed(json_obj):
    if not json_obj:
        return None
    return [parse_json_account_summed(o) for o in json_obj]


def parse_json_account_summed(json_obj):
    account_summed = AccountSummed()
    account_summed.from_account = parse_json(json_obj.get('fromAccount'))
    account_summed.to_account = parse_json(json_obj.get('toAccount'))
    return account_summed


def get_all(auth,
            filters=None,
            sort_by=None):
    return api_communicator.get_all_objects(auth, parse_json, 'accounts', filters, sort_by)
