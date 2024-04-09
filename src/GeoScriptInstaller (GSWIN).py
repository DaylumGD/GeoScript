import sys
import ctypes
import platform

import shutil
import os
import tkinter

import zipfile
import zlib
import base64
import json

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
    
def build_json(main_binary, data_loc, main_loc, gdbin, gddata, sf):
    build = {
        "main_app_loc": main_loc,
        "appdata_loc": data_loc,
        
        "binaries": {
            "main": main_binary,
            "geometry_dash": gdbin
        },
        
        "gddata_dir": gddata,
        "cclocallevels": sf
    }
    with open('hooking.json', 'w') as file:
        json.dump(build, file)

def install():
    #decompress
    compressed_zip = open('geoscript.src.enc.zip', 'rb').read()
    compressed_zip = base64.b64decode(compressed_zip)
    compressed_zip = zlib.decompress(compressed_zip)
    open('geoscript.src.enc.zip', 'wb').write(compressed_zip)
    zipfile.ZipFile('geoscript.src.enc.zip').extractall()
    
    build_json('geoscript.bat', gsap.get(), gsmp.get(), 'C:\\Program Files x86\\Steam\\steamapps\\common\\GeometryDash', gdsfp.get(), 'CCLocalLevels.dat')
    
    os.mkdir(gsmp.get(), 0o777)
    os.mkdir(gsap.get(), 0o777)
    shutil.copytree('libraries', f'{gsap.get()}\\libraries')
    
    for file in os.listdir():
        if not file in ['.vscode', 'libraries', 'src']:
            try:
                if file == 'geoscript.bat':
                    shutil.copyfile('geoscript.bat', 'C:\\Windows\\System32\\geoscript.bat')
                shutil.copy(file, f'C:\\Windows\\System32\\GeoScript\\{file}')
                os.remove(file)
            except:
                window.destroy()
                print('There was an error installing GeoScript')
                print(f'Failed to copy file {file}')

#window
window = tkinter.Tk()
window.title('Installer')
window.geometry('300x400')

tkinter.Label(window, text='GeoScript Installer', font=1).place(anchor='center', relx=0.5, rely=0.1)

tkinter.Label(window, text='Geometry Dash savefile path').place(anchor='center', relx=0.5, rely=0.3)
gdsfp = tkinter.Entry(window, width=40); gdsfp.place(anchor='center', relx=0.5, rely=0.35)
tkinter.Label(window, text='GeoScript main path').place(anchor='center', relx=0.5, rely=0.4)
gsmp = tkinter.Entry(window, width=40); gsmp.place(anchor='center', relx=0.5, rely=0.45)
tkinter.Label(window, text='GeoScript libraries path path').place(anchor='center', relx=0.5, rely=0.5)
gsap = tkinter.Entry(window, width=40); gsap.place(anchor='center', relx=0.5, rely=0.55)

gdsfp.insert(0, f'C:\\Users\\{ADMIN}\\AppData\\Local\\Geometry Dash')
gsmp.insert(0, 'C:\\Windows\\System32\\GeoScript')
gsap.insert(0, f'C:\\Users\\{ADMIN}\\AppData\\Local\\GeoScript')

tkinter.Label(window, text='By installing you accept the licesnse (./lisence.txt)').place(anchor='center', relx=0.5, rely=0.7)
tkinter.Button(window, text='Install', font=1, width=20, command=install).place(anchor='center', relx=0.5, rely=0.8)

window.mainloop()
