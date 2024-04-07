import json
import sys

#opens file in a wierd way
jsonfile = open('hooking.json')
jsonbuild: dict = json.load(jsonfile)
jsonfile.close()

class binaries:
    main = jsonbuild.get('binaries').get('main')

main_location = jsonbuild.get('main_app_loc')
appdata_location = jsonbuild.get('appdata_loc')

gddataloc = jsonbuild.get('gddata_dir')
savefile = jsonbuild.get('cclocallevels')

rootdir = None

ADMIN = sys.path[0].split('\\')[2]

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