from error_handling import GSError

def auto_type(gtype=str, errortype=()) -> str:
    if gtype.startswith('"') == True:
        return 'str'
    elif gtype.isnumeric() == True:
        return 'int'
    elif '.' in gtype:
        score = 0
        for i in gtype.split('.'):
            if i.isnumeric() == True:
                score += 1
        if score == 2:
            return 'float'
    if gtype.endswith('g') == True:
        return 'group'
    elif gtype.endswith('c') == True:
        return 'counter'
    elif gtype.endswith('cs') == True:
        return 'collision'
    
    elif gtype.startswith('([') == True:
        return 'codeblock'
    elif gtype.startswith('[') == True:
        return 'array'
    elif gtype.startswith('{') == True:
        return 'dict'
    elif gtype.startswith('(') == True:
        return 'collection'
    else:
        GSError('Type does not exist check your spelling or create new gtype', errtype='UndeterminableType', codeline=errortype)

def name_checking(name=str, errortype=()):
    if '#' in name:
        GSError('"#" could not be in Variable, Function and Classe names', errtype='InvalidExpressionName', codeline=errortype)
    elif '@' in name:
        GSError('"@" could not be in Variable, Function and Classe names', errtype='InvalidExpressionName', codeline=errortype)
    elif name.isnumeric() == True:
        GSError('Variables, Functions and Classes could not be named intagers or floats', errtype='InvalidExpressionName', codeline=errortype)
    elif name.startswith('>>') == True:
        GSError('Variables, Functions and Classes could not be named comments', errtype='InvalidExpressionName', codeline=errortype)