import requests

src = 'https://www.cbr-xml-daily.ru/daily_json.js'
exchange_rate = requests.get(src)
exchange_rate_dict = exchange_rate.json()['Valute']
with open('currency.csv', 'w') as file:
    
    for value in exchange_rate_dict.values():
        file.write(f"{value['CharCode']}, {value['Name']}, {value['Value']}\n")

# print(exchange_rate_dict['Valute'])