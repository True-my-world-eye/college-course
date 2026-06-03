matrix = [[1, 2, 3], [7, 8, 9], [6, 5, 4]]

sum=0

for i in range(3):
    sum+=matrix[i][i]
print(f"主对角线元素之和为：{sum}")