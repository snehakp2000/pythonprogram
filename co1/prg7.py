list1=[2,4,8,9]
list2=[1,2,5,8]
list3=[]
if len(list1)==len(list2):
    print("lists have same length")
else:
    print("list have different length")
x=sum(list1)
y=sum(list2)
if x==y:
    print("sums are equal")
else:
    print("sums are different")
for x in list1:
    if x in list2:
        list3.append(x)
    else:
        print("no common elements")
print(f"common element are present they are {list3}")
