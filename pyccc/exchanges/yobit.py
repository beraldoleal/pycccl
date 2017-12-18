from pn.base import ExchangeBase


class YoBit(ExchangeBase):
    _public_endpoint = "https://yobit.net/api/2"
    _private_endpoint = _public_endpoint

    def get_ticker(self, ticker, against='USD'):
        pair = "{}_{}".format(ticker.lower(), against.lower())
        endpoint = "{}/{}/ticker".format(self._public_endpoint, pair)

        raw = self._get(endpoint)['ticker']
        return {'last': float(raw['last']),
                '24highest': float(raw['high']),
                '24lowest': float(raw['low']),
                '24volume': float(raw['vol'])}
