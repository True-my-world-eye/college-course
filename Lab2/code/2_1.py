def count(s):
    upper=lower=digit=other=0
    for char in s:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
        elif char.isdigit():
            digit+=1
        else:
            other+=1
    return (upper,lower,digit,other)

s=input()
print(count(s))