# PCelMedic - Sistema de Gestion para Taller de Celulares

<p align="center">
  <strong>Eficiencia y transparencia en tu servicio tecnico.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange" alt="Tkinter">
  <img src="https://img.shields.io/badge/BD-MySQL%208.0-4479A1?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Licencia-Privada-red" alt="Licencia">
</p>

---

**PCelMedic** es una aplicacion de escritorio profesional desarrollada en **Python** con **Tkinter**, disenada para optimizar la operacion diaria de talleres de reparacion de dispositivos moviles. Gestiona el ciclo completo: desde el registro del cliente y su dispositivo, pasando por la reparacion y facturacion, hasta el control de garantias y analisis financiero.

---

## Guia Rapida de Inicio

### Instalación en 5 pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cesarpato92/PCelMedic-python.git
cd PCelMedic-python

# 2. Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear base de datos
mysql -u tu_usuario -p < pcelmedic_database.sql

# 5. Ejecutar la aplicación
python main.py
```

---

## Tabla de Contenidos

- [Guia Rapida de Inicio](#guia-rapida-de-inicio)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalacion](#instalacion)
- [Configuracion de la Base de Datos](#configuracion-de-la-base-de-datos)
- [Configuracion del Administrador](#configuracion-del-administrador)
- [Uso](#uso)
- [Modulos del Sistema](#modulos-del-sistema)
- [Generacion de Reportes PDF](#generacion-de-reportes-pdf)
- [Tests](#tests)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estructura de Archivos](#estructura-de-archivos)

---

## Caracteristicas Principales

- **Gestión Integral de Clientes**: Validación completa de datos (cédula, email, celular, nombre) con búsqueda y filtrado.
- **Control del Ciclo de Reparación**: Estados bien definidos (*En Proceso* → *Completada* → *Entregada*) con seguimiento en tiempo real.
- **Facturación Inteligente**: Generación automática de facturas vinculadas a reparaciones con cálculo automatizado de totales.
- **Gestión de Garantías Flexible**: Flujo de entrada y salida, estados configurables, seguimiento de vencimientos y observaciones detalladas.
- **Panel Financiero Avanzado**: Gráficos dinámicos con Matplotlib, análisis comparativo (ventas vs. costos) y exportación a Excel.
- **Reportes Profesionales en PDF**: Órdenes de reparación, recibos de garantía y facturas personalizadas.
- **Seguridad Robusta**: Autenticación de administrador con contraseñas encriptadas (bcrypt), transacciones ACID con commit/rollback automático.
- **Base de Datos Optimizada**: Índices estratégicos, vistas útiles para reportes y procedimientos almacenados para operaciones complejas.
- **Interfaz Intuitiva**: Navegación clara con iconografía, validación en tiempo real y mensajes de error descriptivos.

---

## Arquitectura del Proyecto

El sistema sigue una arquitectura en capas que separa responsabilidades:

```
+-----------------------------------------+
|           GUI (Tkinter)                 |  Interfaz de usuario
|  VentanaPrincipal, VentanaRegistro      |
|  VentanaReparacion, VentanaFactura      |
|  VentanaGarantia, VentanaFinanzas       |
+-----------------------------------------+
|           Logica (Negocio)              |  Validaciones y reglas de negocio
|  LogicaCliente, LogicaDispositivo       |
|  LogicaReparacion, LogicaFactura        |
|  LogicaGarantia, GeneradorPDF           |
+-----------------------------------------+
|           DAO (Acceso a Datos)          |  Consultas SQL aisladas
|  ClienteDAO, DispositivoDAO             |
|  ReparacionDAO, FacturasDAO             |
|  GarantiaDAO                            |
+-----------------------------------------+
|           Modelo (Entidades)            |  Objetos del dominio
|  ModeloCliente, ModeloDispositivo       |
|  ModeloReparacion, ModeloFactura        |
|  ModeloGarantia                         |
+-----------------------------------------+
|         Utilidades (Soporte)            |  Validadores,
|      Validador, ManejadorPassword       |  encriptacion
+-----------------------------------------+
+-----------------------------------------+
|         Config (Conexion a DB)          |  Conexion BD
|  Conexion, TransaccionConexion          |  
|                                         | 
+-----------------------------------------+
```

---

## Requisitos Previos

Antes de comenzar, asegurate de tener instalado:

| Requisito | Version |
|-----------|---------|
| **Python** | 3.13 o superior |
| **MySQL Server** | 8.0 (recomendado) |
| **pip** | Ultima version estable |

Opcionalmente, un gestor de bases de datos como **MySQL Workbench** o **DBeaver** para administrar el esquema.

---

## Instalacion

### 1. Clonar el repositorio

```bash
git clone https://github.com/Cesarpato92/PCelMedic-python.git
cd PCelMedic-python
```

### 2. Crear y activar un entorno virtual

```bash
# Crear el entorno virtual
python -m venv .venv

