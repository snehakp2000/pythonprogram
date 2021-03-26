str=input("enter the string")
if (len(str)>2):
    if str[-3:]=='ing':
        str+='ly'
    else:
        str+='ing'
print(str)
