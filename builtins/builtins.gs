>> Default objects
#include typing.gs

@class object {
    #define pinboard: list = [];
    #define object_info: str = "";

    >> builtins
    #define __annotations__: str = "";
    #define __base__: str = "";
    #define __scope__: str = "Global";
    #define __callid__: str = "";
    
    #function gom() {
        >$ typing.property
        #define result: dict = {"annotations": __annotations__, "base": __base__, "scope": __scope__, "callid": __callid__};
        return result;
    };
}

@class Function {
    >& object

    #function function_id() {
        >$ typing.property
    }
}