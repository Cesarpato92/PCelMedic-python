@echo off
setlocal
echo ========================================================
echo CONFIGURADOR DE FIREWALL PARA PCELMEDIC
echo ========================================================
echo.
echo Verificando permisos de Administrador...

:: Comprobar privilegios de administrador
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Este script debe ser ejecutado como Administrador.
    echo Por favor, cierre esto, haga clic derecho en el archivo .bat 
    echo y seleccione "Ejecutar como administrador".
    pause
    exit /b 1
)

echo Permisos de Administrador confirmados.
echo Creando reglas de Firewall para el puerto 3306...
echo.

:: Ejecutar comando PowerShell para añadir la regla
powershell -Command "New-NetFirewallRule -DisplayName 'PCelMedic - MySQL Localhost Solo' -Direction Inbound -LocalPort 3306 -Protocol TCP -Action Allow -RemoteAddress '127.0.0.1' -Profile Any -Description 'Permite conexion a MySQL solo de forma local para PCelMedic'"

:: Informar al usuario
echo.
echo ========================================================
echo Regla aplicada con exito. 
echo Windows Firewall ahora permite conexiones a MySQL 
echo unicamnente desde el localhost (127.0.0.1).
echo ========================================================
pause
