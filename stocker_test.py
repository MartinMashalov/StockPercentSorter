import stocker
from yahoo_fin import stock_info as si

stock_arr = []
percent_dif_arr = []

for stock in stock_arr:
    stocker_price = stocker.predict.tomorrow(stock)
    high_price = (1+stocker_price[1]*0.01)*stocker_price[0]
    low_price = (1-stocker_price[1]*0.01)*stocker_price[0]

    current_price = si.get_live_price(stock)

    if current_price < low_price:
        percent_dif_arr.append(((low_price - current_price)/low_price)*100)
    elif current_price > high_price:
        percent_dif_arr.append(((current_price - high_price) / high_price) * 100)

print(percent_dif_arr.sort())