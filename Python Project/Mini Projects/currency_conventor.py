from requests import get
from pprint import PrettyPrinter


BASE_URL = 'https://free.currconv.com/'
API_KEY = 'fca_live_3Tu9p2NG497BCEnf1YuJSEaREUvaGsaxgcucV7eD'


printer = PrettyPrinter()


def getCurrencies():
    endpoint = f'api/v7/currencies?apikey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()['result']
    
    data = list(data.items())
    data.sort()
    
    return data
    


def printCurrencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f'{_id} - {name} - {symbol}')


def exchangeRate(currency1, currency2):
    endpoint = f'api/v7/convert?q={currency1}_{currency2}&compact=ultra&apikey={API_KEY}'
    url = BASE_URL + endpoint
    response = get(url)
    
    data = response.json()
    
    if len(data) == 0:
        print('Invalid currencies.')
        return
    
    return list(data.values())[0]
    print(f'{currency1} -> {currency2} = {rate}')
    
    return rate


def convert(currency1, currency2, amount):
    rate = exchangeRate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print('Invalid amount.')
        return
    
    converted_amount = rate * amount 
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount

def main():
    currencies = getCurrencies()
    
    print('Welcome to the Currencies Converter!')
    print('List - List the differnt currencies')
    print('Convert - Convert from one currency to another')
    print('Rate - Get the exchange rate of two currencies')
    print()
    
    while True:
        command = input('Enter a command (a to quit): ').lower()
        
        if command == 'q':
            break
        elif command == 'list':
            printCurrencies(currencies)
        elif command =='convert':
            currency1 = input('Enter a base currency : ').upper()
            amount = input(f'Enter an amount in {currency1}: ')
            currency2 = input('Enter a currency to convert to : ').upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
           currency1 = input('Enter a base currency : ').upper()
           currency2 = input('Enter a currency to convert to : ').upper()
           exchangeRate(currency1, currency2)
        else:
            print('Invalid command. Please try again.')

main()
            
            
      