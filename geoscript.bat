@echo off

set "command=%1"
set "arg1=%2"
set "arg2=%3"

if "%command%"=="build" (
    cmd /c python -c "import GeoScript; GeoScript.build('%arg1%', '%arg2%')"
) else if "%command%"=="settings" (
    cmd /c python -c "import GeoScript; GeoScript.settings()"
) else if "%command%"=="documentation" (
    cmd /c python -c "import GeoScript; GeoScript.documentation()"
) else (
    cmd /c python -c "import GeoScript; GeoScript.main()"
)
