import json
import sys
import keyboard

#main root directory
main_root_dir = sys.path[0]
'Main path of GeoScript eg: C:/Users/ADMIN/Downloads/GeoScript/GeoScript'
main_root_dir = main_root_dir.split('\\')
main_root_dir.pop()
main_root_dir.pop()
main_root_dir = '\\'.join(main_root_dir)

ADMIN = sys.path[0].split('\\')[2]
'This is the user of the device eg: C:/Users/ADMIN'

def build_json(main_binary, data_loc, main_loc, gdbin, gddata, sf):
    'Builds "hooking.json" for the installtion'
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
    with open(f'{main_root_dir}\\hooking.json', 'w') as file:
        json.dump(build, file)
        
def auto_input(string=str):
    'Makes the user automaticly type what ever you put in as an argument'
    charmap: list[str] = [i for i in string]
    for char in charmap:
        if not char.isupper() == True:
            keyboard.press(char)
        else:
            keyboard.press(f'shift+{char}')