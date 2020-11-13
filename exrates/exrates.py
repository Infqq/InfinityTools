from pycbrf import ExchangeRates, Banks
from time import gmtime, strftime

class currency():
        def get(self, name: str):
                tt = strftime("%Y-%m-%d", gmtime())
                rates = ExchangeRates(tt, locale_en=True)
                result = rates[name].rate
                return result
