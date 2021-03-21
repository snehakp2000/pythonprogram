#generate positive list
list=[1,-3,4,5,-6,14,-9,56]
new=[x for x in list if x>0]
print(new)
#square of n numbers
list=[]
n=int(input("enter the number of list element "))
for i in range(n):
    x=int(input("enter the element "))
    list.append(x)
    i=i+1
print(list)
list2=[x**2 for x in list]
print(list2)
word=input("enter the word ")
vowels="aeiouAEIOU"
list=[x for x in word if x in vowels]
print(list)
#ordinal value
list=[]
word=input("enter the word ")
list=[ord(x) for x in word]
print(list)