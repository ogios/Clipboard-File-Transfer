import json
import random, tempfile, socket, signal, time, os, datetime
import sys
from threading import Thread
import win32clipboard as wp
from PIL import ImageGrab
from io import BytesIO
import FileTransfer
from Tools import *
import zip
# import click
os.system('')


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



def fileConvert(dtype,clipdata):
    global s
    match dtype:
        case wp.CF_DIB:
            bdata=BytesIO()
            data=ImageGrab.grabclipboard()
            data.save(bdata,format="PNG")
            data=bdata.getvalue()
            s.ml+=[(str(time.time())+'.png', data)]    #加入mission行列等待传输
        case wp.CF_HDROP:
            for a in clipdata:
                if os.path.isdir(a):
                    zipname=zip.compress(tmp,a)
                    if zipname==2:
                        print(uop(' ',color('File doesn\'t exsist','red')))
                    elif not zipname:
                        print(uop(' ',color('Unknow error','red')))
                    else:
                        a=zipname
                f=open(a, 'rb')
                data=f.read()
                s.ml+=[(os.path.basename(a), data)]
        case wp.CF_UNICODETEXT:
            s.ml+=[clipdata]
    


def clipget():
    data=None
    while 1:
        try:
            wp.OpenClipboard()
            break
        except:
            continue
    for i in l:
        if wp.IsClipboardFormatAvailable(i):
            data=wp.GetClipboardData(i)
            break
    wp.CloseClipboard()
    return i, data


def moniter():
    global data0
    while 1:
        if is_exit:
            break
        try:
            dtype, data=clipget()
        except Exception as e:
            print(e)
            time.sleep(0.1)
            continue
        if data==data0:
            time.sleep(0.1)
            continue
        else:
            if dtype==wp.CF_DIB:
                print(f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - ScreenShot')
            else:
                print(f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - {data}')
            data0=data
            fileConvert(dtype,data)
        time.sleep(0.1)


def createThreads(s, counts):
    tid=[i for i in range(1,counts+1)]
    ths=[]
    for i in tid:
        th=Thread(target=s.accept,args=(i,))
        th.daemon=True
        th.start()
        ths+=[th]
    

def _exit(signum, frame):
    global is_exit
    is_exit=1
    print(uop(' ',color('Recieved keyinterrupt, exiting','red')))
    print(uop(' ',color('Shutting down threads','red')))

def main():
    global args
    global data0
    global s
    global l
    global tmp
    global is_exit
    args=sys.argv
    data0=None
    is_exit=0
    l=[wp.CF_DIB, wp.CF_HDROP, wp.CF_UNICODETEXT]
    ser=json.loads(open('server.json','r').read())

    host=getarg('-h', default=ser["host"])
    port=int(getarg('-p', default=ser['port']))
    ser['host']=host; ser['port']=port
    open('server.json','w').write(json.dumps(ser))

    so=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.connect(("192.168.0.0", 48946))
    lan=so.getsockname()[0]
    print(color(f'LAN_HOST - ','green')+f'{lan}')
    print(uop(' ',color(f'LISTENING AT {host}:{port}','green')))
    tmp=tempfile.mkdtemp(prefix='tmp',dir='./Temp/')
    signal.signal(signal.SIGINT,_exit)
    signal.signal(signal.SIGTERM,_exit)


    s=FileTransfer.mission(host=host,port=port)
    ths=createThreads(s,1)
    moniter()



if __name__=='__main__':
    main()