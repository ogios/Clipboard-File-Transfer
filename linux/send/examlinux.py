import json
import random
import re
import tempfile
import socket
import signal
import time
import os
import datetime
import sys
from threading import Thread
import pyperclip
import subprocess
import traceback

# import win32clipboard as wp
# from PIL import ImageGrab
from io import BytesIO
import FileTransfer
from Tools import *
import zip
# import click
os.system('')
global tmp
tmp = tempfile.mkdtemp(prefix='tmp', dir='./Temp/')


CMD_XCLIP = {
    "check": "xclip - selection clipboard - t TARGETS - o",
    "has_jpg": "xclip -selection clipboard -t TARGETS -o | grep image/jpeg",  # .split()
    "has_png": "xclip -selection clipboard -t TARGETS -o | grep image/png",
    "is_file": "xclip -selection clipboard -t TARGETS -o | grep copied-files",
    "has_txt": "xclip -selection clipboard -t TARGETS -o | grep text/plain;charset=utf-8",
    "save_jpg": "xclip -selection clipboard -t image/jpeg -o",
    "save_png": "xclip -selection clipboard -t image/png -o",
    "get_txt": "xclip -selection clipboard -t text/plain -o",
}


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


def run_shell(cmd):
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    return proc.stdout


# def fileConvert(dtype, clipdata):
#     global s
#     match dtype:
#         case wp.CF_DIB:
#             bdata = BytesIO()
#             data = ImageGrab.grabclipboard()
#             data.save(bdata, format="PNG")
#             data = bdata.getvalue()
#             s.ml += [(str(time.time())+'.png', data)]  # 加入mission行列等待传输
#         case wp.CF_HDROP:
#             for a in clipdata:
#                 if os.path.isdir(a):
#                     zipname = zip.compress(tmp, a)
#                     if zipname == 2:
#                         print(uop(' ', color('File doesn\'t exsist', 'red')))
#                     elif not zipname:
#                         print(uop(' ', color('Unknow error', 'red')))
#                     else:
#                         a = zipname
#                 f = open(a, 'rb')
#                 data = f.read()
#                 s.ml += [(os.path.basename(a), data)]
#         case wp.CF_UNICODETEXT:
#             s.ml += [clipdata]


# def clipget():
#     data = None
#     while 1:
#         try:
#             wp.OpenClipboard()
#             break
#         except:
#             continue
#     for i in l:
#         if wp.IsClipboardFormatAvailable(i):
#             data = wp.GetClipboardData(i)
#             break
#     wp.CloseClipboard()
#     return i, data


def dataCompare(tmpdata):
    global old_data
    if tmpdata == old_data:
        return 0
    else:
        old_data = tmpdata
        return 1


def getdata(tmpdata):
    # 二进制数据在内存中无法用字符串读出
    if tmpdata == "":

        # png格式图片
        if run_shell(CMD_XCLIP["has_png"]):
            tmpdata = run_shell(CMD_XCLIP["save_png"])
            if dataCompare(tmpdata):
                print(
                    f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - ScreenShot')
                return (str(time.time())+".png", tmpdata)

        # jpg格式图片
        elif run_shell(CMD_XCLIP["has_jpg"]):
            tmpdata = run_shell(CMD_XCLIP["save_jpg"])
            print(tmpdata)
            if dataCompare(tmpdata):
                print(
                    f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - ScreenShot')
                return (str(time.time())+".jpg", tmpdata)

        # 未知
        else:
            # print("未知类:")
            # print(run_shell(CMD_XCLIP["check"]))
            return None

    # 提取出字符串内容
    else:
        if dataCompare(tmpdata):

            # 文件夹/文件
            if run_shell(CMD_XCLIP["is_file"]):
                pathes = tmpdata.split("\n")
                files = []
                for i in pathes:
                    if os.path.isdir(i):
                        zipname = zip.compress(tmp, i)
                        if zipname == 2:
                            print(uop(' ', color('File doesn\'t exsist', 'red')))
                            return
                        elif not zipname:
                            print(uop(' ', color('Unknow error', 'red')))
                            return
                        else:
                            print(zipname)
                            i = zipname
                    name = os.path.basename(i)
                    print(
                        f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - File [ {name} ]')
                    files += [(name, open(i, "rb"))]
                return tuple(files)

            # 字符串
            else:
                print(
                    f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - String [ {tmpdata} ]')
                return tmpdata


def moniter():
    global old_data
    # while 1:
    #     if is_exit:
    #         break
    #     try:
    #         dtype, data = clipget()
    #     except Exception as e:
    #         print(e)
    #         time.sleep(0.1)
    #         continue
    #     if data == old_data:
    #         time.sleep(0.1)
    #         continue
    #     else:
    #         if dtype == wp.CF_DIB:
    #             print(
    #                 f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - ScreenShot')
    #         else:
    #             print(
    #                 f'{color("✂  ","red")} {color("["+gettime()+"]","green")} - {data}')
    #         old_data = data
    #         fileConvert(dtype, data)
    #     time.sleep(0.1)
    while 1:
        if is_exit:
            break
        # data = pyperclip.paste()
        # print(res)
        data = getdata(pyperclip.paste())
        if data:
            if isinstance(data[0], tuple):
                for i in data:
                    s.ml += [i]
            else:
                s.ml += [data]
        time.sleep(0.1)


def createThreads(s, counts):
    tid = [i for i in range(1, counts+1)]
    global ths
    ths = []
    for i in tid:
        th = Thread(target=s.accept, args=(i,))
        th.daemon = True
        th.start()
        ths += [th]


def _exit(signum, frame):
    global is_exit
    is_exit = 1
    s.exit = True
    print(uop(' ', color('Recieved keyinterrupt, exiting', 'red')))
    print(uop(' ', color('Shutting down threads', 'red')))


def main():

    global args
    global old_data
    global s
    # global l
    global is_exit
    args = sys.argv
    data = None
    old_data = None
    is_exit = 0
    # l = [wp.CF_DIB, wp.CF_HDROP, wp.CF_UNICODETEXT]
    f = open('server.json', 'a+')
    f.seek(0)
    try:
        ser = json.loads(f.read())
        host = getarg('-h', default=ser["host"])
        print(host)
        port = int(getarg('-p', default=ser['port']))
        ser['host'] = host
        ser['port'] = port
        f.close()
        open('server.json', 'w').write(json.dumps(ser))

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
            # host = input(color("No host provided\n>>>", "green"))
            host = "0.0.0.0"
        while not port:
            port = input(color("No port provided\n>>>", "green"))
        ser['host'] = host
        ser['port'] = port
        open('server.json', 'w').write(json.dumps(ser))
    # ser=json.loads(open('server.json','r').read())

    # host=getarg('-h', default=ser["host"])
    # port=int(getarg('-p', default=ser['port']))
    # ser['host']=host; ser['port']=port
    # open('server.json','w').write(json.dumps(ser))

    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.connect(("192.168.0.0", 48946))
    lan = so.getsockname()[0]
    print(color(f'LAN_HOST - ', 'green')+f'{lan}')
    print(uop(' ', color(f'LISTENING AT {host}:{port}', 'green')))

    signal.signal(signal.SIGINT, _exit)
    signal.signal(signal.SIGTERM, _exit)

    s = FileTransfer.mission(host=host, port=port)
    ths = createThreads(s, 1)
    moniter()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print(traceback.print_exc())
        input(color("Press any button to exit", "red"))
