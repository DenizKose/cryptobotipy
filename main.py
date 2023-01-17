import typing

import requests as requests


class CryptBot:

    def __init__(self, token, debug=False):
        self.debug = debug
        if self.debug:
            self.api = f'https://testnet-pay.crypt.bot/api/'
            self.headers = {'Host': 'testnet-pay.crypt.bot', 'Crypto-Pay-API-Token': token}
        else:
            self.api = f'https://pay.crypt.bot/api/'
            self.headers = {'Host': 'pay.crypt.bot', 'Crypto-Pay-API-Token': token}

    def create_invoice(self, asset: str, amount: str, description: typing.Optional[str] = None,
                       hidden_message: typing.Optional[str] = None, paid_btn_name: typing.Optional[str] = None,
                       paid_btn_url: typing.Optional[str] = None, payload: typing.Optional[str] = None,
                       allow_comments: typing.Optional[bool] = True, allow_anonymous: typing.Optional[bool] = True,
                       expires_in: typing.Optional[int] = None):

        params = {
            'asset': asset,
            'amount': amount,
            'description': description,
            'hidden_message': hidden_message,
            'paid_btn_name': paid_btn_name,
            'paid_btn_url': paid_btn_url,
            'payload': payload,
            'allow_comments': allow_comments,
            'allow_anonymous': allow_anonymous,
            'expires_in': expires_in
        }
        try:
            r = requests.request(method='POST', url=self.api + 'createInvoice',
                                 params=params,
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def transfer(self, user_id: str, asset: str, amount: str, spend_id: str, comment: typing.Optional[str] = None,
                 disable_send_notification: typing.Optional[bool] = None):
        params = {
            'user_id': user_id,
            'asset': asset,
            'amount': amount,
            'spend_id': spend_id,
            'comment': comment,
            'disable_send_notification': disable_send_notification
        }
        try:
            r = requests.request(method='POST', url=self.api + 'transfer',
                                 params=params,
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def get_invoices(self, asset: typing.Optional[str] = None, invoice_ids: typing.Optional[str] = None,
                     status: typing.Optional[str] = None, offset: typing.Optional[int] = None,
                     count: typing.Optional[int] = None):
        params = {
            'asset': asset,
            'invoice_ids': invoice_ids,
            'status': status,
            'offset': offset,
            'count': count
        }
        try:
            r = requests.request(method='GET', url=self.api + 'getInvoices',
                                 params=params,
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def get_balance(self):
        try:
            r = requests.request(method='GET', url=self.api + 'getBalance',
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def get_exchange_rates(self):
        try:
            r = requests.request(method='GET', url=self.api + 'getExchangeRates',
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def get_currencies(self):
        try:
            r = requests.request(method='GET', url=self.api + 'getCurrencies',
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)

    def get_me(self):
        try:
            r = requests.request(method='GET', url=self.api + 'getMe',
                                 headers=self.headers)
            return r.json()
        except Exception as e:
            print(e)
