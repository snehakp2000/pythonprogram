list=["park","python","java","javascript"]
count=0
for x in list:
    for i in x:
        if i=='a':
            count+=1
print(f"occurances of a is {count} times" )
