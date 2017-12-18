from pycccl.base import ExchangeBase


class Liqui(ExchangeBase):
    _public_endpoint = "https://api.liqui.io/api/3"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USD'):
        pair = "{}_{}".format(ticker, against)
        endpoint = "{}/ticker/{}".format(self._public_endpoint, pair)

        raw = self._get(endpoint)[pair]
        return {'last': float(raw['last']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['vol'])}
