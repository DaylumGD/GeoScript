import ctypes
import sys
import platform

import os
os.system('pip install -r "requirements.txt"')

from buildsettings import ADMIN, build_json
from consolemenu import ConsoleMenu

import shutil

main_dir = 'C:\\Windows\\System32\\GeoScript'
data_dir = f'C:\\Users\\{ADMIN}\\AppData\\Local\\GeoScript'

gdbinary = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash'
gddataloc = f'C:\\Users\\{ADMIN}\\AppData\\Local\\GeometryDash'
cclocallevels = 'CCLocalLevels.dat'

#main root directory
main_root_dir = sys.path[0]
main_root_dir = main_root_dir.split('\\')
main_root_dir.pop()
main_root_dir.pop()
main_root_dir = '\\'.join(main_root_dir)

consolemenu = ConsoleMenu()

if sys.platform == 'win32':
    while True:
        consolemenu.clear_screen()
        print('Welcome to the GeoScript Installer\n')
        print('GeoScript Installation Settings,')
        print('1. Installation directories')
        print('2. Geometry Dash Directories')
        print('3. Install GeoScript')
    
        command = int(input('choose (1, 2, 3): '))
    
        if command == 1:
            consolemenu.clear_screen()
            print('All installation directories,\n')
            print(f'Main executable: {main_dir}\\__init__.py')
            print(f'Libraries and other data: {data_dir}')
        
            cmd = input('\nenter 1 to edit Main executabe, enter 2 to edit data directory, hit enter to exit: ')
            
            if cmd == '1':
                main_dir = input('New directory: ')
            elif cmd == '2':
                data_dir = input('New directory: ')
        elif command == 2:
            consolemenu.clear_screen()
            print('Geometry Dash directories,\n')
            print(f'Geometry Dash: {gdbinary}')
            print(f'GD AppData: {gddataloc}')
            print(f'Game Save File: {cclocallevels}')
        
            cmd = input('\nenter 1 to edit Geometry Dash binary, enter 2 to edit data directory, enter 3 to edit savefile name, hit enter to exit: ')
            
            if cmd == '1':
                gdbinary = input('New directory: ')
            elif cmd == '2':
                gddataloc = input('New directory: ')
            elif cmd == '3':
                cclocallevels = input('New file name: ')
        elif command == 3:
            consolemenu.clear_screen()
            print('Installing GeoScript')
            
            #permitions elivate
            def admin_check():
                try:
                    return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                    return False
            if admin_check() == False:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            
            try: os.mkdir(data_dir, 0o777)
            except: pass
            try: os.mkdir(main_dir, 0o777)
            except: pass
            build_json('geoscript.exe', data_dir, main_dir, gdbinary, gddataloc, cclocallevels)
            shutil.copytree('libraries', f'{data_dir}/libraries')
            for file in os.listdir(main_root_dir):
                if not file in ['.vscode', 'libraries']:
                    if file == 'geoscript.bat':
                        shutil.copyfile(file, r'C:/Windows/System32/geoscript.bat')
                    elif os.path.isdir(file) == True:
                        shutil.copytree(file, f'{main_dir}\\{file}')
                    else:
                        shutil.copyfile(file, f'{main_dir}\\{file}')
            print('Sucsesfuly installed GeoScript')
            input('Hit enter to exit')
            exit(1)
        
else:
    consolemenu.clear_screen()
    print('A Software Error Has Occured...\n', file=sys.stderr)
    print(f'Looks like your using {platform.platform().split("-")[0]} ({sys.platform}). As of now GeoScript is only available of Windows', file=sys.stderr)
    print('For more infomation read read below\n', file=sys.stderr)
    print(f"GeoScript currently only works on Windows 10 and 11, this is because as of now we have no other way of decoding the {platform.platform().split('-')[0]}'s Geometry Dash save file if you know or have an idea of how to decode it then please contact me through Discord (discord in the readme)", file=sys.stderr)
    input('\nHit enter to exit')
    exit(0)