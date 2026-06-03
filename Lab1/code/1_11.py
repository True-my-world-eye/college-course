n=int(input())

nums = list(map(int, input().split()))

odd_count = 0  # 奇数
even_count = 0  # 偶数

for num in nums:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print(f"奇数个数：{odd_count}")
print(f"偶数个数：{even_count}")