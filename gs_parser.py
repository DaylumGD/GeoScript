from error_handling import GSError, GSWarnings
import memory_modules
import os
import settings

def asess_dependencies(file=str):
    contents = open(file).read().splitlines()
    
    for line in contents:
        if line.startswith('#include') == True:
            line = line.removeprefix('#include ')
            if not line in os.listdir(settings.rootdir):
                if not line in os.listdir(f'{settings.appdata_location}\\libraries'):
                    if not line in os.listdir(f'{settings.appdata_location}\\libraries\\std'):
                        GSError(f'Module {line} does not exist')
                    else:
                        memory_modules.insert_to_dependencies(line, 'stdlib')
                else:
                    memory_modules.insert_to_dependencies(line, 'lib')
            else:
                memory_modules.insert_to_dependencies(line, 'rootdir')
            continue
            
        elif line.startswith('#export') == True:
            line = line.removeprefix('#export ')
            lnsplit = line.split(' ')
            if not lnsplit[0] in os.listdir(settings.rootdir):
                if not lnsplit[0] in os.listdir(f'{settings.appdata_location}/libraries'):
                    if not lnsplit[0] in os.listdir(f'{settings.appdata_location}/libraries/std'):
                        GSError(f'Module {lnsplit[0]} does not exist')
                    else:
                        memory_modules.insert_to_dependencies(lnsplit[0], 'stdlib')
                else:
                    memory_modules.insert_to_dependencies(lnsplit[0], 'lib')
            else:
                memory_modules.insert_to_dependencies(lnsplit[0], 'rootdir')

