s=input().lower()

count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

char, cnt = sorted_items[0]
print(char, cnt)