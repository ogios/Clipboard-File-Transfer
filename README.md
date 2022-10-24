# clipboardFileTransfer

源代码:
```shell
git clone https://github.com/ogios/clipboardFileTransfer.git --depth=1
```

下载:  
* [安卓端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/CBFT.apk)  
* [win接受端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/client_exe.zip)   
* [win发送端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/server_exe.zip)  
* [linux端](https://github.com/ogios/clipboardFileTransfer/releases/download/v2.2/linux.zip)  

## Examples

> 截图传输:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%88%AA%E5%9B%BE.gif?raw=true)

> File transfer:

![fileTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E4%BB%B6.gif?raw=true)

> String transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E5%AD%97.gif?raw=true)

## Linux
linux端需安装xclip
```shell
sudo apt install xclip
```
例如在Ubuntu中截图或在文件管理器中复制了文件等都会被记录，连接后会被传输。  
复制文件夹时会调用7zz压缩再传输，记得及时清理Temp文件夹中的缓存.
> 7zz文件夹中备有32位可执行文件，如果误删可以去7zip官网重新下载  

接受端运行:
```shell
python3 ./recv/test_client.py [-h hostIP] [-p Port]
```

发送端运行:
> 发送端默认host和port为 `0.0.0.0:5566` 
```shell
python3 ./send/examlinux.py [-h hostIP] [-p Port]
```

使用过-h和-p后都会被记录下来，下次使用时无需再次输入。  
可以将这些放在.bashrc等终端的个性化设置里方便直接使用。
例如：
```shell
$ vim ~/.zshrc
## 加载最下面
alias send='cd /home/moiiii/tools/clipboardFileTransfer/linux/send && /home/moiiii/app/python/bin/python3 ./examlinux.py'
alias recv='cd /home/moiiii/tools/clipboardFileTransfer/linux/recv && /home/moiiii/app/python/bin/python3 ./test_client.py'
```

## Windows
### Packages
|PC_server|
|--|
|Pywin32|
|Pillow|
```shell
pip install pywin32 pillow
```

### server
```python
./send/exam.exe [-h hostIP] [-p Port]
```
### client
```python
./recv/test_client.exe [-h hostIP] [-p Port]
```

接受端用传输文件的小工具(./recv/ftm.py):
```python
python ftm.py [-h <host>] [-p <port>] [-f <file_path1 file_path2>] [-char <String1 String2>]
```
### 传输配置说明
**IP_Address** 和 **Port** 的配置被保存在`server.json` he `client.json`文件中  
在使用-h或-p后会把配置保存，下次在同一个网络环境中可以不用再配置-h和-p


## App
按 `IP OPTION` 配置连接的ip，之后只需发送发送文件就可以接收了。  
在 `Send` 页面可以发送文件。  
在MSG输入框内输入文字再点击 `GETSTR` 保存文本，点击 `GETFILE` 获取文件流接入口  
最后点击 `SEND` 发送  
tutorial: https://www.bilibili.com/video/BV1wG411E7Gc
