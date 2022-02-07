import socket

print("I am a client")

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#be sure to hardcode IP address to make it work between machines
c.connect(('localhost',9999))

print(c.recv(2048).decode())