from binance.spot import Spot 
import time

client = Spot()

#API Keys
api_key = <Your API Key>
api_secret = <Your API Secret>


#Set API 
client = Spot(key=api_key, secret=api_secret)




def buy():
    price = client.ticker_price(symbol='BTCUSDT')
     # Posting Buy Order
    params1 = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': '0.00055',
        'price': price['price'],
    }

    response = client.new_order(**params1)

    #Response Calculation
    while True:
        res = client.get_open_orders(symbol='BTCUSDT')
        if len(res) == 0:
            sample_price = response['fills'][0]['price']
            final_price = float(sample_price) + 0.5
            return final_price
            break
        else:
            continue



#final_price = buy()

def sell(final_price):
    # Posting Sell Order
    params2 = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': '0.00055',
        'price': final_price,
    }
    response2 = client.new_order(**params2)
    print(response2)


while True:
    res = client.get_open_orders(symbol='BTCUSDT')
    if len(res) == 0:
        print("Open order not found INITIALIZING Order")
        final_price = buy()
        sell(final_price)
        continue
    else:
        print("Open Order Detected")
        time.sleep(5)
        continue