def parse(file=str, strmode=False) -> list[tuple[str]]:
    parsedfile = []
    linenum = 0
    searchscope = 'Global'
    
    def insert_to_parser(*args):
        parsedfile.insert(0, args)
    
    def alter_searchscope(value, searchscope):
        if searchscope == 'Global':
            return value
        else:
            return f'{searchscope}.{value}'
    
    if strmode == False: contents: list[str] = open(file).read().splitlines()
    else: contents = file.split(';')
    
    for line in contents:
        #default values
        linearchive = line
        linenum += 1
        foobar: None
        
        # ";" syntax handling
        lsplit = line.split(';', 1)
        if len(lsplit) == 1:
            line = lsplit[0]
        else:
            line = lsplit[0]
            pcomment = lsplit[1]
            pcomment = pcomment.strip(' ')
            if not pcomment.startswith('>>'):
                GSError('codeblocks must be seperated with newlines', errtype='SyntaxError', codeline=(linenum, line))
        
        #whitespace handling
        while line.startswith(' ') == True:
            line = line.removeprefix(' ')
        while line.endswith(' ') == True:
            line = line.removesuffix(' ')
        
        while line.endswith('\n') == True:
            line = line.removesuffix('\n')
        while line.startswith('\n') == True:
            line = line.removeprefix('\n')
        
        while line.startswith('\t') == True:
            line = line.removeprefix('\t')
        while line.endswith('\t') == True:
            line = line.removesuffix('\t')
        
        #Comment handling
        if line.startswith('>>') == True:
            continue
        elif line.startswith('/*') == True:
            continue
        elif line.startswith('>>!') == True:
            continue
        
        #scope handling
        if line == '}':
            if '.' in searchscope:
                searchscope = searchscope.split('.')
                searchscope.pop()
                searchscope = '.'.join(searchscope)
            else:
                searchscope = 'Global'
            continue
        
        #Parser
        if line.startswith('#') == True:
            #definitive statements
            if line.startswith('#define'):
                line = line.lstrip(' ')
                line = line.removeprefix('#define')
                line = line.split(':')
                
                if line[0].startswith('#'):
                    GSWarnings('Function name starts with a #, this function is unable to be called')
                elif line[0].startswith('@'):
                    GSWarnings('Function name starts with a @, this function is unable to be called')
                if line[0].isdigit():
                    GSWarnings(f'Function name is an intager the number {lnsplit[0]} is no longer able to be used')
                
                try:
                    memory_modules.insert_heap_memory(line[0], line[1].split('=')[0], line[1].split('=')[1], searchscope)
                except IndexError:
                    try: foobar = line[1].split('=')[0]
                    except: GSError('Variable type is not defined', errtype='SyntaxError', codeline=(linenum, linearchive))
                    try: foobar = line[1].split('=')[1]
                    except: GSError('Value is not defined', errtype='SyntaxError', codeline=(linenum, linearchive))
                insert_to_parser('#define', line[0], line[1].split('=')[0], line[1].split('=')[1], searchscope)
            
            elif line.startswith('#include'):
                continue
            elif line.startswith('#export'):
                continue
            
            elif line.startswith('#function'):
                line = line.removeprefix('#function ')
                line = line.lstrip(' ')
                lnsplit = line.split('(')
                lnsplit[1] = lnsplit[1].removesuffix(')')
                
                if lnsplit[1] == '':
                    lnsplit[1] = None
                
                if lnsplit[0].startswith('#'):
                    GSWarnings('Function name starts with a #, this function is unable to be called')
                elif lnsplit[0].startswith('@'):
                    GSWarnings('Function name starts with a @, this function is unable to be called')
                if lnsplit[0].isdigit():
                    GSWarnings(f'Function name is an intager the number {lnsplit[0]} is no longer able to be used')
                
                insert_to_parser('#function', lnsplit[0], lnsplit[1].split(','), searchscope)
                searchscope = alter_searchscope(lnsplit[0], searchscope)
            
            else:
                GSError(f'{linearchive} is not a definitive statement', errtype='StatementError', codeline=(linenum, linearchive))

        elif line.startswith('@') == True:
            #Structule statements
            if line.startswith('@container'):
                line = line.lstrip(' ')
                lnsplit = line.split('(')
                lnsplit[1] = lnsplit[1].removesuffix(')')
                arguments = lnsplit[1].split(',')
                
                if not len(arguments) == 2:
                    GSWarnings('container does not have an end point')
                
                insert_to_parser('@container', arguments)
                searchscope = alter_searchscope('container', searchscope)
            
            elif line.startswith('@structure'):
                line = line.removeprefix('@container')
                line = line.removesuffix('{')
                
                insert_to_parser('@structure', line, searchscope)
                searchscope = alter_searchscope(line, searchscope)
            
            elif line.startswith('@class'):
                line = line.removeprefix('@class')
                line = line.removesuffix('{')
                
                insert_to_parser('@class', line, searchscope)
                searchscope = alter_searchscope(line, searchscope)
            
            elif line.startswith('@add'):
                line = line.strip(' ')
                line = line.removeprefix('@add("')
                line = line.removesuffix('")')
                
                insert_to_parser('@add', line)
        
            else:
                GSError(f'{linearchive} is not a structule element', errtype='StatementError', codeline=(linenum, linearchive))
        
        #object oriented fetures
        elif line.startswith('>&'):
            line = line.strip(' ')
            line = line.removeprefix('>&')
                
            insert_to_parser('inheritance', line, searchscope)
        elif line.startswith('>$'):
            line = line.strip(' ')
            line = line.removeprefix('>$')
                
            insert_to_parser('decorator', line, searchscope)
        
        elif line.endswith(')') == True:
            line = line.lstrip(' ')
            lnsplit = line.split('(')
            lnsplit[1] = lnsplit[1].removesuffix(')')
            
            func = memory_modules.functionBlock(lnsplit[0], lnsplit[1], None, None)
            memory_modules.insert_to_callstack(func)
        
        #controll flow
        elif line.startswith('if'):
            insert_to_parser('if statement', line.removeprefix('if '), None)
        elif line.startswith('} else {'):
            insert_to_parser('else statement', None)
        elif line.startswith('} else if '):
            insert_to_parser('else if statement', line.removeprefix('} else if '), None)
        
        #event loops
        elif line.startswith('while '):
            line = line.strip(' ')
            insert_to_parser('while loop', line.removeprefix('while(').removesuffix('){'), None)
        
        elif line.startswith('for '):
            line = line.strip(' ')
            lnsplit = line.removeprefix('for(').removesuffix('){').split(';')
            searchscope = alter_searchscope('main::forloop', searchscope)
            memory_modules.insert_heap_memory(lnsplit[0], 'int', '0', searchscope)
            insert_to_parser('for loop', lnsplit[0], lnsplit[1], lnsplit[2])
        
        elif line.startswith('forEach '):
            line = line.strip(' ')
            lnsplit = lnsplit = line.removeprefix('forEach(').removesuffix('){').split(';')
            searchscope = alter_searchscope('main::forEachloop', searchscope)
            memory_modules.insert_heap_memory(lnsplit[0], 'auto', None, searchscope)
            insert_to_parser('forEach loop', lnsplit[0], lnsplit[1])
        
        #errors
        else:
            if line == '':
                continue
            GSError('line is not a definitive statement, structule element, function, variable, class, controll block or event loop', errtype='UndefinedError', codeline=(linenum, line))
    
    if not searchscope == 'Global':
        GSWarnings('File does not end with a searchscope of "Global"')
    return parsedfile