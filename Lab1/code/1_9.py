n=int(input())

result=set()

for i in range(1,n+1):
    result.add(i//2)
    result.add(i//3)
    result.add(i//5)

print(len(result))