#Python program to copy odd lines of one file to other

f1 = open("program2a.txt", "w")
f2 = open("program2b.txt", "w")
n = int(input("Enter the number of lines:"))
for i in range(n):
    f1.write(input("Enter some text:")+"\n")
# f1.write("Hey\n")
# f1.write("I\n")
# f1.write("am\n")
# f1.write("Aparna\n")
f1.close()
f1 = open("program2a.txt", "r")
count = 1
for i in f1:
    if count % 2 == 0:
        count += 1
        continue
    f2.write(i)
    count += 1
f1.close()
f2.close()