import socket
import sys 
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',10000))
s.listen(1)

clientsocket,address = s.accept()
file_name="sample.txt"
clientsocket.sendall(file_name.encode())
file = open("sample.txt","rb")

data = file.read()
clientsocket.sendall(data)
file.close()
clientsocket.close()
s.close()





