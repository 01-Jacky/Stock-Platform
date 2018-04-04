import json

data = json.load(open('symbols.json'))

print(len(data))
for stock in data:
    if stock['symbol'] == 'EAGLU':
        print(stock['name'])