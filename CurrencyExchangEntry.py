import Utilities
from Utilities import parse_to_float


class CurrencyExchangEntry:
    currency = ''
    buy_ratio = 1.0
    sell_ratio = 1.0
    time_stamp = ''

    def __init__(self, name, buy, sell, time_stamp):
        self.currency = name[0:3]
        self.buy_ratio = parse_to_float(buy)
        self.sell_ratio = parse_to_float(sell)
        self.time_stamp = time_stamp

    def printData(self):
        print "%s:  %.4f %.4f   @%s" % (self.currency, self.buy_ratio, self.sell_ratio, self.time_stamp)

