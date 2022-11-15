import socket
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen(5)

while True:
    clientsocket , address = s.accept()
    print(f"cconnection is estavlished from socket{address}")
    clientsocket.send(bytes("welcome","utf-8"))


