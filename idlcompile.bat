@echo off
cd /d %~dp0
setlocal
for %%I in (python.exe) do if exist %%~$path:I set f=%%~$path:I
if exist %f% (
  %f:python.exe=%omniidl.exe -bpython -I"/usr/include/openrtm-1.2/rtm/idl" idl/VelocitySwitcher.idl 
) else (
  echo "python.exe" can not be found.
  echo Please modify PATH environmental variable for python command.
)
endlocal
