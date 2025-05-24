import requests
import json

url = 'https://v6.exchangerate-api.com'
apiKey = '2b3608875101349f3b6a5da3'
curList = {'USD', 'EUR', 'GBP', 'JPY', 'CNY', 'CHF'}

def get_endpoint(currency):
    endpoint = '/v6/' + apiKey + '/latest/' + currency
    return endpoint

def get_conversation_rates(data):
    rates = data['conversion_rates']
    return rates

def get_custom_crrency(data, currency):
    exchangeRate = data[currency]
    return exchangeRate

def get_exchange_rate():
    response = requests.get(url + get_endpoint('RUB'))
    data = response.content.decode('utf-8')
    decoder = json.JSONDecoder()
    python_obj = decoder.decode(data)
    return python_obj

def get_api_currencies(Val):
    customCurr = get_conversation_rates(currencies_obj)
    return round(1/(get_custom_crrency(customCurr, Val)), 2)


currencies_obj = get_exchange_rate()
