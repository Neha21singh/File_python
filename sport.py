f=open('sport.txt',mode='w+')
i=0
while i<5:
    n=input("enter your sport name...........")
    i=i+1
    data=f.write(n)
    f.write("\n")
data=f.read()
print()
f.close()
