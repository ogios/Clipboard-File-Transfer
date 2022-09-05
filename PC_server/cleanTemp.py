import os, shutil, time
from Tools import ok,fatal
os.system('')
# os.removedirs('./Temp/')
try:
    shutil.rmtree('./Temp')
    os.mkdir('./Temp')
    print(ok,'Remove Temp successfully')
except Exception as e:
    print(fatal,e)
for i in range(3,0,-1):
    print(f'\rExit in {i}s',end='')
    time.sleep(1)
print(f'\rExit in 0s',end='')