a= input("Enter the string in binary :")
print ("data recieved")
count =0
for x in a:
    if (x=='1'):
        count=count+1

data=''
if (count%2 != 0):
    data = ("1"+a)
    print(f"the data after adding the pairity bit : {data}")
else:
    data = ("0"+a)
    print(f"the data after adding the pairity bit : {data}")
    



print("Adding error in the 3rd bit from last....")


if (data[-3]=="0"):
    data = data[:-3]+"1"+data[-2:]
    print(f"{data}")
    
else :
    data = data[:-3]+"0"+data[-2:]
    print(f"{data}")

pairity_bit=data[1]
new_data= data[1:]

print("checking....")


count2=0
for y in new_data:
    if (x=='1'):
        count2=count2+1

if count2 %2 == int(pairity_bit):
    print("Error")
else:
    print("Success")
