@echo off
setlocal

title Firewall MySQL Local y Docker
echo =====================================
echo Script: firewall_local_mysql.bat
echo Descripción: crea reglas de Windows Firewall para MySQL local (3306) y MySQL en Docker (3308).
echo Obligatorio: ejecutar en modo administrador.
echo =====================================
echo.
echo Este script debe ejecutarse obligatoriamente en modo administrador.
echo Si no se ejecuta con privilegios elevados, no podra crear las reglas de firewall.
echo.
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: el script no se esta ejecutando como administrador.
    echo Por favor, cierre esta ventana y ejecute el archivo con "Ejecutar como administrador".
    pause >nul
    exit /b 1
)

echo Configurando el firewall de Windows para MySQL local y Docker...

REM Eliminar reglas existentes con el mismo nombre para evitar duplicados.
netsh advfirewall firewall delete rule name="MySQL Local" protocol=TCP localport=3306 >nul 2>&1
netsh advfirewall firewall delete rule name="MySQL Docker" protocol=TCP localport=3308 >nul 2>&1

REM Crear reglas de entrada para los puertos MySQL local y Docker.
netsh advfirewall firewall add rule name="MySQL Local" dir=in action=allow protocol=TCP localport=3306 profile=private,public
if %errorlevel% neq 0 goto error
netsh advfirewall firewall add rule name="MySQL Docker" dir=in action=allow protocol=TCP localport=3308 profile=private,public
if %errorlevel% neq 0 goto error

echo Reglas de firewall creadas correctamente para los puertos 3306 y 3308.
goto end

:error
echo Error: no se pudieron crear las reglas de firewall.

:end
echo Presiona una tecla para salir...
pause >nul
endlocal
