import compiler
import shutil
import settings as gs_settings
from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu()

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