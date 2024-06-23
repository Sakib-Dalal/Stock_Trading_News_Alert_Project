import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ''
NEWS_API_KEY = ''

SID = ""
TOKEN = ""
P_NUM = "+"

stock_parameter = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'full',
    'apikey': STOCK_API_KEY
}

news_parameter = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_API_KEY
}

stock_respond = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
stock_respond.raise_for_status()
data = stock_respond.json()

data_list = [value for (key, value) in data.items()]
data_list = [v for k, v in data_list[1].items()]

yesterday_closing_price = data_list[0]['4. close']
day_before_yesterday_closing_price = data_list[1]['4. close']

print(yesterday_closing_price, day_before_yesterday_closing_price)