# Activar en Windows (PowerShell)
.venv\Scripts\activate

# Activar en Windows (CMD)
.venv\Scripts\activate.bat

# Activar en Linux / macOS
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> **Dependencias principales**:
> - `mysql-connector-python`: Driver para conexión a MySQL 8.0+
> - `matplotlib`: Visualización de gráficos financieros
> - `fpdf2`: Generación de reportes PDF de alta calidad
> - `openpyxl`: Exportación a Excel (.xlsx)
> - `bcrypt`: Encriptación segura de contraseñas (12 rounds)
> - `tkcalendar`: Selectores de fecha en la interfaz
> - `pillow`: Procesamiento de imágenes
> - `pytest`: Framework de testing unitario
> - `python-dotenv`: Biblioteca para lectura de variables de entorno


---

## Configuracion de la Base de Datos

### Opción 1: Usando el Script SQL (Recomendado)

1. **Ejecutar el script SQL** para crear la base de datos y todas las tablas:

   ```bash
   # Desde PowerShell o CMD
   mysql -u tu_usuario -p < pcelmedic_database.sql
   
   # O desde MySQL CLI
   mysql> SOURCE pcelmedic_database.sql;
   ```

   > El script `pcelmedic_database.sql` incluye:
   > - Creación de base de datos con charset UTF-8
   > - 5 tablas principales (clientes, dispositivos, reparaciones, facturas, garantias)
   > - Índices para optimizar consultas
   > - Restricciones de integridad referencial
   

2. **Configurar las credenciales de conexión usando archivo `.env`**:

   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```env
   # Configuración de Base de Datos
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=tu_usuario
   DB_PASSWORD=tu_password
   DB_DATABASE=pcelmedic_db
   ```

   > **Nota de seguridad**: El archivo `.env` NO debe versionarse en Git. 
   > Asegúrate de que está incluido en `.gitignore` (ya está por defecto).
   
   El archivo [Config/Conexion.py](Config/Conexion.py) carga automáticamente estas variables usando `python-dotenv`.

### Opción 2: Creación Manual

Si prefieres crear la base de datos manualmente:

```sql
CREATE DATABASE IF NOT EXISTS pcelmedic_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE pcelmedic_db;

-- Crear tablas individuales según los DAOs
-- (Consulta pcelmedic_database.sql para la definición completa)
```

### Verificación

Antes de ejecutar la aplicación, verifica que todo está configurado correctamente:

1. **Verificar que el archivo `.env` existe** en la raíz del proyecto:
   ```bash
   # En Windows (PowerShell o CMD)
   dir .env
   
   # En Linux / macOS
   ls -la .env
   ```

2. **Verificar que las variables de entorno se cargan correctamente**:
   ```bash
   # Conectar a MySQL con las credenciales del .env
   mysql -u tu_usuario -p pcelmedic_db
   ```

3. **Conectar a MySQL y verificar la base de datos**:

   ```bash
   # Listar tablas
   SHOW TABLES;

   # Verificar estructura de una tabla
   DESCRIBE clientes;
   ```

### Plantilla de variables de entorno (`.env.example`)

Se recomienda crear un archivo `.env.example` **versionado en Git** como referencia para nuevos desarrolladores:

```env
# Configuración de Base de Datos
# Cambia estos valores según tu entorno local
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=contraseña_aqui
DB_DATABASE=pcelmedic_db
```

Para configurar tu entorno:
1. Copia `.env.example` a `.env`
2. Edita los valores en `.env` con tus credenciales reales
3. El archivo `.env` está en `.gitignore` y no se versionará

---

## Configuracion del Administrador

### Autenticación Segura del Módulo Finanzas

El acceso al módulo **Finanzas** está protegido por autenticación de administrador. Las credenciales se almacenan de forma segura en el archivo `.configAdmin` (no versionado en Git).

#### Crear credenciales iniciales

```bash
python Utilidades/EncriptarConfigAdmin.py
```

Se te pedirá ingresar:
1. **Usuario**: Nombre de usuario del administrador (ej: `admin`)
2. **Contraseña**: Contraseña en texto plano (será encriptada con bcrypt)

