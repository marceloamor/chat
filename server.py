# Python program to implement server side of chat room.
import socket
# import select
# import sys
# from thread import *

print("I am a server")

s = socket.socket() 
print('Socket created')

s.bind(('localhost',9999))

s.listen(3)
print('waiting for connection...')

while True:
    c, addr = s.accept()
    print('Connected with ', addr)

    c.send('Welcome to the server')

    c.close()