from pycccl.base import ExchangeBase


class Binance(ExchangeBase):
    _public_endpoint = "https://api.binance.com/api/v1"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USDT'):
        pair = "{}{}".format(ticker, against)
        endpoint = "{}/ticker/24hr".format(self._public_endpoint)
        params = {'symbol': pair}
        raw = self._get(endpoint, params=params)
        return {'last': float(raw['lastPrice']),
                '24highest': float(raw['highPrice']),
                '24lowest': float(raw['lowPrice']),
                '24volume': float(raw['volume'])}
