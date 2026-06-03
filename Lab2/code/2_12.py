from functools import reduce

products = [
    {'product': '苹果', 'price': 10.5},
    {'product': '香蕉', 'price': 5.2},
    {'product': '橘子', 'price': 7.8},
    {'product': '草莓', 'price': 14.0},
    {'product': '苹果', 'price': 12.0},
    {'product': '葡萄', 'price': 15.3}
]

price = list(map(lambda x: x['price'], products))

avg=reduce(lambda x, y: x + y, price) / len(price)
print(f"平均价格: {avg:.2f}")
sorted_products = sorted(products, key=lambda x: x['price'], reverse=True)
high_price_products = list(filter(lambda x : x['price'] > avg, sorted_products))

print("价格高于平均价格的商品:")
for product in high_price_products:
    print(f"{product['product']}: {product['price']:.2f}")
