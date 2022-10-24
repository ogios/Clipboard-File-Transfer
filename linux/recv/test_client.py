import os
import sys
import signal
import json
import re
import socket
import time
import datetime
from threading import Thread
os.system('')
ss = []
if os.name == "posix":
    IS_LINUX = True
else:
    IS_LINUX = False


def gettime():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


def uop(thsnum, str):
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


def getarg(arg, default=None):
    global args
    try:
        for i in args:
            if i == arg:
                data = []
                for a in args[args.index(i)+1:]:
                    if '-' in a:
                        break
                    data += [a]
                if len(data) == 1:
                    return data[0]
                else:
                    return data
        return default
    except:
        return default


def accept(thsnum):
    global ss
    while 1:
        if is_exit:
            print(uop(f'{thsnum}', color('Exiting', 'red')))
            return
        print(f"{thsnum}"+color('   ', 'red') +
              f'[{gettime()}] - '+color("ready for connection", 'green'))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((host, port))
        except Exception as e:
            if 10061 in e.args or 111 in e.args or "No route to host" in str(e) or 'timed out' in str(e):
                print(
                    uop(thsnum, color('Connection timeout, starting a new connection', 'red')))
            else:
                print('e:', e.args)
            s.close()
            time.sleep(0.5)
            continue
        print(f"{thsnum}"+color('   ', 'red') +
              f'[{gettime()}] - '+color('connected', 'green'))
        ss += [s]
        transmission(s, thsnum)
        s.close()
        del ss[ss.index(s)]
        print(f"{thsnum}"+color('   ', 'red') +
              f'[{gettime()}] - '+color("close connection", 'green'))


def transmission(s: socket, thsnum):
    global IS_LINUX

    head = None
    start = time.time()
    if IS_LINUX:
        while 1:
            if is_exit:
                return
            try:
                head = s.recv(1024).decode()
                break
            except Exception as e:
                if 10035 in e.args or "timed out" in str(e):
                    pass
                else:
                    if 10054 in e.args:
                        print(uop(thsnum, color("Connection offline", "green")))
                        return
                    else:
                        print(uop(thsnum, color(f"Unknow error - {e}", "red")))
                        print(e.with_traceback(None))
                        return
    else:
        s.setblocking(0)
        while 1:
            if is_exit:
                return
            try:
                head = s.recv(1024).decode()
            except Exception as e:
                if 10035 in e.args:
                    pass
                else:
                    if 10054 in e.args:
                        print(uop(thsnum, color("Connection offline", "green")))
                    else:
                        print(uop(thsnum, color(f"Unknow error - {e}", "red")))
                        print(e.with_traceback(None))
                    return
            if head:
                # print(head)
                s.setblocking(1)
                break
            else:
                pass
            time.sleep(0.1)
    print(thsnum, '  '+f'[{gettime()}] - ' +
          color('Get head successfully: ', 'green')+head)
    if head == 'str':
        s.send('1'.encode())
        print(thsnum, '  '+f'[{gettime()}] - ' +
              color('Recieving string...', 'green'))
        tmp = ''
        while 1:
            data = s.recv(1024)
            if not data:
                break
            tmp += data.decode()
        print(f"{thsnum}   "+f'[{gettime()}] - '+color('>>> ', 'red')+tmp)
    else:
        s.send('1'.encode())
        print(thsnum, f'  '+f'[{gettime()}] - ' +
              color(f'Recieving {head}...', 'green'))
        f = open(f'./recv/{head.replace("file - ","")}', 'wb')
        while 1:
            data = s.recv(1024)
            if not data:
                print(thsnum, '  '+f'[{gettime()}] - ' +
                      color(f'{head} successfully transmited', 'green'))
                break
            f.write(data)
        f.close()


def _exit(signum, frame):
    global is_exit
    global ss
    is_exit = 1
    print(uop(' ', color('Recieved keyinterrupt, exiting', 'red')))
    for i in ss:
        print(uop(' ', color(f'Closing socket {i}', 'red')))
        i.close()
    print(uop(' ', color('Shutting down threads', 'red')))


if __name__ == "__main__":
    try:
        global args
        args = sys.argv
        if not os.path.exists('./recv'):
            os.mkdir('./recv')
        signal.signal(signal.SIGINT, _exit)
        signal.signal(signal.SIGTERM, _exit)

        f = open('client.json', 'a+')
        f.seek(0)
        try:
            ser = json.loads(f.read())
            host = getarg('-h', default=ser["host"])
            print(host)
            port = int(getarg('-p', default=ser['port']))
            ser['host'] = host
            ser['port'] = port
            f.close()
            open('client.json', 'w').write(json.dumps(ser))

        except Exception as e:
            f.truncate()
            f.close()
            ser = {}
            host = getarg('-h')
            try:
                port = int(getarg('-p'), 5566)
            except:
                port = 5566
            while not host:
                host = input(color("No host provided\n>>>", "green"))
            while not port:
                port = input(color("No port provided\n>>>", "green"))
            ser['host'] = host
            ser['port'] = port
            open('client.json', 'w').write(json.dumps(ser))

        # ser=json.loads(open('client.json','r').read())

        # host=getarg('-h', default=ser["host"])
        # print(host)
        # port=int(getarg('-p', default=ser['port']))
        # ser['host']=host; ser['port']=port
        # open('client.json','w').write(json.dumps(ser))

        so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        so.connect(("192.168.0.0", 48946))
        lan = so.getsockname()[0]
        print(color(f'LAN_HOST - ', 'green')+f'{lan}')
        print(uop(' ', color(f'LISTENING AT {host}:{port}', 'green')))

        # host='192.168.124.1'
        # port=5566
        # host=getarg()

        is_exit = 0
        thcounts = 2
        ths = []
        for i in range(1, thcounts+1):
            th = Thread(target=accept, args=(i,))
            th.daemon = True
            ths += [th]
            th.start()

        br = 0
        while 1:
            for i in ths:
                if i.is_alive():
                    time.sleep(0.1)
                    continue
                br = 1
                break
            if br == 1:
                break
    except Exception as e:
        print(e)
        print(e.with_traceback(None))
        input(color("Press any button to exit", "red"))
