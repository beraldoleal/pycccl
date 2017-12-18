from pycccl.base import ExchangeBase


class BitBay(ExchangeBase):
    _public_endpoint = "https://bitbay.net/API/Public"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USD'):
        pair = "{}{}".format(ticker, against)
        endpoint = "{}/{}/ticker.json".format(self._public_endpoint, pair)

        raw = self._get(endpoint)
        return {'last': float(raw['last']),
                '24highest': float(raw['max']),
                '24lowest': float(raw['min']),
                '24volume': float(raw['volume'])}
