import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',1234))
addr = input("Enter IP: ")
s.send(addr.encode())
mac = s.recv(1024)

mac.decode("utf-8")
print("Mac address is : ",mac)