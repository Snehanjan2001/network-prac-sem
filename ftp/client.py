import sys 
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',10000))

file_name = client.recv(1024).decode()
file_name= "Hello"+file_name
file =open(file_name,"wb")
data = client.recv(4097)
file.write(data)
file.close()
client.close()