s=input("enter the string")
f=s[0]
for x in s:
    if x==f:
        n=s[1:].replace(x,"$")
    new=f+n
print(new)
