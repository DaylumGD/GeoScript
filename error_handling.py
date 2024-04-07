import sys
from consolemenu import ConsoleMenu
consolemenu = ConsoleMenu()

warnings = []

class GSError:
    def __init__(self, *args, errtype=str, codeline):
        consolemenu.clear_screen()
        print(f'There has been an error compiling at line {codeline[0]}\n')
        print(codeline[1])
        print(f'[{errtype}]')
        print(''.join(args), file=sys.stderr)
        input('\nhit enter to exit compiler')
        sys.exit()

class GSWarnings:
    def __init__(self, *args):
        global warnings
        print('\n[Compiler Warning]')
        print(''.join(args))
        print('')
        
        warnings.insert(0, ''.join(args))