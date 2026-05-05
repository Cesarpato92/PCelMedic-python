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

:: Crea el script de respaldo (backup_pcelmedic.bat)
echo Creando script de respaldo...

(
echo @echo off
echo :: Script de respaldo automatico - PCelMedic
echo set FECHA=%%DATE:~10,4%%%%DATE:~4,2%%%%DATE:~7,2%%
echo set HORA=%%TIME:~0,2%%%%TIME:~3,2%%
echo set HORA=%%HORA: =0%%
echo if not exist "C:\PCelMedic_backup\Backups\" mkdir "C:\PCelMedic_backup\Backups"
echo "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u user_limited_pcelmedic -pPass_Secure_XLMS19dXkd8x3AS pcelmedic ^> "C:\PCelMedic_backup\Backups\backup_pcelmedic_%%FECHA%%_%%HORA%%.sql"
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

) else (
    echo ------------------------------------------------
    echo       ERROR: No se pudo crear la tarea
    echo Verifique que el script se ejecuta como Administrador

)
pause