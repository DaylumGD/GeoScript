import linker
import settings
import gs_parser
import json
import memory_modules
from error_handling import GSError, GSWarnings
import error_handling
import os
import shutil

from webbrowser import open as open_tab


objecthandling: dict[str] = json.load(open('objecthandling.json'))

#functions
compilelist = []

def compile_codeblock(codeblock=list[tuple]):
    with open('compiling/lvlstr.dat', 'a') as file:
        for block in codeblock:
            #list conversion
            block = [bit for bit in block]
            
            statement = block[0]
            
            #variable inplace
            nblock = block
            
            for brick in enumerate(block):
                brickreplace = memory_modules.heap_memory.get(brick[1])
                if not brickreplace == None:
                    nblock.pop(brick[0])
                    nblock.insert(block[0], brickreplace)
            
            #basic support
            if not statement == '@add':
                ins = objecthandling[statement].format(i for i in block)
                file.write(ins)
            elif statement == '#function':
                func_compile = []
                for i in codeblock:
                    if i[len(i)-1] == block[len(block)-1]:
                        func_compile.insert(0, i)
                compile_codeblock(func_compile)
            
            # if statement support
            elif statement in ['if statement', 'else if statement']:
                if codeblock[2] == '==':
                    if codeblock[1] == codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
                        
                elif codeblock[2] == '>':
                    if codeblock[1] > codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
                        
                elif codeblock[2] == '<':
                    if codeblock[1] < codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
                
                elif codeblock[2] == '>=':
                    if codeblock[1] >= codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
                
                elif codeblock[2] == '=<':
                    if codeblock[1] <= codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
                
                elif codeblock[2] == '!=':
                    if not codeblock[1] == codeblock[2]:
                        compile_codeblock(memory_modules.statement_backlog[codeblock[3]])
            else:
                file.write(block[1])

#MAIN compiler
def compilegs(file=str, level=str):
    fsplit = file.split('/')
    file = '\\'.join(fsplit)
    print(f'Compiling {file} and other dependencies')
    print('Initalizing...')
    
    if not file.endswith('.gss'):
        GSWarnings(f'File extension ".{file.split('.').pop()}" is not the standard GeoScript file extension (.gss)')
    
    rootdir = file.split('/')
    rootdir.pop()
    rootdir = '/'.join(rootdir)
    if rootdir == '':
        rootdir = None
    
    settings.rootdir = rootdir
    
    os.mkdir('compiling', 0o777)
    shutil.copyfile(f'{settings.gddataloc}\\{settings.savefile}', 'backup.dat')
    shutil.copyfile(f'{settings.gddataloc}\\{settings.savefile}', 'compiling/insert.dat')
    open('compiling/lvlstr.dat', 'x')
    
    #dependencies
    print('Assesing dependencies...')
    gs_parser.asess_dependencies(file)
    dependencies: list[tuple] = memory_modules.dependecies
    compilelist = [file, 'builtins/builtins.gss', 'gserr.gss', 'typing.gss']
    
    for dependency in dependencies:
        compileinsert = None
        if dependency[1] == 'rootdir':
            compileinsert = f'{settings.rootdir}\\{dependency[0]}'
        elif dependency[1] == 'lib':
            compileinsert = f'{settings.appdata_location}\\libraries\\{dependency[0]}'
        elif dependency[1] == 'stdlib':
            compileinsert = f'{settings.appdata_location}\\libraries\\std\\{dependency[0]}'
        
        if os.path.isdir(compileinsert) == True:
            if '@package_init.gss' in os.listdir(compileinsert):
                requirements_package = f'{compileinsert}\\@requirements.txt'
                
                for requirement in open(requirements_package).read().splitlines():
                    if not requirement in compilelist:
                        if requirement.startswith('./'):
                            requirement = f'{settings.rootdir}\\{requirement}'
                        elif requirement.startswith('../'):
                            requirement = f'{settings.appdata_location}\\libraries\\{requirement}'
                        elif requirement.startswith('.../'):
                            requirement = f'{settings.appdata_location}\\libraries\\std\\{requirement}'
                        compilelist.insert(requirement)
                
                compileinsert = f'{compileinsert}\\@package_init.gss'
            else:
                GSError(f'module {compileinsert} is not a modular gss file, package or library')
        
        compilelist.insert(len(compilelist)+1, compileinsert)
    
    #parsing
    print('Parsing...')
    total_parsing = []
    
    for dparse in dependencies:
        fparse = gs_parser.parse(dparse)
        for i in fparse:
            total_parsing.insert(0, i)
    
    #optimising
    tp_cache = []
    for i in enumerate(total_parsing):
        if not i[1] in tp_cache:
            tp_cache.insert(0, i[1])
        else:
            total_parsing.pop(i[0])
    del tp_cache
    
    print('Compiling...')
    compile_codeblock(total_parsing)
    
    #Link and finish
    print('Linking...')
    linker.linktosf(level)
    
    ws = False
    if not len(error_handling.warnings) == 0:
        ws = error_handling.warnings
    
    finish_compiling(ws)

def finish_compiling(warnings=False):
    os.rmdir('compiling')
    os.remove('backup.dat')
    if warnings == False:
        print('Sucsessfuly compiled')
        print('Would you like to launch Geometry Dash')
        c = input('Y/n: ')
        if c.lower() == 'y':
            open_tab('steam://rungameid/322170')
    else:
        print('Compiled with Warnings')
        print('Would you like to view warnings')
        c = input('Y/n: ')
        if c.lower() == 'y':
            for w in warnings:
                print(w)
            input('\nHit enter to exit: ')