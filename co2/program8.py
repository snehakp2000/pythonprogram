n=int(input("enter the no. of list items"))
list=[]
for i in range(n):
    a=input("enter the word")
    list.append(a)
for x in list:
    n=len(x)
    for y in list:
        b=len(y)
        if b>n:
            large=b
            word=y
print(f"longest word is {word} with {large} letters")

