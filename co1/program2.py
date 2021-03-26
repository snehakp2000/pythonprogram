x=int(input("enter the current year "))
y=int(input("enter the end year "))
print("leap years are:")
while x<=y:
    if x%4==0 or x%400==0 and x%100!=0:
        print(x)
    x=x+1
