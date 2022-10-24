# clipboardFileTransfer

源代码:
```shell
git clone https://github.com/ogios/clipboardFileTransfer.git --depth=1
```

下载:  
<a href="https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/CBFT.apk" target="_blank">
安卓端</a>  
<a href="https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/client_exe.zip" target="_blank">
win接受端</a>  
<a href="https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/server_exe.zip" target="_blank">
win发送端</a>  
<a href="https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/linux.zip" target="_blank">
linux端</a>  
#[安卓端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/CBFT.apk)  
#[win接受端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/client_exe.zip)   
#[win发送端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/server_exe.zip)  
#[linux端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/linux.zip)  

## Examples

> 截图传输:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%88%AA%E5%9B%BE.gif?raw=true)

> File transfer:

![fileTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E4%BB%B6.gif?raw=true)

> String transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E5%AD%97.gif?raw=true)


## Packages
> no need for client to install any site-packages

|PC_server|
|--|
|Pywin32|
|Pillow|

## RUN
### Win_server
Start server(./server_exe/origin_code/):
```python
python exam.py [-h <host>] [-p <port>]
```
> Or just run ./server_exe/exam.exe  

### client
Revieve(./client_exe/origin_code/):
```python
python test_client.py [-h <host>] [-p <port>]
```
> Or just run ./client_exe/test_client.exe  

FileTransfer(./client_exe/origin_code/):
```python
python ftm.py [-h <host>] [-p <port>] [-f <file_path1 file_path2>] [-char <String1 String2>]
```
### Configuration
**IP_Address** and **Port** are both saved in two json_files: `server.json` and `client.json`  
no -h or -p when running script means using default option in the json_file  
once using -h or -p means to update options in these two files  

## App
tutorial: https://www.bilibili.com/video/BV1wG411E7Gc
