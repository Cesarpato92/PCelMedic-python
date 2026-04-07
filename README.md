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

## Tabla de Contenidos

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

- **Registro de clientes y dispositivos** con validacion completa de datos (cedula, email, celular, nombre).
- **Control del ciclo de reparacion** con estados: *En Proceso*, *Completada*, *Entregada*.
- **Facturacion automatica** vinculada a las reparaciones realizadas.
- **Gestion de garantias** con flujo de entrada y salida, seguimiento de estados y observaciones.
- **Panel financiero** con graficos dinamicos (Matplotlib) y exportacion a Excel (.xlsx).
- **Generacion de reportes en PDF**: ordenes de reparacion, recibos de garantia y facturas.
- **Autenticacion de administrador** con contrasenas encriptadas mediante bcrypt.
- **Transacciones seguras** con soporte para commit/rollback automatico via context manager.

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
|         Utilidades (Soporte)            |  Conexion BD, validadores,
|  Conexion, TransaccionConexion          |  encriptacion
|  Validador, ManejadorPassword           |
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

# Activar en Windows (PowerShell / CMD)
.venv\Scripts\activate

# Activar en Linux / macOS
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> **Nota:** El archivo `requirements.txt` incluye todas las librerias necesarias: `mysql-connector-python`, `matplotlib`, `fpdf`, `openpyxl`, `bcrypt`, `tkcalendar`, `pillow`, entre otras.

---

## Configuracion de la Base de Datos

1. Accede a tu servidor MySQL y crea la base de datos:

   ```sql
   CREATE DATABASE pcelmedic;
   ```

2. Edita las credenciales de conexion en `Utilidades/Conexion.py`:

   ```python
   __port = 3306
   __host = "localhost"
   __user = "tu_usuario"
   __password = "tu_password"
   __database = "pcelmedic"
   ```

3. Crea las tablas necesarias. El sistema utiliza las siguientes tablas:

   | Tabla | Descripcion |
   |-------|-------------|
   | `cliente` | Datos de clientes (cedula, nombre, email, celular) |
   | `dispositivo` | Dispositivos vinculados a clientes (id_dispositivo, marca, version, tipo de reparacion, tipo_contrasena, contrasena, comentarios, referencia a cliente) |
   | `reparacion` | Registro de reparaciones (id_reparacion, fecha_ingreso, estado, costo_repuesto, precio_reparacion, comentarios, referencia a dispositivo) |
   | `factura` | Facturas generadas (id_factura, fecha, total, referencia a reparacion) |
   | `garantia` | Garantias (id_garantia, estado, observaciones, fecha_inicio, fecha_fin, precio_insumos, comentarios finales, referencia a reparacion) |

---

## Configuracion del Administrador

El acceso al modulo de **Finanzas** requiere autenticacion. Las credenciales se almacenan en un archivo `.configAdmin` en la raiz del proyecto con el siguiente formato:

```
USER=admin
PASSWORD=<hash_bcrypt>
```

Para encriptar una contrasena en texto plano, ejecuta:

```bash
python Utilidades/EncriptarConfigAdmin.py
```

Este script:
1. Lee la contrasena actual del archivo `.configAdmin`.
2. Genera un hash bcrypt (12 rounds).
3. Crea un backup (`.configAdmin.backup`).
4. Sobrescribe el archivo con la contrasena encriptada.

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

El proyecto incluye pruebas unitarias con **pytest**. Los tests se ubican en la carpeta `tests/` y cubren las validaciones de la capa de logica de negocio:

```bash
# Ejecutar todas las pruebas
pytest tests/ -v

# Ejecutar un test especifico
pytest tests/test_logica_cliente.py -v
```

### Tests disponibles

| Archivo | Cobertura |
|---------|-----------|
| `test_logica_cliente.py` | Validacion de cedula, email, nombre y celular. |
| `test_logica_reparacion.py` | Validacion de datos y estados de reparacion. |
| `test_logica_garantia.py` | Validacion de campos y estados de garantia. |
| `test_validador_precio.py` | Validacion de precios (numeros positivos). |

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.13** | Lenguaje principal |
| **Tkinter / ttk** | Interfaz grafica de escritorio |
| **MySQL** | Base de datos relacional |
| **mysql-connector-python** | Driver de conexion a MySQL |
| **Matplotlib** | Graficos y visualizaciones financieras |
| **fpdf** | Generacion de reportes PDF |
| **openpyxl** | Exportacion de datos a Excel (.xlsx) |
| **bcrypt** | Encriptacion de contrasenas |
| **tkcalendar** | Selectores de fecha en la GUI |
| **Pillow** | Procesamiento de imagenes |
| **pytest** | Framework de testing |
| **numpy** | Calculos para graficos de barras |

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
```

---

<p align="center">
  &copy; 2026 <strong>PCelMedic</strong> — Eficiencia y transparencia en tu servicio tecnico.
</p>
