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

|exam.py|
|--|
|Pillow|
|pywin32|

if not installed, run:
```python
pip install <package>
```

### Server
> exam.py requires python3.10  

Open ```exam.py``` to start monitor the clipboard and wait for connection.    
```python
python exam.py
```    
When copying directories, `exam.py` will generate zip file in Temp folder using `7z.exe` and then send it to socket client.  
Use `cleanTemp.py` to clean Temp or delete it manually.  
ScreenShots won't be created in Temp but are sended directly to the client using `\<timestamp\>.png` as it's name.  

### client
open ```test_client.py``` to connect and recieve string or file.  
```python
python test_client.py
```  
The file recieved are in recv folder, zip files won't be automaticly unziped.  
Strings that are recieved will be shown in Shell with ">>>" in the front.  

## Configuration
### server-exam.py
change host, port or thread-counts in main()
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

