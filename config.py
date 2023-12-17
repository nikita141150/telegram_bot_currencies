import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('TOKEN')


currencies = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR'
}


API_KEY = '146e5295d845336e52a65515677c22b7'
