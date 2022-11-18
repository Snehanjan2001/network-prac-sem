lst = []
a = int(input("Enter number of elements : "))
  
for i in range(0, a):
    ele = int(input())
  
    lst.append(ele) 

recv=[]
recv_ack=[]

ack_index=1
start=1
end=3
while len(lst)>=len(recv):
    if ack_index %3 ==0:
        print(f"Ack for index {ack_index} not recieved")
        print(f"Sending frames again {start-1} to {end-1}")
        ack_index+=1
    else:
        print(f"Sending {start} to {end}")
        start+=1
        end+=1
        print(f"Ack recieved for {ack_index}")
        if ack_index>=len(lst):
            recv.append(lst[ack_index-1])
        ack_index+=1
        