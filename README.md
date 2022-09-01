# clipboardFileTransfer
## Examples

> Screenshot transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%88%AA%E5%9B%BE.gif?raw=true)

> File transfer:

![fileTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E4%BB%B6.gif?raw=true)

> String transfer:

![stringTransfer](https://github.com/ogios/clipboardFileTransfer/blob/main/gif/%E4%BC%A0%E8%BE%93%E6%96%87%E5%AD%97.gif?raw=true)


## Usage
### Server
Open ```exam.py``` to start monitor the clipboard and wait for connection.    
```python
python exam.py
```    
When copying directories, exam.py will generate zip file in Temp folder using 7z.exe and then send it to socket client.  
Use cleanTemp.py to clean Temp or delete it manually.  
ScreenShots won't be created in Temp but are sended using \<timestamp\>.png as it's name.  

### client
open ```test_client.py``` to connect and recieve string or file.  
```python
python test_client.py
```  
The file recieved are in recv folder, zip files won't be automaticly unziped.  
Strings that are recieved will be shown in Shell with ">>>" in the front.  

## Configuration
