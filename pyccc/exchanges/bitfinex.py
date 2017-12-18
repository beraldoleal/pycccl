from pyccc.base import ExchangeBase


class Bitfinex(ExchangeBase):
    _public_endpoint = "https://api.bitfinex.com/v1"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USD'):
        pair = "{}{}".format(ticker, against)
        endpoint = "{}/pubticker/{}".format(self._public_endpoint, pair)

        raw = self._get(endpoint)
        return {'last': float(raw['last_price']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['volume'])}
