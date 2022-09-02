import random, tempfile
import signal
from threading import Thread
import time, os, datetime, concurrent.futures as futures
import win32clipboard as wp
from PIL import ImageGrab
from io import BytesIO
import clipTransfer
from Tools import *
import zip
os.system('')



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
            # for a in wp.GetClipboardData(i):
            for a in clipdata:
                if os.path.isdir(a):
                    zipname=zip.compress(tmp,a)
                    if zipname==2:
                        print(uop(' ',color('File doesn\'t exsist','red')))
                        # print(fatal,f'[{gettime()}] - File doesn\'t exsist')
                    elif not zipname:
                        print(uop(' ',color('Unknow error','red')))
                        # print(fatal,f'[{gettime()}] - Unknow error')
                    else:
                        a=zipname
                with open(a, 'rb') as f:
                    data=f.read()
                    s.ml+=[(os.path.basename(a), data)]
        case wp.CF_UNICODETEXT:
            # data=wp.GetClipboardData(i)
            s.ml+=[clipdata]
    


def clipget():
    while 1:
        try:
            wp.OpenClipboard()
            break
        except:
            continue
    # wp.OpenClipboard()
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
        # if data0==None:
        #     dtype, data0=clipget()
        # else:
        #     dtype, data=clipget()
        #     if data==data0:
        #         time.sleep(0.1)
        #         continue
        #     else:
        #         if dtype==wp.CF_DIB:
        #             print(f'{color("✂","red")} {color("["+gettime()+"]","green")} - ScreenShot')
        #         else:
        #             print(f'{color("✂","red")} {color("["+gettime()+"]","green")} - {data}')
        #         data0=data
        #         fileConvert(dtype,data)
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
                print(f'{color("✂","red")} {color("["+gettime()+"]","green")} - ScreenShot')
            else:
                print(f'{color("✂","red")} {color("["+gettime()+"]","green")} - {data}')
            data0=data
            fileConvert(dtype,data)
        time.sleep(0.1)


def createThreads(s, counts):
    tid=[i for i in range(1,counts+1)]
    ths=[]
    for i in tid:
        th=Thread(target=s.accept,args=(i,))
        # th.setDaemon(True)
        th.daemon=True
        th.start()
        ths+=[th]
    

def _exit(signum, frame):
    global is_exit
    is_exit=1
    print(uop(' ',color('Recieved keyinterrupt, exiting','red')))
    print(uop(' ',color('Shutting down threads','red')))

def main():

    global data0
    global s
    global l
    global tmp
    global is_exit
    data0=None
    is_exit=0
    l=[wp.CF_DIB, wp.CF_HDROP, wp.CF_UNICODETEXT]
    host='0.0.0.0'
    port=5566
    tmp=tempfile.mkdtemp(prefix='tmp',dir='./Temp/')
    signal.signal(signal.SIGINT,_exit)
    signal.signal(signal.SIGTERM,_exit)


    s=clipTransfer.mission(host=host,port=port)
    ths=createThreads(s,2)
    moniter()



if __name__=='__main__':
    main()