@echo off

set "command=%1"

if "%command%"=="install_all_packages" (
    cmd /c pip install -r "installation/requirements.txt"
) else if "%command%"=="open_installer" (
    cmd /c python "installation/GeoInstaller.py"
)