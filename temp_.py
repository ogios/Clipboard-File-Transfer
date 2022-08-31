import tempfile
# path=tempfile.gettempdir()
path=tempfile.mkdtemp(prefix='tmp',dir='./Temp/')
print(path)