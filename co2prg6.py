str=input("enter the string")
n=len(str)
a=str.split(" ")
count=0
for i in range(0,n):
   if(str[i]!=' '):
       count+=1
print(f"count={count}")

