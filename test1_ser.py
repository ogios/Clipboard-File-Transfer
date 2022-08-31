import socket
from threading import Thread
import time
host='127.0.0.1'
port=5555
ml=[]

def run():
    global ml
    data=input("INPUT TO GET ML UPDATE>>>")
    ml+=[data]
th=Thread(target=run)
th.start()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
print('start listen')
cli, ipaddr=s.accept()
cli.setblocking(0)
n=0

while 1:
    try:
        cli.recv(1024)
    except Exception as e:
        # print(e)
        if 10054 in e.args:
            print('客户端断开连接')
            break
    print(f'\r{n}',end='')
    if ml:
        print('已输入，等待发送')
        cli.setblocking(1)
        cli.send(ml[0].encode())
        print('已发送')
        del ml[0]
        break
    n+=1
    time.sleep(0.1)

# if not data:
#     print('no data')
# print(data)
# data1=cli.recv(1024)
# print('data1:'+data1)
cli.close()