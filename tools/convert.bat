@echo off
title .UI to .py files converter !
echo Generate Python files from .UI files!
pause

echo   "| |"
echo   "| |"
echo  "\   /"
echo   "\ /"
echo    "V"
echo UI file Name
set /p UiName=Enter .UI file Name: 
echo   "| |"
echo   "| |"
echo  "\   /"
echo   "\ /"
echo    "V" 
echo PY file Name
set /p PyName=Enter .PY file Name: 
echo   "| |"
echo   "| |"
echo  "\   /"
echo   "\ /"
echo    "V"
echo Start Converting Files Please wait.

call python -m PyQt5.uic.pyuic -x "%UiName%" -o "%PyName%.pyw"

echo Job Completed.
pause