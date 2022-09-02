# clipboardFileTransfer
## Examples

> Screenshot transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%88%AA%E5%9B%BE.gif?raw=true)

> File transfer:

![fileTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E4%BB%B6.gif?raw=true)

> String transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E5%AD%97.gif?raw=true)


## Usage
A script that allows you to transfer string or file/folder automaticly when copying things.   
当复制文件/文件夹或字段甚至截图时自动传输到另一端，不必登录微信或qq
### Packages
> to run `test_client.py`, you don't need to install any site-packages  
> 使用客户端`test_client.py`无需安装任何python包

|exam.py|
|--|
|Pillow|
|pywin32|

if not installed, run:  
如果上述包未安装则运行：
```python
pip install <package>
```

### Server
> exam.py requires python3.10  
> exam.py 需要在python3.10环境下运行

Open ```exam.py``` to start monitor the clipboard and wait for connection.    
运行```exam.py```以监控剪切板同时等待客户端连接
```python
python exam.py
```    
When copying directories, `exam.py` will generate zip file in Temp folder using `7z.exe` and then send it to socket client.  
Use `cleanTemp.py` to clean Temp or delete it manually.  
ScreenShots won't be created in Temp but are sended directly to the client using `\<timestamp\>.png` as it's name.  

复制文件夹时`exam.py`会使用`7z.exe`生成压缩文件再向客户端发送  
使用`cleanTemp.py`清空Temp临时文件夹，或者也可以手动删除Temp文件夹清除缓存  
截图在内存中生成的二进制文件不会在服务端临时文件夹生成再发送，而是转码为`.png`格式字节直接向客户端发送以时间戳命名的图片  

### client
open ```test_client.py``` to connect and recieve string or file.  
打开```test_client.py```连接并接收字符串或文件  
```python
python test_client.py
```  
The file recieved are in recv folder, zip files won't be automaticly unziped.  
Strings that are recieved will be shown in Shell with ">>>" in the front.  

被接收的文件会保存在recv文件夹，压缩文件不会被自动解压  
接收到的字符串会在命令行中输出显示，字符串前附带">>>"表明字符串输出的位置  


## Configuration
### server-exam.py
change host, port or thread-counts in main()  
在main()函数中更改地址，端口和线程数  
```python
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
```

### client-test_client.py
line 110-114:
```python
host='192.168.0.104'
port=5566

is_exit=0
thcounts=2
```

