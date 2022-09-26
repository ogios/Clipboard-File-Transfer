# import win32clipboard as wp
# wp.OpenClipboard()
# # a=wp.GetClipboardFormatName(0)
# a=wp.GetGlobalMemory(wp)

# print(a)
import time
from PIL import ImageGrab, Image
from io import BytesIO
p1=time.time()
a=ImageGrab.grabclipboard()
print(a)
b=BytesIO()
a.save(b,format='PNG')
a.show()
print(time.time()-p1)
# with open('shit.png', 'wb') as f:
#     f.write(b.getvalue())
# print(b.getvalue())