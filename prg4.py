str=input("enter the string ")
a=str.split(" ")
list=[]
for x in a:
    if x not in list:
        list.append(x)
for x in list:
    c=0
    for i in a:
        if i==x:
            c=c+1
    print(f"occurence of {x} is {c} times ")
