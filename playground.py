import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 'C7HEEAH47D31HNMD'
NEWS_API_KEY = '7a59cf2f7bd342bf9f05c15562c81430'

SID = "ACe42a5bc058466ca50272c505ae359efe"
TOKEN = "4eac8f83d3a850170a95328e599c9a69"
P_NUM = "+12135137716"

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
