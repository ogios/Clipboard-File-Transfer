import sys, json
from threading import Thread
import datetime, random, time, os
import socket
os.system('')



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

ok=color('[ OK ]','green')
fatal=color('[ FATAL ]','red')

def gettime():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def uop(thsnum,str):
    return f'{thsnum}'+'   '+f'[{gettime()}] - '+str


def getarg(arg,default=None):
    global args
    try:
        for i in args:
            if i==arg:
                data=[]
                for a in args[args.index(i)+1:]:
                    if '-' in a:
                        break
                    data+=[a]
                if len(data)==1:
                    return data[0]
                else:
                    return data
        return default
    except:
        return default
    



class mission:
    def __init__(self, host=None, port=None, thsnum=2) -> None:
        self.ml=[]
        self.host=host
        self.port=port
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(thsnum)
        self.server=None


    def accept(self, thsnum):
        while 1:
            if self.ml:
                print(uop(thsnum,color("Ready for connection",'green')))
                cli, ipaddr=self.socket.accept()
                print(uop(thsnum,f'{ipaddr[0]}:{ipaddr[1]} '+color('Connected','green')))
                self.transmission(cli,thsnum)
                cli.close()
                print(uop(thsnum,color("Close connection",'green')))
                time.sleep(0.1)
            else:
                break

    def transmission(self, cli, thsnum):
        cli.setblocking(0)
        data=None
        while 1:
            try:
                data=cli.recv(512)
            except Exception as e:
                if 10054 in e.args or 10053 in e.args:
                    print(uop(thsnum,color('Connection lost','red')))
                    break
            if isinstance(data,bytes):
                print(uop(thsnum,color('Connection lost','red')))
                break
            if self.ml:
                try:
                    data=self.ml[0]
                    del self.ml[0]
                except Exception as e:
                    time.sleep(0.1)
                    continue
                cli.setblocking(1)
                if isinstance(data,tuple):
                    print(uop(thsnum,color(f'Start to send file: ','green')+f'{data[0]}'))
                    self.transmit(cli,data[1],f'file - {data[0]}',thsnum)
                else:
                    print(uop(thsnum,color(f'Start to send string: ','green')+f"{data}"))
                    self.transmit(cli,data.encode(),'str',thsnum)
                break
            else:
                break
            time.sleep(0.1)


    def transmit(self,cli,data,dtype,thsnum):
        cli.send(dtype.encode())
        cli.recv(512)
        print(uop(thsnum,color('Head transfer success','green')))
        cli.sendall(data)
        cli.close()
        print(uop(thsnum,color('Body transfer success, exiting...','green')))



def main():
    global args
    global host
    global port
    args=sys.argv[1:]
    ser=json.loads(open('server.json','r').read())

    host=getarg('-h', default=ser["host"])
    port=int(getarg('-p', default=ser['port']))
    ser['host']=host; ser['port']=port
    open('server.json','w').write(json.dumps(ser))
    # h=getarg('-h', default='0.0.0.0')
    # p=int(getarg('-p', default=5566))
    f=getarg('-f', default='')
    char=getarg('-char', default='')
    # # host=h
    # # port=p
    s=mission(host=host, port=port)
    if isinstance(f,list):
        for i in f:
            if os.path.exists(i):
                name=os.path.basename(i)
                s.ml+=[(name,open(i,'rb').read())]
    else:
        if os.path.exists(f):
            name=os.path.basename(f)
            s.ml+=[(name,open(f,'rb').read())]


    if isinstance(char,list):
        for i in char:
            if i:
                s.ml+=[i]
    else:
        if char:
            s.ml+=[char]
    print(s.ml)
    so=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.connect(("192.168.0.0", 48946))
    lan=so.getsockname()[0]
    print(color(f'LAN_HOST - ','green')+f'{lan}')
    print(uop(' ', color(f'LISTENING AT {host}:{port}','green')))
    ths1=Thread(target=s.accept,args=(1,))
    ths2=Thread(target=s.accept,args=(2,))
    ths1.isDaemon=True
    ths2.isDaemon=True
    ths1.start()
    ths2.start()
    ths1.join()
    ths2.join()
    print(color('ALL MISSION COMPLETED','green'))


if __name__=='__main__':
    main()


