list1=["red","blue","orange","black"]
list2=["blue","white","orange","green"]
list3=[]
for x in list1:
    if x not in list2:
        list3.append(x)
print(list3)
