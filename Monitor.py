import urllib2
import time
import os
from bs4 import BeautifulSoup
from CurrencyExchangeRateEntry import CurrencyExchangeRateEntry

CURRENCY_STATS_URL = 'https://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl'
RATES_OVER_TIME_FILE = "rates.txt"

rates = dict()

# if os.path.isfile(RATES_OVER_TIME_FILE):
#     os.remove(RATES_OVER_TIME_FILE)

def check_for_changed_rates():
    soup = BeautifulSoup(urllib2.urlopen(CURRENCY_STATS_URL).read(), 'html.parser')
    global row, cells, entry
    for row in soup('table')[0].tbody('tr'):
        cells = row('td')
        entry = CurrencyExchangeRateEntry(
            cells[0].span.string,
            cells[1].string,
            cells[2].string,
            cells[5].string)
        entry.print_data()
        if not rates.has_key(entry.name):
            rates[entry.name] = list()
        rates_for_entry = rates[entry.name]
        last_time_stamp = '00'
        if len(rates_for_entry) > 0:
            last_time_stamp = rates_for_entry[-1].time_stamp
        if entry.time_stamp != last_time_stamp:
            print 'change!!!!'
            rates[entry.name].append(entry)
            write_row_to_file(entry.get_pretty_data())
    write_row_to_file('')


def write_row_to_file(row):
    with open(RATES_OVER_TIME_FILE, "a") as myfile:
        myfile.write("%s\n" % row)


while True:
    check_for_changed_rates()
    time.sleep(30)