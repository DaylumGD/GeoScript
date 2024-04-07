import shutil
import decoder

import settings

def force_stop():
    shutil.move('backup.dat', f'{settings.gddataloc}\\CCLocalLevels.dat')
    exit()

def savefile_test():
    try:
        decoder.DecryptCCLL('compiling/insert.dat')
        return True
    except:
        return False