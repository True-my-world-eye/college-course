stock_list=[]
with open("Lab3/data/info_stocks.txt","r") as f:
    for line in f:
        line=line.strip()
        stock_dict={}
        items=line.split(",")
        for item in items:
            k, v = item.split(":")
            k = k.strip().strip("'")
            v = v.strip().strip("'")

            stock_dict[k] = v if k == "name" else float(v)  # 数值转浮点
        stock_dict["total"] = stock_dict["price"] * stock_dict["shares"]

        stock_list.append(stock_dict)
sorted_stocks=sorted(stock_list, key=lambda x: (-x["total"], -x["price"]))
for stock in sorted_stocks:
    print(f"{stock['name']}: price={stock['price']}, total={stock['total']}")

filter_stocks=filter(lambda x : x["price"]>100,stock_list)
for stock in filter_stocks:
    print(f"{stock['name']}: price={stock['price']}, total={stock['total']}")