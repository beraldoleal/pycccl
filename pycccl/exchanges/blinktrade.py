from pycccl.base import ExchangeBase


class BlinkTrade(ExchangeBase):
    _public_endpoint = "https://api.blinktrade.com/api/v1"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='BRL'):
        endpoint = "{}/{}/ticker".format(self._public_endpoint, against)
        params = {"crypto_currency": ticker}

        raw = self._get(endpoint, params=params)
        return {'last': float(raw['last']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['vol'])}