El script generará:
- **`.configAdmin`**: Archivo con credenciales encriptadas (formato: `USER=admin\nPASSWORD=<hash_bcrypt>`)
- **`.configAdmin.backup`**: Copia de seguridad de la configuración anterior

#### Formato del archivo `.configAdmin`

```
USER=admin
PASSWORD=$2b$12$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
```

### Seguridad y Mejores Prácticas

- ✅ **Las contraseñas se encriptan con bcrypt** (12 rounds) - nunca se almacenan en texto plano
- ✅ **El archivo `.configAdmin` no se versionan en Git** - se incluye en `.gitignore`
- ✅ **Hacer backup regular** del archivo `.configAdmin.backup` en lugar seguro
- ⚠️ **Cambiar la contraseña periódicamente** ejecutando nuevamente `EncriptarConfigAdmin.py`

---

## Uso

Ejecuta la aplicacion desde la raiz del proyecto:

```bash
python main.py
```

Se abrira la ventana principal con la barra de navegacion que permite acceder a todos los modulos del sistema.

---

## Modulos del Sistema

### Registro de Clientes y Dispositivos (`VentanaRegistro`)

- Captura de datos del cliente: nombre, cedula, email y celular.
- Registro de dispositivos vinculados al cliente con: marca, modelo, tipo de reparacion y contrasena de acceso (PIN, patron, texto/numeros).
- Validacion automatica de todos los campos antes de persistir.

### Control de Reparaciones (`VentanaReparacion`)

- Registro de nuevas reparaciones asociadas a un dispositivo.
- Gestion del ciclo de vida con estados: **En Proceso** -> **Completada** -> **Entregada**.
- Registro de diagnosticos, repuestos utilizados y costo de mano de obra.
- Generacion automatica de ordenes de reparacion en PDF.

### Facturacion (`VentanaFactura`)

- Generacion de facturas basadas en reparaciones completadas.
- Calculo automatico de totales (repuestos + servicio tecnico).
- Generacion de recibos de pago en PDF.

### Gestion de Garantias

| Ventana | Funcion |
|---------|---------|
| `VentanaEntradaGarantia` | Registro de dispositivos que regresan por fallas cubiertas. |
| `VentanaSalidaGarantia` | Resolucion de la garantia, comentarios finales y entrega. |
| `VentanaGarantia` | Vista general y busqueda de garantias por ID. |

- Estados de garantia: **En Garantia**, **Completada**, **Rechazada**.
- Historial detallado de observaciones.

### Analisis Financiero (`VentanaFinanzas`)

> Requiere autenticacion de administrador.

- **Graficos dinamicos** con barras agrupadas (ventas vs. costos de repuestos) usando Matplotlib.
- **Filtro por rango de fechas** con selectores de calendario.
- **Detalle de movimientos** con tabla dia a dia.
- **Exportacion a Excel** (.xlsx) del listado de clientes.

---

## Generacion de Reportes PDF

El sistema genera tres tipos de reportes en PDF, almacenados en la carpeta `Reportes/`:

| Tipo de Reporte | Archivo | Contenido |
|-----------------|---------|-----------|
| **Orden de Reparacion** | `Orden_{id}-{cedula}.pdf` | Datos del cliente, dispositivo y detalles de la reparacion. |
| **Recibo de Garantia** | `Garantia_{id}-{cedula}.pdf` | Informacion completa del cliente, dispositivo, reparacion y garantia. |
| **Factura** | `Factura_{id}-{cedula}.pdf` | Recibo de pago con detalle del servicio y totales. |

---

## Tests

El proyecto incluye una **suite completa de pruebas unitarias** desarrollada con **pytest**. Los tests validan la capa de lógica de negocio asegurando confiabilidad y mantenibilidad del código.

### Ejecutar pruebas

```bash
# Ejecutar todas las pruebas con salida detallada
pytest tests/ -v

# Ejecutar pruebas específicas
pytest tests/test_logica_cliente.py -v

# Ejecutar con cobertura de código
pytest tests/ --cov=Logica --cov-report=html

# Ejecutar pruebas y mostrar output de print
pytest tests/ -v -s
```

### Cobertura de pruebas

| Módulo | Archivo | Casos de uso |
|--------|---------|-------------|
| **Clientes** | `test_logica_cliente.py` | Validación de cédula (formato), email (RFC), nombre, celular |
| **Reparaciones** | `test_logica_reparacion.py` | Estados válidos, transiciones permitidas, cálculo de costos |
| **Garantías** | `test_logica_garantia.py` | Validación de fechas, estados, observaciones |
| **Precios** | `test_validador_precio.py` | Números positivos, decimales, cero no permitido |

