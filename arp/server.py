import socket

#table consisting the ipa and mac of given any rnadom4
table={
    '192.35.3.2':'1E.4A.5C.6D',
    '192.35.3.4':'1E.4H.5C.6D',
    '192.35.5.2':'1B.4A.5C.6D',
    '192.36.3.2':'1E.4A.5J.6L',
}

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen()
clientsocket,address = s.accept()
print("Connection from ",address," has been established")

ip = clientsocket.recv(1024)
ip=ip.decode("utf-8")
mac = table.get(ip,"no entry")
clientsocket.send(mac.encode())

