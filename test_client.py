import os
import socket, time,datetime
from threading import Thread
os.system('')
ss=[]

def gettime():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def color(string, color):
    dic = {
        'white': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'black': '\033[37m'
    }
    return dic[color]+string+'\033[0m'

def accept(thsnum):
    global ss
    while 1:
        print(f"{thsnum} "+color('▮ ','red')+f'[{gettime()}] - '+color("ready for connection",'green'))
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('127.0.0.1',5555))
        data=s.recv(1024)
        # print(data.decode())
        s.send('1'.encode())
        print(f"{thsnum} "+color('✔ ','red')+f'[{gettime()}] - '+color('connected','green'))
        ss+=[s]
        transmission(s,thsnum)
        s.close()
        print(f"{thsnum} "+color('◀ ','red')+f'[{gettime()}] - '+color("close connection",'green'))

def transmission(s,thsnum):
    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    head=s.recv(512).decode()
    print(thsnum,'  '+f'[{gettime()}] - '+color('Get head successfully: ','green')+head)
    if head=='str':
        s.send('1'.encode())
        print(thsnum,'  '+f'[{gettime()}] - '+color('Recieving string...','green'))
        tmp=''
        while 1:
            data=s.recv(1024)
            if not data:
                break
            tmp+=data.decode()
        print(f"{thsnum}   "+f'[{gettime()}] - '+color('>>> ','red')+tmp)
    else:
        s.send('1'.encode())
        print(thsnum,f'  '+f'[{gettime()}] - '+color(f'Recieving {head}...','green'))
        f=open(f'./recv/{head.replace("file - ","")}', 'wb')
        while 1:
            data=s.recv(1024)
            if not data:
                print(thsnum,'  '+f'[{gettime()}] - '+color(f'{head} successfully transmited','green'))
                break
            f.write(data)
        f.close()

ths1=Thread(target=accept, args=(1,))
ths2=Thread(target=accept, args=(2,))
ths1.start()
ths2.start()
ths1.join()
ths2.join()
# accept()
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',5555))
# data=s.recv(1024)
# print(data.decode())
# s.send('1'.encode())
# print('connected')
# transmission(s)


