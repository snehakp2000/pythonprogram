x=int(input("enter first number "))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x<y:
    if y<z:
        print(f"{z} is large")
    else:
        print(f"{y} is large")
else:
    if x<z:
        print(f"{z} is large")
    else:
        print(f"{x} is large")
