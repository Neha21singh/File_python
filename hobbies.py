f=open('hobby.txt',mode='a+')
i=0
while i<5:
    n=input("enter your hobbies name...........")
    i=i+1
    data=f.write(n)
    f.write("\n")
data=f.read()
f.close()

