# 原始数据列表
data = [
    {'id': '7', 'name': 'b'},
    {'id': '5', 'name': 'c'},
    {'id': '1', 'name': 'a'},
    {'id': '2', 'name': 'g'},
    {'id': '6', 'name': 'f'}
]

# 按id从小到大排序
sorted_data = sorted(data, key=lambda x: int(x['id']))

print(sorted_data)