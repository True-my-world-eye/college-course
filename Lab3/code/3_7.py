with open("Lab3/data/out.txt","w") as f:
    while(1):
        x=input()
        if x == "@":
            break
        else:
            f.write(x)


