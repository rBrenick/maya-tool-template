@ECHO OFF
:BEGIN
CLS

ECHO Welcome to TOOL_NAME
ECHO Here are the options for install
ECHO.


ECHO 1. Install
ECHO 2. Uninstall
ECHO.
ECHO Advanced:
ECHO 3. Make New Tool from TOOL_NAME

ECHO.
SET /P AREYOUSURE=Choice: 
IF /I "%AREYOUSURE%" EQU "1" GOTO :ONE
IF /I "%AREYOUSURE%" EQU "2" GOTO :TWO
IF /I "%AREYOUSURE%" EQU "3" GOTO :THREE

:ONE
CALL _install_\install_maya_module.bat
GOTO END

:TWO
CALL _install_\uninstall_maya_module.bat
GOTO END

:THREE
Powershell.exe -executionpolicy remotesigned -File  _install_\create_new_tool.ps1


:END
PAUSE