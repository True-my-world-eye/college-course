import math
nums=[]

for x in range(1,10000001):
    a2 = x + 101
    b2 = x + 2026
    a = int(math.isqrt(a2))
    b = int(math.isqrt(b2))
    if a * a == a2 and b * b == b2:
        nums.append(x)
print(nums)