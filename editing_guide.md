# Editing Guide

## GeoScript
GeoScript was mainly programmed in Python but the cli (geoscript.bat) and the quick fixes was programmed in Batch. The language was built on a modular system, all the important settings like the Geometry Dash savefile location are stored in a json file (hooking.json) and you can read the values with the modular python settings file (settings.py)

## geoscript.bat
### infomation
Language: Batch
Native location: C:\Windows\System32\geoscript.bat

### how it works
geoscript.bat is the file used in the GeoScript cli (command line interface) this file is programmed in Batch script. The file takes in 3 command line arguments (the arguments that suffix the initial command) the first argument is ment to be the "command" eg. build, settings or documentation, the second and third are ment to give argumrnts to the "command" the code looks like this,
``` batch
@echo off

set "command=%1"
set "arg1=%2"
set "arg2=%3"
```
How the script executes commands is with a simple if else chain using arg1 or arg2 when needed the program runs the commands by using the python cli to execute code in the command line, the file references the folder "GeoScript" it pulls functions form the init file and executes them. The codeclock looks something like this,
``` batch
if "%command%"=="build" (
    cmd /c python -c "import GeoScript; GeoScript.build('%arg1%', '%arg2%')"
) else if "%command%"=="settings" (
    cmd /c python -c "import GeoScript; GeoScript.settings()"
) else if "%command%"=="documentation" (
    cmd /c python -c "import GeoScript; GeoScript.documentation()"
) else if "%command%"=="uninstall" (
    cmd /c python -c "import GeoScript; GeoScript.uninstall()"
) else (
    cmd /c python -c "import GeoScript; GeoScript.main()"
)
```

## __init__.py
### infomation
Language: Python
Native location: C:\Windows\System32\GeoScript\__init__.py

### how it works