import socket
ipaddr ="127.0.0.1"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr  = (ipaddr,1234)


c="Y"

while c.upper()=="Y":
    req_domain=input("Enter the domain name foe the ip :")
    send = s.sendto(req_domain.encode(),addr)
    data,addr= s.recvfrom(1024)
    reply_ip = data.decode().strip()
    print(f"The required ip is {reply_ip}",)
s.close()