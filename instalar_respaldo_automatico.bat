@echo off
:: Script para instalar la tarea de respaldo automático en programador de tareas de Windows para la base de datos PCelMedic
:: SOLO SE EJECUTA SI ES COMO ADMINISTRADOR

:: Verificar si se está ejecutando como administrador
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ------------------------------------------------
    echo              ERROR DE PERMISOS
    echo Este script debe ejecutarse como Administrador.
    echo.
    echo Haga clic derecho en el archivo y seleccione:
    echo "Ejecutar como administrador"
    echo.
    echo ------------------------------------------------
    pause
    exit /b 1
)

echo Instalando tarea de respaldo automatico para PCelMedic
echo.

:: Crea la carpeta Backups si no existe
if not exist "C:\PCelMedic_backup\Backups\" mkdir "C:\PCelMedic_backup\Backups"

:: Solicitar credenciales de la base de datos al usuario (no se almacenan en el repositorio)
echo ------------------------------------------------
echo Configuracion de credenciales de la base de datos
echo ------------------------------------------------
set /p DB_USER=Ingrese el usuario de MySQL para el respaldo: 
set /p DB_PASSWORD=Ingrese la contrasena de MySQL para el respaldo: 
set /p DB_NAME=Ingrese el nombre de la base de datos (por defecto pcelmedic): 
if "%DB_NAME%"=="" set DB_NAME=pcelmedic

:: Crear archivo de configuracion de credenciales para mysqldump (--defaults-extra-file).
:: Este archivo NO se versiona en el repositorio y se restringe a SYSTEM y administradores.
echo Creando archivo de credenciales en C:\PCelMedic_backup\mysql_backup.cnf...
(
echo [client]
echo user=%DB_USER%
echo password=%DB_PASSWORD%
) > "C:\PCelMedic_backup\mysql_backup.cnf"

:: Restringir el acceso al archivo de credenciales solo a SYSTEM y administradores
icacls "C:\PCelMedic_backup\mysql_backup.cnf" /inheritance:r /grant:r "SYSTEM:(F)" "Administrators:(F)" >nul

:: Crea el script de respaldo (backup_pcelmedic.bat)
echo Creando script de respaldo...

(
echo @echo off
echo :: Script de respaldo automatico - PCelMedic
echo set FECHA=%%DATE:~10,4%%%%DATE:~4,2%%%%DATE:~7,2%%
echo set HORA=%%TIME:~0,2%%%%TIME:~3,2%%
echo set HORA=%%HORA: =0%%
echo if not exist "C:\PCelMedic_backup\Backups\" mkdir "C:\PCelMedic_backup\Backups"
echo "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" --defaults-extra-file="C:\PCelMedic_backup\mysql_backup.cnf" %DB_NAME% ^> "C:\PCelMedic_backup\Backups\backup_pcelmedic_%%FECHA%%_%%HORA%%.sql"
echo forfiles /p "C:\PCelMedic_backup\Backups\" /m "backup_pcelmedic_*.sql" /d -90 /c "cmd /c del @file"
echo echo Respaldo completado: C:\PCelMedic_backup\Backups\backup_pcelmedic_%%FECHA%%_%%HORA%%.sql
) > "C:\PCelMedic_backup\backup_pcelmedic.bat"

echo Script de respaldo creado en C:\PCelMedic_backup\backup_pcelmedic.bat
echo.

:: Creaa la tarea en el programador de tareas usando schtasks
echo Creando tarea en el Programador de Tareas...

schtasks /create /tn "PCelMedic - Respaldo BD" ^
    /tr "C:\PCelMedic_backup\backup_pcelmedic.bat" ^
    /sc daily ^
    /st 20:00 ^
    /ru "SYSTEM" ^
    /rl HIGHEST ^
    /f

if %errorlevel% equ 0 (
    echo ------------------------------------------------
    echo          TAREA CREADA EXITOSAMENTE!
    echo La base de datos se respaldara todos los dias a las 8:00 PM
    echo Los respaldos se guardan en C:\PCelMedic_backup\Backups\
    echo ------------------------------------------------
    echo Los respaldos con mas de 90 dias se eliminan automaticamente
    echo IMPORTANTE: Las credenciales se guardaron en C:\PCelMedic_backup\mysql_backup.cnf
    echo Si necesita cambiar la contrasena, vuelva a ejecutar este instalador.

) else (
    echo ------------------------------------------------
    echo       ERROR: No se pudo crear la tarea
    echo Verifique que el script se ejecuta como Administrador

)
pause
