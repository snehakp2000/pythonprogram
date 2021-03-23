def fact(a):
    f=1
    i=1
    while i<=a:
        f=f*i
        i=i+1
    return f
num=int(input("enter the number"))
result=fact(num)
print(f"factorial of {num} is {result}")