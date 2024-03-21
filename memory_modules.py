heap_memory = {}
module_memory = {}
callstack = []
dependecies = []

class functionBlock:
    def __init__(self, name, args, returntype, codeblock) -> None:
        self.name = name
        self.returntype = returntype
        self.codeblock = codeblock
        self.args = args

def insert_heap_memory(key, vtype, value, scope):
    global heap_memory
    k, v = [], []
    for ak in heap_memory:
        k.insert(0, ak)
        v.insert(0, heap_memory.get(ak))
    k.insert(0, key)
    v.insert(0, (vtype, value, scope))
    
    heap_memory = {ik: iv for ik, iv in zip(k, v)}

def modify_heap_memory(key, vtype, value):
    global heap_memory
    k, v = [], []
    for ak in heap_memory:
        k.insert(0, ak)
        v.insert(0, heap_memory.get(ak))
    
    for i in enumerate(heap_memory):
        if i[1] == key:
            v[i[0]][0] = vtype
            v[i[0]][1] = value
    
    heap_memory = {ik: iv for ik, iv in zip(k, v)}

def insert_module_memory(key, code, returntype):
    global module_memory
    k, v = [], []
    for ak in module_memory:
        k.insert(0, ak)
        v.insert(0, module_memory.get(ak))
    k.insert(0, key)
    v.insert(0, (code, returntype))
    
    module_memory = {ik: iv for ik, iv in zip(k, v)}

def insert_to_callstack(function=functionBlock):
    global callstack
    callstack.insert(len(callstack)+1, (function.name, function.returntype, function.args, function.codeblock))

def insert_to_dependencies(modulename, location):
    global dependecies
    dependecies.insert(len(dependecies)+1, (modulename, location))