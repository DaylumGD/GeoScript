from base64 import b64decode, b64encode
from zlib import  decompress, MAX_WBITS, compress

class Decrypt:
    def Xor(path, key):
        fr = open(path,'rb')
        data = fr.read()
        fr.close()
        res = []
        for i in data: res.append(i^key)
        return bytearray(res).decode()
 
    def Decrypt(data):
        return decompress(b64decode(data.replace('-','+').replace('_','/').encode())[10:],-MAX_WBITS)

def DecryptCCLL(filedir):
    res = Decrypt.Xor(filedir, 11)
    fin = Decrypt.Decrypt(res)
    with open(filedir,'wb') as fw:
        fw.write(fin)

def DecryptLvl(lvlstr=str):
    return decompress(b64decode(lvlstr.replace('-', '+').replace('_', '/').encode())[10:], -MAX_WBITS).decode()

def EncryptLvl(lvlstr=str):
    return compress(b64encode(lvlstr.replace('+', '-').replace('/', '_'))[-10:], -MAX_WBITS)

def DecryptStr(string):
    return decompress(string[10:], -MAX_WBITS).decode()

def EncryptStr(string):
    return compress(string[-10:], -MAX_WBITS)