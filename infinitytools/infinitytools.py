from pycbrf import ExchangeRates, Banks
from time import gmtime, strftime
import socket

mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995]


class currency():
        def get(self, name: str):
                tt = strftime("%Y-%m-%d", gmtime())
                rates = ExchangeRates(tt, locale_en=True)
                result = rates[name].rate
                return result

class scan():
        def get(self, host: str):
                p = f'Открытые порты {host}:\n'
                for port in mas:
                        s = socket.socket()
                        s.settimeout(1)
                        try:
                                s.connect((host, port))
                        except socket.error:
                                pass
                        else:
                                s.close
                                p = p + str(port) + ' '
                                return p
