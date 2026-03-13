# PCelMedic - Sistema de Gestión para Taller de Celulares

PCelMedic es una solución profesional de escritorio desarrollada en Python y Tkinter, diseñada específicamente para optimizar el flujo de trabajo en talleres de servicio técnico de dispositivos móviles.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.13** o superior.
- **MySQL Server** (8.0 recomendado).
- Un gestor de bases de datos como **MySQL Workbench** o **DBeaver**.

---

##  Instalación 

Sigue estos pasos para poner en marcha el sistema en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Cesarpato92/PCelMedic-python.git
cd PCelMedic-python
```

### 2. Configurar el Entorno Virtual
Es altamente recomendable usar un entorno virtual para evitar conflictos de dependencias:
```bash
# Crear entorno
python -m venv .venv

# Activar en Windows (PowerShell/CMD)
.venv\Scripts\activate

# Activar en Linux/macOS
source .venv/bin/activate
```

### 3. Instalar Dependencias
Instala todas las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
1. Accede a tu servidor MySQL.
2. Crea una base de datos (ej: `pcelmedic_db`).
3. Localiza el archivo `Utilidades/Conexion.py` y actualiza las credenciales:
   ```python
   self.config = {
       'host': 'localhost',
       'user': 'tu_usuario',
       'password': 'tu_password',
       'database': 'pcelmedic_db'
   }
   ```
4. Asegúrate de ejecutar el script SQL de creación de tablas (si se proporciona) o verificar que los DAOs tengan las tablas correspondientes.

---

## 🛠️ Guía de Uso por Módulos

El sistema está dividido en módulos accesibles desde la ventana principal:

### 👤 Gestión de Clientes y Dispositivos (`VentanaRegistro`)
- **Registro de Clientes:** Captura datos como nombre, cédula, email y celular.
- **Registro de Dispositivos:** Vincula dispositivos a clientes, registrando marca, modelo, tipo de reparación solicitada y contraseñas de acceso (PIN, Patrón, etc.).

### 🔧 Control de Reparaciones (`VentanaReparacion`)
- Permite gestionar el ciclo de vida de una reparación.
- Registro de diagnósticos técnicos.
- Gestión de repuestos utilizados y mano de obra.
- Cambio de estados (En espera, En proceso, Terminado).

### 🧾 Facturación (`VentanaFactura`)
- Generación automática de facturas basadas en los servicios realizados.
- Calcula totales incluyendo repuestos y servicios técnicos.
- Opción de impresión o generación de PDF.

### 🛡️ Gestión de Garantías (`VentanaEntradaGarantia` / `VentanaSalidaGarantia`)
- **Entrada:** Registro de dispositivos que regresan por fallas cubiertas por la garantía.
- **Salida:** Seguimiento del proceso de resolución de la garantía y entrega final al cliente.
- Historial detallado de observaciones y estados.

### 📊 Análisis Financiero (`VentanaFinanzas`)
- **Gráficos Dinámicos:** Visualización de ventas vs. costos de repuestos mediante Matplotlib.
- **Rango de Fechas:** Filtra estadísticas por períodos específicos.
- **Exportación:** Genera reportes detallados en Excel (.xlsx) para contabilidad externa.

---

## 📂 Estructura del Código

- **`GUI/`**: Interfaz visual (Tkinter). Separación de ventanas por funcionalidad.
- **`Logica/`**: Reglas de negocio y validación de datos antes de ir a la BD.
- **`DAO/`**: (Data Access Objects) Consultas SQL puras aisladas de la lógica.
- **`Modelo/`**: Clases que representan los objetos del sistema (Cliente, Factura, etc.).
- **`Utilidades/`**: Scripts de conexión, encriptación y validadores genéricos.

---

## 🛠️ Comandos Útiles

- **Ejecutar App:** `python main.py`
- **Actualizar Requerimientos:** `pip freeze > requirements.txt`

---
© 2026 PCelMedic - Eficiencia y transparencia en tu servicio técnico.
