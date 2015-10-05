from CurrencyExchangEntry import CurrencyExchangEntry
from bs4 import BeautifulSoup
import graphy
import urllib2

CURRENCY_STATS_URL = 'https://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl'

soup = BeautifulSoup(urllib2.urlopen(CURRENCY_STATS_URL).read(), 'html.parser')
for row in soup('table')[0].tbody('tr'):
    cells = row('td')
    entry = CurrencyExchangEntry(
        cells[0].span.string,
        cells[1].string,
        cells[2].string,
        cells[5].string)
    entry.printData()