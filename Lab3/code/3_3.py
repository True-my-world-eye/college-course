def count(num):
    res=0
    binary_num=[]
    while(num>0):
        binary_num.append(num%2)
        num//=2
    sorted(binary_num,reverse=True);
    for i in binary_num:
        if i==1:
            res+=1
    binary_str = ''.join(map(str, binary_num[::-1]))
    return res,binary_str

with open("Lab3/data/binary_analysis.txt","w") as f:
    for i in range(8,1001):
        res,binary_num=count(i)
        flag=True if res==1 else False
        f.write(f"{i}->{binary_num} | 1的个数 {res} | "+("是2的幂" if flag else "不是2的幂")+"\n")