from pyccc.base import ExchangeBase


class CEXIO(ExchangeBase):
    _public_endpoint = "https://cex.io/api"
    _private_endpoint = _public_endpoint

    # def _get_signature(self):
    #     message = "{}{}{}".format(self._get_nonce(),
    #                               self.settings['userid'],
    #                               self.settings['api_key'])
    #     return hmac.new(self.settings['secret'].encode('utf-8'),
    #                     message.encode('utf-8'),
    #                     hashlib.sha256).hexdigest().upper()

    # def _prepare_request(self, params={}, data={}, headers={}):
    #     """CEX.io uses key + signature + nonce as data args."""
    #     data['key'] = self.settings['api_key']
    #     data['signature'] = self._get_signature()
    #     data['nonce'] = self._get_nonce()
    #     return params, data, headers

    def get_ticker(self, ticker, against='USD'):
        endpoint = "{}/ticker/{}/{}".format(self._public_endpoint,
                                            ticker,
                                            against)

        raw = self._get(endpoint)
        return {'last': float(raw['last']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['volume'])}
