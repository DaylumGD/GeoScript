import sys
import ctypes
import platform

import shutil
import os

import zipfile
import zlib
import base64

ADMIN = sys.path[0].split('\\')[2]

if not sys.platform == 'win32':
    print('A Software Error Has Occured...\n', file=sys.stderr)
    print(f'Looks like your using {platform.platform().split("-")[0]} ({sys.platform}). As of now GeoScript is only available of Windows', file=sys.stderr)
    print('For more infomation read read below\n', file=sys.stderr)
    print(f"GeoScript currently only works on Windows 10 and 11, this is because as of now we have no other way of decoding the {platform.platform().split('-')[0]}'s Geometry Dash save file if you know or have an idea of how to decode it then please contact me through Discord (discord in the readme)", file=sys.stderr)
    input('\nHit enter to exit')
    exit(0)

#Initalizing
def admin_check():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
            return False
if admin_check() == False:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def install():
    #decompress
    compressed_zip = open('geoscript.src.enc.zip', 'rb').read()
    compressed_zip = base64.b64decode(compressed_zip)
    compressed_zip = zlib.decompress(compressed_zip)
    open('geoscript.src.enc.zip', 'wb').write(compressed_zip)
    zipfile.ZipFile('geoscript.src.enc.zip').extractall()
    
    os.mkdir(f'C:\\Windows\\System32\\GeoScript', 0o777)
    os.mkdir(f'C:\\Users\\{ADMIN}\\AppData\\Local\\GeoScript', 0o777)
    shutil.copytree('libraries', f'C:\\Users\\{ADMIN}\\AppData\\Local\\GeoScript\\libraries')
    
    for file in os.listdir():
        if not file in ['.vscode', 'libraries']:
            try:
                shutil.copy(file, f'C:\\Windows\\System32\\GeoScript\\{file}')
                os.remove(file)
            except:
                pass