nums = []
result = 1

for i in range(1, 31):
    if i % 2 == 0 and i % 4 != 0:
        nums.append(i)
        result *= i

print("能被2整除但不能被4整除的数：")
print(nums)
print(f"乘积为：{result}")