### Ejecutar tests de forma automática

Para ejecutar tests cada vez que haces cambios (modo watch):

```bash
# Usando pytest-watch (si está instalado)
ptw tests/ -v
```

---

## Tecnologias Utilizadas

### Stack Tecnológico

| Componente | Tecnología | Versión | Propósito |
|-----------|-----------|---------|----------|
| **Lenguaje** | Python | 3.13+ | Lenguaje principal |
| **GUI** | Tkinter / ttk | Built-in | Interfaz gráfica de escritorio multiplataforma |
| **Base de Datos** | MySQL | 8.0+ | Base de datos relacional con transacciones ACID |
| **Driver BD** | mysql-connector-python | 9.0+ | Conexión segura a MySQL |
| **Visualización** | Matplotlib | 3.8+ | Gráficos de barras, líneas y análisis financiero |
| **Reportes PDF** | fpdf2 | 2.7+ | Generación de PDFs profesionales |
| **Excel** | openpyxl | 3.10+ | Exportación de datos a archivos .xlsx |
| **Seguridad** | bcrypt | 4.0+ | Hash seguro de contraseñas (12 rounds) |
| **Calendario** | tkcalendar | 1.6+ | Selectores de fecha en GUI |
| **Imágenes** | Pillow | 10.0+ | Procesamiento y manipulación de imágenes |
| **Testing** | pytest | 8.0+ | Framework de testing unitario |
| **Análisis** | numpy | 2.0+ | Cálculos numéricos para gráficos |

### Requisitos de Infraestructura

- **Python 3.13** o superior
- **MySQL Server 8.0** o compatible (MariaDB 10.5+)
- **4GB RAM** mínimo para operación normal
- **500MB** espacio en disco para instalación base
- **Windows 7+**, **Linux** o **macOS 10.14+**

---

## Estructura de Archivos

```
PCelMedic-python/
|-- main.py                          # Punto de entrada de la aplicacion
|-- requirements.txt                 # Dependencias del proyecto
|-- .gitignore                       # Archivos ignorados por Git
|-- .configAdmin                     # Credenciales del administrador (no versionado)
|
|-- GUI/                             # Capa de presentacion (Tkinter)
|   |-- VentanaPrincipal.py          # Ventana principal con navegacion
|   |-- VentanaRegistro.py           # Registro de clientes y dispositivos
|   |-- VentanaReparacion.py         # Gestion de reparaciones
|   |-- VentanaFactura.py            # Generacion de facturas
|   |-- VentanaGarantia.py           # Vista general de garantias
|   |-- VentanaEntradaGarantia.py    # Entrada de garantias
|   |-- VentanaSalidaGarantia.py     # Salida/cierre de garantias
|   +-- VentanaFinanzas.py           # Panel de analisis financiero
|
|-- Logica/                          # Capa de logica de negocio
|   |-- LogicaCliente.py             # Validaciones de cliente
|   |-- LogicaDispositivo.py         # Validaciones de dispositivo
|   |-- LogicaReparacion.py          # Validaciones de reparacion
|   |-- LogicaFactura.py             # Logica de facturacion
|   |-- LogicaGarantia.py            # Validaciones de garantia
|   +-- GeneradorPDF.py              # Generacion de reportes PDF
|
|-- DAO/                             # Capa de acceso a datos
|   |-- ClienteDAO.py                # CRUD de clientes
|   |-- DispositivoDAO.py            # CRUD de dispositivos
|   |-- ReparacionDAO.py             # CRUD de reparaciones
|   |-- FacturasDAO.py               # CRUD de facturas
|   +-- GarantiaDAO.py               # CRUD de garantias
|
|-- Modelo/                          # Entidades del dominio
|   |-- ModeloCliente.py             # Modelo de cliente
|   |-- ModeloDispositivo.py         # Modelo de dispositivo
|   |-- ModeloReparacion.py          # Modelo de reparacion
|   |-- ModeloFactura.py             # Modelo de factura
|   +-- ModeloGarantia.py            # Modelo de garantia
|
|-- Utilidades/                      # Modulos de soporte
|   |-- Conexion.py                  # Singleton de conexion MySQL
|   |-- TransaccionConexion.py       # Context manager para transacciones
|   |-- Validador.py                 # Validaciones genericas reutilizables
|   |-- ManejadorPassword.py         # Hash y verificacion bcrypt
|   +-- EncriptarConfigAdmin.py      # Script para encriptar credenciales
|
|-- Reportes/                        # Reportes PDF generados
|   |-- Orden_*.pdf
|   |-- Factura_*.pdf
|   +-- Garantia_*.pdf
|
+-- tests/                           # Pruebas unitarias
    |-- test_logica_cliente.py
    |-- test_logica_reparacion.py
    |-- test_logica_garantia.py
    +-- test_validador_precio.py
|
+-- pcelmedic_database.sql          # Script SQL de inicialización
|-- .gitignore                       # Archivos ignorados por Git
|-- requirements.txt                 # Dependencias del proyecto
+-- setup.py (opcional)              # Configuración para packaging
```

