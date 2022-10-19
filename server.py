import socket
s=socket.socket()
print("Socket created")
s.bind(('',9999))
s.listen(5)
print('Waiting')
while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("Connected with",addr,name)
    c.send(bytes("Hello "+str(name)+" Welcome to sockets",'utf-8'))
    c.close()