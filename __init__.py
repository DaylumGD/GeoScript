import compiler
import shutil
import settings as gs_settings
from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu()

import os

def build(file, level):
    compiler.compilegs(file, level)

def settings():
    print('Welcome to GeoScript settings\n')
    print('1. Change data location')
    print('2. Change GD location')
    cmd = int(input('Choose (1, 2): '))
    
    if cmd == 1:
        ns = input('New Data location: ')
        shutil.move(gs_settings.appdata_location, ns)

def uninstall():
    print('Found GeoScript files C:\\Windows\\System32\\GeoScript (geoscript main program directory)')
    print(f'Found GeoScript files C:\\Users\\{gs_settings.ADMIN}\\AppData\\Local\\GeoScript (geoscript main library directory)')
    print('\nAre you shure you want to uninstall')
    if input('Y or N: ').lower() == 'y':
        for folder in ['C:\\Windows\\System32\\GeoScript', f'C:\\Users\\{gs_settings.ADMIN}\\AppData\\Local\\GeoScript']:
            for file in os.listdir(folder):
                os.remove(f'{folder}{file}')
            os.removedirs(folder)
        os.remove('C:\\Windows\\System32\\geoscript.bat')

def documents():
    print('GeoScript documentation\n')
    print('1. readme')
    print('2. License')
    print('3. changelog')
    print('4. quick fixes')
    print('5. editing guide')
    cmd = int(input('Choose (1, 2, 3, 4, 5): '))
    consolemenu.clear_screen()
    
    if cmd == 1:
        print(open('readme.rst').read())
    elif cmd == 2:
        print(open('license.txt').read())
    elif cmd == 3:
        print(open('changelog.md').read())
    elif cmd == 4:
        print(open('quick_fixes.md').read())
    elif cmd == 5:
        print(open('editing_guide.md').read())
    input('\nHit enter to finish')

def main():
    print('Welcome to GeoScript\n')
    print('1. Compile GeoScript file')
    print('2. GeoScript settings')
    print('3. Documentation')
    cmd = int(input('Choose (1, 2, 3): '))
    
    if cmd == 1:
        level = input('Name of the level: ')
        file = input('File directory: ')
        consolemenu.clear_screen()
        build(file, level)
    elif cmd == 2:
        consolemenu.clear_screen()
        settings()
    elif cmd == 3:
        consolemenu.clear_screen()
        documents()