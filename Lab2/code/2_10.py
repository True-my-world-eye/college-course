def mypow(x,n):
    result=1
    for i in range(n):
        result*=x
    return result

x,n=map(int,input().split())
print(mypow(x,n))