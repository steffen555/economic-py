class Authentication:
    def __init__(self, agreement_grant_token, app_secret_token):
        self.agreement_grant_token = agreement_grant_token
        self.app_secret_token = app_secret_token

    def get_request_headers(self):
        return {'X-AgreementGrantToken': self.agreement_grant_token,
                'X-AppSecretToken': self.app_secret_token}
