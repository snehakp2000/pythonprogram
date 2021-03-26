str1=input("enter first string")
str2=input("enter second string")
newstr1=str2[:1]+str1[1:]
newstr2=str1[:1]+str2[1:]
print(newstr1+" "+newstr2)
