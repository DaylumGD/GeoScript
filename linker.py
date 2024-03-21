import decoder

def optimise_level_string(lvlstr=str):
    contents = lvlstr.split('1,')
    cache = []
    
    for item in enumerate(contents):
        item = f'1,{item}'
        if not item[1] in cache:
            cache.insert(0, item[1])
        else:
            contents.pop(item[0])
    contents = '1,'.join(contents)
    return contents

def linktosf(lvlname):
    decoder.DecryptCCLL('compiling/insert.dat')
    
    sf = open('compiling/insert.dat').read()
    
    lvlstr = sf.split(lvlname, 1)[1].removeprefix('</s><k>k4</k><s>')
    lvlstr = lvlstr.split('</')[0]
    lvlstr = decoder.DecryptLvl(lvlstr)
    
    newlvlstr = f'{lvlstr}{open("compiling/lvlstr.dat").read()}'
    newlvlstr = optimise_level_string(newlvlstr)
    newlvlstr = decoder.EncryptLvl(newlvlstr)
    
    nsf = sf.replace(lvlstr, newlvlstr, 1)
    
    open('compiling/insert.dat', 'wb').write(nsf)