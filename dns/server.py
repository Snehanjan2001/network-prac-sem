import socket

dns_table={
    "www.google.com":"192.65.36.2",
    "www.haloom.com":"192.66.36.2",
    "www.loom.com":"192.65.75.2",
    "www.joom.com":"192.65.36.3",
}

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("starting server ...")
s.bind(('',1234))

s.connect(("127.0.0.1",1234))
while True:
    data,address=s.recvfrom(1024)
    #the connection is established
    print(f"connection established at address {address}")
    data = data.encode()
    ip = dns_table.get(data,"not found").encode()