---

## Configuracion Avanzada

### Optimización de Base de Datos

Para mejor rendimiento en producción:

```sql
-- Analizar tablas y actualizar estadísticas
ANALYZE TABLE clientes, dispositivos, reparaciones, facturas, garantias;

-- Optimizar tablas fragmentadas
OPTIMIZE TABLE clientes, dispositivos, reparaciones, facturas, garantias;

-- Ver configuración actual
SHOW VARIABLES LIKE '%buffer%';
```

### Variables de Entorno (Opcional)

Crear archivo `.env` para mayor seguridad:

```bash
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=tu_contrasena
DB_NAME=pcelmedic_db
LOG_LEVEL=INFO
```

---

## Solucion de Problemas

### Problema: "Access denied for user"

**Solución**:
```bash
# Verificar usuario MySQL está creado
mysql -h localhost -u root -p

mysql> CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_password';
mysql> GRANT ALL PRIVILEGES ON pcelmedic_db.* TO 'tu_usuario'@'localhost';
mysql> FLUSH PRIVILEGES;
```

### Problema: "No module named 'mysql'"

**Solución**:
```bash
# Reinstalar el driver MySQL
pip install --upgrade mysql-connector-python
```

### Problema: "Tkinter not installed"

**Solución en Ubuntu/Debian**:
```bash
sudo apt-get install python3-tk python3-dev
```

**En Windows**: Tkinter viene incluido con Python. Si tienes problemas, reinstala Python incluyendo Tkinter.

---

## Contribuciones y Reporte de Bugs

### Reportar un error

1. Abre un issue en GitHub con descripción detallada
2. Incluye la versión de Python, Sistema Operativo y pasos para reproducir
3. Adjunta archivos de log si es necesario (carpeta `Reportes/` sin datos sensibles)

### Contribuir código

1. Haz fork del repositorio
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Asegúrate que los tests pasen: `pytest tests/ -v`
4. Commit con mensajes descriptivos: `git commit -m "Agregar nueva funcionalidad"`
5. Push a la rama: `git push origin feature/nueva-funcionalidad`
6. Abre un Pull Request con descripción clara

### Estándares de código

- Seguir **PEP 8** para estilo de código
- Incluir docstrings en funciones públicas
- Escribir tests para funcionalidad nueva
- Usar type hints cuando sea posible

---

## Roadmap (Próximas Versiones)

### v1.1 (Q2 2026)
- [ ] API REST para integración con sistemas externos
- [ ] Soporte para múltiples sedes/sucursales
- [ ] Dashboard web complementario
- [ ] Integración con WhatsApp para notificaciones

### v1.2 (Q3 2026)
- [ ] Sincronización en la nube (AWS S3 / Azure Blob)
- [ ] Soporte para múltiples idiomas
- [ ] Catálogo de repuestos con inventario
- [ ] Generación de reportes automáticos vía email

### v2.0 (2027)
- [ ] Migración a arquitectura microservicios
- [ ] Aplicación móvil (Flutter/React Native)
- [ ] Machine Learning para predicción de fallos

---

## Licencia

Este proyecto está bajo licencia **Privada**. Todos los derechos reservados © 2026 PCelMedic.

Para información sobre permisos de uso comercial, contactar a: `parcerazo@gmail.com`

---

## Contacto y Soporte

- **Documentación**: [Wiki del Proyecto](https://github.com/Cesarpato92/PCelMedic-python/wiki)
- **Issues**: [GitHub Issues](https://github.com/Cesarpato92/PCelMedic-python/issues)
- **Email**: `parcerazo@gmail.com`

---<p align="center">
  &copy; 2026 <strong>PCelMedic</strong> — Eficiencia y transparencia en tu servicio tecnico.
</p>
