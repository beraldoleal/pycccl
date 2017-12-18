from pycccl.base import ExchangeBase


class Bitstamp(ExchangeBase):
    _public_endpoint = "https://www.bitstamp.net/api/v2"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USD'):
        endpoint = "{}/ticker/{}{}".format(self._public_endpoint,
                                           ticker,
                                           against)

        raw = self._get(endpoint)
        return {'last': float(raw['last']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['volume'])}
