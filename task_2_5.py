prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for price in prices:
    print(f'{price // 1:.0f} руб {round(price % 1 * 100):02.0f} коп', end=', ')
print()
print(id(prices))
prices.sort()
print(id(prices))
for price in prices:
    print(f'{price // 1:.0f} руб {round(price % 1 * 100):02.0f} коп', end=', ')
new_prices = prices[::-1]
print()
print(id(prices))
print(id(new_prices))
for idx in range(5):
    print(f'{new_prices[idx] // 1:.0f} руб {round(new_prices[idx] % 1 * 100):02.0f} коп', end=', ')
print()

# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# prices.sort(reverse=True)
# print(prices[:5])

# интересный момент
# 70.01 * 100 == 7001  False
# 8.53 * 100 == 853  False
