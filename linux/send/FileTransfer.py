import datetime
import random
import time
import os
from Tools import *
import socket
os.system('')


class mission:
    def __init__(self, host=None, port=None, thsnum=2) -> None:
        self.ml = []
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(thsnum)
        self.server = None

    def accept(self, thsnum):
        while 1:
            if not self.ml:
                time.sleep(0.5)
                continue
            print(uop(thsnum, color("Ready for connection", 'green')))
            self.transmission(thsnum)

            print(uop(thsnum, color("Close connection", 'green')))
            time.sleep(0.1)

    def transmission(self, thsnum):
        data = None
        res = 1
        while self.ml:
            try:
                data = self.ml[0]
                del self.ml[0]
                break
            except Exception as e:
                time.sleep(0.1)
        while 1:
            cli, ipaddr = self.socket.accept()
            print(
                uop(thsnum, f'{ipaddr[0]}:{ipaddr[1]} '+color('Connected', 'green')))
            if isinstance(data, tuple):
                if res:
                    print(
                        uop(thsnum, color(f'Start to send file: ', 'green')+f'{data[0]}'))
                res = self.transmit(cli, data[1], f'file - {data[0]}', thsnum)
                if res:
                    break
            else:
                if res:
                    print(
                        uop(thsnum, color(f'Start to send string: ', 'green')+f"{data}"))
                res = self.transmit(cli, data.encode(), 'str', thsnum)
                if res:
                    break
            time.sleep(0.1)
        print(f"{ipaddr}closed")

    def transmit(self, cli, data, dtype, thsnum):
        cli.send(dtype.encode())
        res = cli.recv(512).decode()
        if str(res) != "1":
            cli.close()
            print(
                uop(thsnum, color("Zombie connection, quit and wait for new connection", "red")))
            return 0
        print(uop(thsnum, color('Head transfer success', 'green')))
        if isinstance(data, bytes):
            cli.sendall(data)
        else:
            while 1:
                t = data.read(1024)
                if not t:
                    break
                cli.send(t)
        cli.close()
        print(uop(thsnum, color('Body transfer success, exiting...', 'green')))
        return 1


# @click.command()
# @click.option('-h',default='192.168.0.104',help="host",)
# @click.option('-p', default=5566, help='port')
# @click.option('-f',default='')
# @click.option('-char',default='')
# def main(h,p,f,char):
#     global host
#     global port
#     host=h
#     port=p
#     s=mission(host=host, port=port)
#     ths1=Thread(target=s.accept,args=(1,))
#     ths2=Thread(target=s.accept,args=(2,))
#     ths1.start()
#     ths2.start()
#     if os.path.exists(f):
#         name=os.path.basename(f)
#         s.ml+=[(name,open(f,'rb').read())]
#     if char:
#         s.ml+=[char]
#     print(s.ml)
#     ths1=Thread(target=s.accept,args=(1,))
#     # ths2=Thread(target=s.accept,args=(2,))
#     ths1.start()
#     # ths2.start()
#     ths1.join()


# if __name__=='__main__':
#     main()
