import socket, time, datetime, os
from threading import Thread
# from concurrent import futures
os.system('')
host='127.0.0.1'
port=5555
clis=[]
ml=[
    # ('dynv6_2.0.exe',open(r'C:\Users\moiiii\Downloads\dynv6_2.0.exe','rb').read()),
    'text1',
    'text2',
    # ('aria2.rar',open(r'C:\Users\moiiii\Downloads\【软件小】Aria2.rar','rb').read()),
    # ('856799.png',open(r'C:\Users\moiiii\Downloads\856799.png','rb').read())
    ]


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

def accept(s,thsnum):
    global clis
    global ml
    while 1:
        print(f'{thsnum} '+color('▮ ','red')+f'[{gettime()}] - '+color("ready for connection",'green'))
        cli, ipaddr=s.accept()
        cli.send('1'.encode())
        data=cli.recv(1024)
        # print(data.decode())
        print(f'{thsnum} '+color('✔ ','red')+f'[{gettime()}] - '+f'{ipaddr[0]}:{ipaddr[1]} '+color('connected','green'))
        transmission(cli,thsnum)
        cli.close()
        print(f'{thsnum} '+color('◀ ','red')+f'[{gettime()}] - '+color("close connection",'green'))
        time.sleep(0.1)

def transmission(cli,thsnum):
    global ml
    while 1:
        if ml:
            data=ml[0]
            del ml[0]
            if isinstance(data,tuple):
                print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color(f'Start to send file {data[0]}...','green'))
                transmit(cli,data[1],f'file - {data[0]}',thsnum)
            else:
                print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color(f'Start to send string {data}...','green'))
                transmit(cli,data.encode(),'str',thsnum)
            break
        time.sleep(0.1)


def transmit(cli,data,dtype,thsnum):
    # print(data)
    cli.send(dtype.encode())
    cli.recv(512)
    print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color('Head transfer success','green'))
    # print(data)
    cli.sendall(data)
    cli.close()
    print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color('Body transfer success, exiting...','green'))
    # isRecieved=cli.recv(512)
    # if isRecieved=='1':
    #     print(f'Successfully transmited file {dtype.replace("file - ","")}')


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
print('start listen')
# thsnum=2
# pool=futures.ThreadPoolExecutor(thsnum)
# tid=[i for i in range(1,thsnum+1)]
# ths=[pool.submit(accept,s,i) for i in tid]
# pool.map(accept,tid)
# while 1:
#     time.sleep(1)
# print(f'[{gettime}]'+' - '+color('Transmission Threads started','green'))

ths1=Thread(target=accept,args=(s,1))
ths2=Thread(target=accept,args=(s,2))
ths1.start()
ths2.start()
ths1.join()
ths2.join()
# accept(s)
# cli, ipaddr=s.accept()
# cli.send('1'.encode())
# data=cli.recv(1024)
# print(data.decode())
# print(f'{ipaddr} connected')
# transmission(cli)


