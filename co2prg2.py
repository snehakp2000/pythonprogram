def febi(x):
    a=0
    b=1
    c=0
    while c<=x:
        print(c)
        a=b
        b=c
        c=a+b
n=int(input("enter the limit"))
febi(n)