import csv

class Book:
    def __init__(self,title,price):
        self.__price=price
        self.__title=title

    def discount(self):
        self.__price *= 0.8

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price
    
books=[]
with open("Lab4/books.csv","r") as f:
    reader=csv.DictReader(f)
    # print(reader)
    for row in reader:
        b=Book(row["title"],float(row["price"]))
        b.discount()
        books.append(b)
books.sort(key=lambda x:-x.get_price())
for b in books:
    print(b.get_title(),b.get_price())

