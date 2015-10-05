import Utilities
from Utilities import parse_to_float


class CurrencyExchangeRateEntry:
    name = ''
    buy_ratio = 1.0
    sell_ratio = 1.0
    time_stamp = ''

    def __init__(self, name, buy, sell, time_stamp):
        self.name = name[0:3]
        self.buy_ratio = parse_to_float(buy)
        self.sell_ratio = parse_to_float(sell)
        self.time_stamp = time_stamp

    def get_pretty_data(self):
        return "%s:  %.4f %.4f  %s" % (self.name, self.buy_ratio, self.sell_ratio, self.time_stamp)

    def print_data(self):
        print self.get_pretty_data()
