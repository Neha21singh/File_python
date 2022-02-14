def count():
    f=open("mssg.txt",'r')
    d=f.read()
    w=d.split()
    for i in w:
        if i=='MY'or i=='me':
            print(i)
        f.close()
count()