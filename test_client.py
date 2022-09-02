import os, sys, signal
import socket, time, datetime
from threading import Thread
# from concurrent import futures
os.system('')
ss=[]

def gettime():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def uop(thsnum,str):
    return f'{thsnum}'+'   '+f'[{gettime()}] - '+str

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
        if is_exit:
            print(uop(f'{thsnum}',color('Exiting','red')))
            return
        print(f"{thsnum} "+color('▮ ','red')+f'[{gettime()}] - '+color("ready for connection",'green'))
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((host,port))
        except Exception as e:
            if 10061 in e.args or 'timed out' in str(e):
                print(uop(thsnum,color('Connection timeout, starting a new connection','red')))
            else:
                print('e:',e.args)
            continue
        # print('a:',a)
        # data=s.recv(1024)
        # # print(data.decode())
        # s.send('1'.encode())
        print(f"{thsnum} "+color('✔ ','red')+f'[{gettime()}] - '+color('connected','green'))
        ss+=[s]
        transmission(s,thsnum)
        s.close()
        # s.
        del ss[ss.index(s)]
        print(f"{thsnum} "+color('◀ ','red')+f'[{gettime()}] - '+color("close connection",'green'))

def transmission(s,thsnum):
    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(0)
    head=None
    while 1:
        if is_exit:
            # print('transmission: is exit')
            # s.close()
            return
        try:
            head=s.recv(1024).decode()
        except:
            pass
        if head:
            s.setblocking(1)
            break
        time.sleep(0.1)
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

def _exit(signum, frame):
    global is_exit
    global ss
    is_exit=1
    print(uop(' ',color('Recieved keyinterrupt, exiting','red')))
    for i in ss:
        print(uop(' ',color(f'Closing socket {i}','red')))
        i.close()
    print(uop(' ',color('Shutting down threads','red')))
    # pool.shutdown(cancel_futures=True)
    # print(uop('',color('Threads have been shut down','red')))
    # sys.exit()


signal.signal(signal.SIGINT,_exit)
signal.signal(signal.SIGTERM,_exit)

host='192.168.0.104'
port=5566

is_exit=0
thcounts=2
# pool=futures.ThreadPoolExecutor(thcounts)
# ths=[]
# for i in range(1,thcounts+1):
#     ths+=[pool.submit(accept,i)]


# while 1:
#     time.sleep(1)
ths=[]
for i in range(1,thcounts+1):
    th=Thread(target=accept, args=(i,))
    th.daemon=True
    ths+=[th]
    th.start()

br=0
while 1:
    for i in ths:
        # print(i.is_alive())
        if i.is_alive():
            time.sleep(0.1)
            continue
        br=1
        break
    if br==1:
        # print('break')
        break
# ths1=Thread(target=accept, args=(1,))
# ths2=Thread(target=accept, args=(2,))

# ths1.start()
# ths2.start()
# ths1.join()
# ths2.join()
# accept()
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',5555))
# data=s.recv(1024)
# print(data.decode())
# s.send('1'.encode())
# print('connected')
# transmission(s)


