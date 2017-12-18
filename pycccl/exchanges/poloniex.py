from pycccl.base import ExchangeBase


class Poloniex(ExchangeBase):
    _public_endpoint = "https://poloniex.com/public"
    _private_endpoint = "https://poloniex.com/tradingApi"

    # def __init__(self, *args, **kwargs):
    #     super(Poloniex, self).__init__(*args, **kwargs)
    #     self.settings = auth['poloniex']
    #     self.subscribers = {"ticker": self.on_ticker,
    #                         "BTC_USDT": self.on_ticker}

    # def _get_signature(self, data):
    #     return hmac.new(self.settings['secret'].encode('utf-8'),
    #                     urlencode(data).encode('utf-8'),
    #                     hashlib.sha512).hexdigest()

    # def _prepare_request(self, params={}, data={}, headers={}):
    #     data['nonce'] = self._get_nonce()
    #     headers['Sign'] = self._get_signature(data)
    #     headers['Key'] = self.settings['api_key']
    #     return params, data, headers

    def _get_tickers(self):
        params = {'command': 'returnTicker'}
        return self._get(self._public_endpoint, params=params)

    def get_ticker(self, ticker, against='USD'):
        all_tickers = self._get_tickers()
        index = "{}_{}".format(against, ticker)
        raw = all_tickers[index]
        return {'last': float(raw['last']),
                '24highest': float(raw['high24hr']),
                '24lowest': float(raw['low24hr']),
                '24volume': float(raw['baseVolume'])}
