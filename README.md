# clipboardFileTransfer
## Examples

> Screenshot transfer:

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
### PC_server
Start server:
```python
python exam.py [-h <host>] [-p <port>]
```
Recieve:
```python
python test_client.py [-h <host>] [-p <port>]
```

### client
Revieve:
```python
python test_client.py [-h <host>] [-p <port>]
```
Transfer:
```python
python ftm.py [-h <host>] [-p <port>] [-f <file_path1 file_path2>] [-char <String1 String2>]
```
### Configuration
ip_address and port are both saved in two json_files: `server.json` and `client.json`
no -h or -p when running script means using default option in the json_file
once using -h or -p means to update options in these two files
