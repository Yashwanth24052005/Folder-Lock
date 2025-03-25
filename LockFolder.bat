@ECHO OFF

title Folder Locker

if EXIST "key.py" (
    goto REGISTER
) else (
    goto LOCKORUNLOCK
)

:REGISTER
python key.py
del "key.py"
del "locker.py"
goto LOCKORUNLOCK

:LOCKORUNLOCK
cd dist
python locker.py

