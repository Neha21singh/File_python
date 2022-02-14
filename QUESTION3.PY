f=open('file-question3.txt',mode='r+')
f.write=banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    print(banks_list[i])
    i=i+1
data=f.read()
print(data)
f.close()

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# i=0
# while i<len(banks_list):
#     print(banks_list[i])
#     i=i+1
