import tempfile
import os
from Tools import ok, fatal
if os.name == "posix":
    IS_LINUX = True
else:
    IS_LINUX = False


def _compress(name, path):

    if IS_LINUX:
        res = os.popen(f"./7zz a -r {name} {path}").read()
    else:
        res = os.popen(f'7z.exe a {name} {path}').read()
    if 'Everything is Ok' in res:
        return 1
    else:
        print(res)
        return 0


def compress(tmp, dirpath):
    if os.path.exists(dirpath):
        if os.path.isdir(dirpath):
            name = tmp+'/'+os.path.basename(dirpath)+'.zip'
            try:
                res = _compress(name, dirpath)
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


if __name__ == '__main__':
    _dir = r'C:\Users\moiiii\Desktop\test'
    tmp = tempfile.mkdtemp(prefix='tmp', dir='./Temp/')
    print(tmp)
