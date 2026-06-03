people=[
    {"name":"xiaoming","age":25},
    {"name":"xiaohong","age":10},
    {"name":"xiaohua","age":18}
]
result = filter(lambda p: p["age"] < 20, people)

for p in result:
    print(p["name"])