import os
import base64
def RenameFile(filename):
    f1 = os.path.basename(filename)
    filename_bytes = f1.encode('utf-8')
    filename_bytes_base64 = base64.encodestring(filename_bytes)    
    filename_bytes_base64 = filename_bytes_base64[::-1][1:]   # 倒序
    new_filename = filename_bytes_base64.decode('utf-8') + '.我的鎖頭很厲害你不要想打開他'
    os.rename(filename, os.path.join(os.path.dirname(filename),new_filename))


def ReserveFilename(filename):
    f = os.path.basename(filename)
    f = f[::-1][7:][::-1]
    filename_base64 = f[::-1] + '\n'
    filename_bytes_base64 = filename_base64.encode('utf-8')
    ori_filename = base64.decodestring(filename_bytes_base64).decode('utf-8')
    os.rename(filename, os.path.join(os.path.dirname(filename), ori_filename))