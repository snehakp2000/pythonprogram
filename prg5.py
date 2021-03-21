list=[]
n=int(input("enter the no. of items "))
for x in range(n):
    x=int(input("enter the item "))
    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)
