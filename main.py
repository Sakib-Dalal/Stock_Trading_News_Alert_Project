import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ''
NEWS_API_KEY = ''

SID = "Twilio SID"
TOKEN = "Twilio Token"
P_NUM = "Twilio Phone Number"

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

yesterdays_closing_price = data_list[0]['4. close']
day_before_yesterdays_closing_price = data_list[1]['4. close']

print(yesterdays_closing_price, day_before_yesterdays_closing_price)

difference = abs(float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price))
print(difference)

diff_percent = (difference / float(yesterdays_closing_price)) * 100
print(diff_percent)


def get_news():
    news_respond = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_respond.raise_for_status()
    news_data = news_respond.json()
    return news_data['articles'][0]


def send_sms(msg):
    client = Client(SID, TOKEN)
    message = client.messages.create(to='+918080535001', from_=P_NUM, body=msg)
    print(message.status)


if diff_percent > 5:
    title = get_news()['title']
    description = get_news()['description']
    print(title, description)
    formatted_article = f"TSLA: {round(diff_percent, 2)} \nHeadline: {title} \nBrief: {description}"
    send_sms(msg=formatted_article)
