from currency_converter import CurrencyConverter
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.convert(1,'USD','KRW'))

