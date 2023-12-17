import requests
import json
from config import currencies, API_KEY


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount):
        if quote == base:
            raise ConvertionException('Ввели одинаковые валюты')
        quote_sticker, base_sticker = currencies[quote], currencies[base]
        try:
            quote_sticker = currencies[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_sticker = currencies[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('Не удалось обработать'
                                      f'количество {amount}')

        r = requests.get('https://currate.ru/api/?get=rates&pairs='
                         f'{quote_sticker}{base_sticker}&key={API_KEY}')
        total_base = json.loads(r.content)['data'][f'{quote_sticker}{base_sticker}']
        return total_base
