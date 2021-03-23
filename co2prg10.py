n=int(input("enter the number"))
i=n
print(f"factors of {n} are:")
for x in range(1,n+1):
    if n%x==0:
        print(x)