A, B, D = map(int, input().split())
sum_num = A + B

if sum_num == 0:
    print(0)
else:
    digits = []
    while sum_num > 0:
        digits.append(str(sum_num % D))
        sum_num = sum_num // D
    # 反转余数
    print(''.join(reversed(digits)))