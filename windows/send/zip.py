import tempfile
import os
from Tools import ok, fatal

def _compress(name,path):
    res=os.popen(f'7z.exe a {name} {path}')
    if 'Everything is Ok' in res.read():
        return 1
    else:
        return 0


def compress(tmp,dirpath):
    if os.path.exists(dirpath):
        if os.path.isdir(dirpath):
            name=tmp+'\\'+os.path.basename(dirpath)+'.zip'
            try:
                res=_compress(name,dirpath)
                if res:
                    return name
                else:
                    return 0
            except:
                return 0
        else:
            return 2
    else:
        return 2

if __name__=='__main__':
    _dir=r'C:\Users\moiiii\Desktop\test'
    tmp=tempfile.mkdtemp(prefix='tmp',dir='./Temp/')
    print(tmp)
