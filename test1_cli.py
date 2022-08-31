import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5555))
n=0
# data='fdafas'.encode()
# s.send(data)

# s.send(b' ')
# print(f'send data: [{data}]')
n=0
while 1:
    print(f'\r{n}',end='')
    data=s.recv(1024)
    if not data:
        break
    print(data.decode())
    n+=1
    time.sleep(0.5)
