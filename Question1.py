def find_best_days(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0
    
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = i
    
    return (buy_day+1, sell_day+1)
prices = [100, 180, 260, 310, 40, 535, 695]
print(f"Prices on Each Date:")

for i in range(0,len(prices)):
    print("Price of Day",i+1,"is",prices[i])
best_days = find_best_days(prices)
print(f"Buy on day {best_days[0]} and sell on day {best_days[1]}")
