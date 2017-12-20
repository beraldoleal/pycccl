from datetime import datetime
import requests
import time


class BasicLog:
    fmt = "{asctime} [{name}] {levelname}: {message}"

    def __init__(self, name=None):
        self.name = name

    def log(self, message, levelname):
        print(self.fmt.format(asctime=datetime.now(),
                              name=self.name,
                              levelname=levelname,
                              message=message))

    def info(self, message):
        self.log(message, "INFO")

    def error(self, message):
        self.log(message, "ERROR")

    def warning(self, message):
        self.log(message, "WARNING")

    def debug(self, message):
        self.log(message, "DEBUG")


class ExchangeBase:
    def __init__(self, *args, **kwargs):
        self.log = BasicLog(self.__class__.__name__)
        self.log.info("Creating component")
        super(ExchangeBase, self).__init__(*args, **kwargs)

    def _get_nonce(self):
        return int(time.time())

    def _get(self, endpoint, params={}, data={}, headers={}):
        # if private:
        #     params, data, headers = self._prepare_request(params,
        #                                                   data,
        #                                                   headers)
        result = requests.get(url=endpoint,
                              params=params,
                              data=data,
                              headers=headers)
        return result.json()

    def _post(self, endpoint, params={}, data={}, json={}, headers={}):
        # if private:
        #     params, data, headers = self._prepare_request(params,
        #                                                   data,
        #                                                   headers)
        result = requests.post(url=endpoint,
                               params=params,
                               data=data,
                               json=json,
                               headers=headers)
        status_code = result.status_code
        if status_code == 403:
            raise Exception("{}: {}".format(status_code, result.reason))
        return result
        return result.json()

    def get_ticker(ticker, against="USD"):
        raise Exception("Not implemented")

    def get_last_price(self, ticker, against='USD'):
        ticker = self.get_ticker(ticker, against)
        return ticker['last']

    def get_24highest(self, ticker, against='USD'):
        ticker = self.get_ticker(ticker, against)
        return ticker['24highest']

    def get_24lowest(self, ticker, against='USD'):
        ticker = self.get_ticker(ticker, against)
        return ticker['24lowest']

    def get_24volume(self, ticker, against="USD"):
        ticker = self.get_ticker(ticker, against)
        return ticker['24volume']

    # def _get_signature(self, data):
    #     raise Exception("Not implemented")

    # def _prepare_request(self, params={}, data={}, headers={}):
    #     raise Exception("Not implemented")

    # def get_balances(self):
    #     raise Exception("Not implemented")

    # def get_fees(self):
    #     raise Exception("Not implemented")

    # def get_address(self, currency='BTC'):
    #     raise Exception("Not implemented")


# class WAMPBase(ExchangeBase, ApplicationSession):
#     def onOpen(self, transport):
#         self.log.info("Openning connection with {}.".format(transport.peer))
#         super(WAMPBase, self).onOpen(transport)
#
#     def onConnect(self):
#         self.log.info("Transport connected.")
#         self.join(self.config.realm)
#
#     def onChallenge(self, challenge):
#         self.log.info("Authentication challenge received.")
#
#     def onLeave(self, details):
#         info = "{}: {}".format(details.reason, details.message)
#         self.log.info("Session left. {}".format(info))
#         self.disconnect()
#
#     async def onJoin(self, details):
#         data = "Authrole: {}. Authmethod: {}".format(details.authrole,
#                                                      details.authmethod)
#         self.log.info("Joined with success. Session: {}".format(data))
#
#         for subscribe, func in self.subscribers.items():
#             self.log.info("Subscribing to {} ...".format(subscribe))
#             try:
#                 await self.subscribe(func, subscribe)
#             except Exception as e:
#                 self.log.error("Could not subscribe to topic {}".format(e))
#
#     def onDisconnect(self):
#         self.log.info("Transport disconnected.")
