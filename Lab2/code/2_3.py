def prime_factor(n):
    primes = []
    exponents = []
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            # 统计这个质因子出现多少次
            while n % i == 0:
                cnt += 1
                n = n // i
            primes.append(i)
            exponents.append(cnt)
        i += 1
    
    # 如果最后剩下的数 >1，说明它本身是质因子
    if n > 1:
        primes.append(n)
        exponents.append(1)
    
    # [[质因子列表], [指数列表]]
    return [primes, exponents]

n=int(input("Enter a number: "))
print("Prime factors of", n, "are:", prime_factor(n))