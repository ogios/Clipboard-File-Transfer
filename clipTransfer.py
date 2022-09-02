# from concurrent import futures
from threading import Thread
import datetime, random, time, os
from Tools import *
import socket
os.system('')


class mission:
    def __init__(self, host=None, port=None, thsnum=2) -> None:
        self.ml=[]
        self.host=host
        self.port=port
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(thsnum)
        self.server=None
        # self.cli=[]
        # self.clipdata=[]


    # def fileConvert(self,i,clipdata):
    #     match i:
    #         case wp.CF_DIB:
    #             bdata=BytesIO()
    #             data=ImageGrab.grabclipboard()
    #             data.save(bdata,format="PNG")
    #             data=bdata.getvalue()
    #             self.ml+=[(str(time.time())+'.png', data)]    #加入mission行列等待传输
    #         case wp.CF_HDROP:
    #             # for a in wp.GetClipboardData(i):
    #             for a in clipdata:
    #                 with open(a, 'rb') as f:
    #                     data=f.read()
    #                     self.ml+=[(os.path.basename(a), data)]
    #         case wp.CF_UNICODETEXT:
    #             # data=wp.GetClipboardData(i)
    #             self.ml+=[clipdata]


    def accept(self, thsnum):
        # global clis
        # global ml
        while 1:
            print(uop(thsnum,color("Ready for connection",'green')))
            # print(f'{thsnum} '+color('   ','red')+f'[{gettime()}] - '+color("Ready for connection",'green'))
            cli, ipaddr=self.socket.accept()
            # cli.send('1'.encode())
            # data=cli.recv(1024)
            # print(data.decode())
            print(uop(thsnum,f'{ipaddr[0]}:{ipaddr[1]} '+color('Connected','green')))
            # print(f'{thsnum} '+color('   ','red')+f'[{gettime()}] - '+f'{ipaddr[0]}:{ipaddr[1]} '+color('Connected','green'))
            self.transmission(cli,thsnum)
            cli.close()
            print(uop(thsnum,color("Close connection",'green')))
            # print(f'{thsnum} '+color('   ','red')+f'[{gettime()}] - '+color("Close connection",'green'))
            time.sleep(0.1)

    def transmission(self, cli, thsnum):
        # global ml
        cli.setblocking(0)
        data=None
        while 1:
            try:
                data=cli.recv(512)
            except Exception as e:
                # print(e)
                if 10054 in e.args or 10053 in e.args:
                    print(uop(thsnum,color('Connection lost','red')))
                    break
            if isinstance(data,bytes):
                print(uop(thsnum,color('Connection lost','red')))
                break
            # print("yes")
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
                    # print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color(f'Start to send file: ','green')+f'{data[0]}')
                    self.transmit(cli,data[1],f'file - {data[0]}',thsnum)
                else:
                    print(uop(thsnum,color(f'Start to send string: ','green')+f"{data}"))
                    # print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color(f'Start to send string: ','green')+f"{data}")
                    self.transmit(cli,data.encode(),'str',thsnum)
                break
            time.sleep(0.1)


    def transmit(self,cli,data,dtype,thsnum):
        cli.send(dtype.encode())
        cli.recv(512)
        print(uop(thsnum,color('Head transfer success','green')))
        # print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color('Head transfer success','green'))
        # print(data)
        cli.sendall(data)
        cli.close()
        print(uop(thsnum,color('Body transfer success, exiting...','green')))
        # print(f'{thsnum}'+'   '+f'[{gettime()}] - '+color('Body transfer success, exiting...','green'))
        # isRecieved=cli.recv(512)
        # if isRecieved=='1':
        #     print(f'Successfully transmited file {dtype.replace("file - ","")}')

if __name__=='__main__':
    host='127.0.0.1'
    port=5555
    s=mission(host=host, port=port)
    ths1=Thread(target=s.accept,args=(1,))
    ths2=Thread(target=s.accept,args=(2,))
    ths1.start()
    ths2.start()
    s.ml+=[
    ('dynv6_2.0.exe',open(r'C:\Users\moiiii\Downloads\dynv6_2.0.exe','rb').read()),
    'text1',
    ('aria2.rar',open(r'C:\Users\moiiii\Downloads\【软件小】Aria2.rar','rb').read()),
    ('856799.png',open(r'C:\Users\moiiii\Downloads\856799.png','rb').read())
    ]
    ths1.join()
    ths2.join()
                



