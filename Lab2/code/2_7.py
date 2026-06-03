while True:
    x=int(input("请输入一个数："))
    if x==0:
        print("输入结束")
        break
    
    y=x
    z=0;
    while(y>0):
        z*=10
        z+=y%10
        y//=10
    if x==z:
        print(x,"是回文数")    
    else:
        print(x,"不是回文数")


