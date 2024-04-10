def chocolate_bars_affordability(total_money, price_per_bar):  
    bars_count = total_money // price_per_bar  
    change = total_money % price_per_bar 
    return bars_count, change  
  
# Example: 
total_money = 100  
price_per_bar = 7  
bars, remaining_money = chocolate_bars_affordability(total_money, price_per_bar)  
print(f"You can buy {bars} chocolate bars and have {remaining_money} left.")
