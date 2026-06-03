n=int(input())

for i in range(1, n+1):
    print(" " * (n - i)+ "*", end="")
    if i != 1:
        print(" " * (1 + 2 * (i - 2)) + "*", end="")
    print()

for i in range(n-1, 0, -1):
    print(" " * (n - i)+ "*", end="")
    if i != 1:
        print(" " * (1 + 2 * (i - 2)) + "*", end="")
    print()