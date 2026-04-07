-- ============================================================================
-- PCelMedic - Script de Creación de Base de Datos
-- Gestión Integral para Taller de Reparación de Dispositivos Móviles
-- ============================================================================
-- Autor: Equipo de Desarrollo PCelMedic
-- Versión: 1.0
-- Fecha: 2026
-- Descripción: Script SQL para inicializar la base de datos con todas las
--              tablas, índices y restricciones necesarias.
-- ============================================================================

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS `pcelmedic_db` 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE `pcelmedic_db`;

-- ============================================================================
-- TABLA: clientes
-- Descripción: Almacena información de los clientes del taller
-- ============================================================================
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único del cliente',
  `cedula` VARCHAR(20) NOT NULL UNIQUE COMMENT 'Cédula de identidad del cliente',
  `nombre` VARCHAR(100) NOT NULL COMMENT 'Nombre completo del cliente',
  `email` VARCHAR(100) NOT NULL UNIQUE COMMENT 'Correo electrónico del cliente',
  `celular` VARCHAR(20) NOT NULL COMMENT 'Número de celular del cliente',
  `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro del cliente',
  `estado` ENUM('Activo', 'Inactivo') DEFAULT 'Activo' COMMENT 'Estado del cliente',
  
  INDEX `idx_cedula` (`cedula`) COMMENT 'Índice para búsqueda rápida por cédula',
  INDEX `idx_nombre` (`nombre`) COMMENT 'Índice para búsqueda por nombre',
  INDEX `idx_fecha_registro` (`fecha_registro`) COMMENT 'Índice para búsqueda por fecha de registro'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de clientes del taller';

-- ============================================================================
-- TABLA: dispositivos
-- Descripción: Almacena dispositivos registrados por los clientes
-- ============================================================================
CREATE TABLE IF NOT EXISTS `dispositivos` (
  `id_dispositivo` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único del dispositivo',
  `id_cliente` INT NOT NULL COMMENT 'Referencia al cliente propietario',
  `marca` VARCHAR(50) NOT NULL COMMENT 'Marca del dispositivo (Samsung, iPhone, Huawei, etc.)',
  `modelo` VARCHAR(50) COMMENT 'Modelo específico del dispositivo',
  `tipo_reparacion` VARCHAR(100) NOT NULL COMMENT 'Tipo de reparación: pantalla, batería, software, etc.',
  `tipo_password` VARCHAR(50) COMMENT 'Tipo de contraseña: PIN, Patrón, Texto, Biométrico, etc.',
  `password` VARCHAR(255) COMMENT 'Contraseña de acceso al dispositivo',
  `comentarios` LONGTEXT COMMENT 'Observaciones y detalles adicionales del dispositivo',
  `version` INT DEFAULT 0 COMMENT 'Versión del registro (para control de cambios)',
  `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro del dispositivo',
  `activo` BOOLEAN DEFAULT TRUE COMMENT 'Indica si el dispositivo está activo',
  
  CONSTRAINT `fk_dispositivos_cliente` 
    FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id_cliente`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  
  INDEX `idx_id_cliente` (`id_cliente`) COMMENT 'Índice para búsqueda por cliente',
  INDEX `idx_marca` (`marca`) COMMENT 'Índice para búsqueda por marca',
  INDEX `idx_tipo_reparacion` (`tipo_reparacion`) COMMENT 'Índice para búsqueda por tipo de reparación'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de dispositivos de los clientes';

-- ============================================================================
-- TABLA: reparaciones
-- Descripción: Registro del ciclo de vida de las reparaciones
-- ============================================================================
CREATE TABLE IF NOT EXISTS `reparaciones` (
  `id_reparacion` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único de la reparación',
  `id_dispositivo` INT NOT NULL COMMENT 'Referencia al dispositivo siendo reparado',
  `fecha_ingreso` DATE NOT NULL COMMENT 'Fecha en que ingresa el dispositivo a reparación',
  `estado` ENUM('En Proceso', 'Completada', 'Entregada') DEFAULT 'En Proceso' 
    COMMENT 'Estado actual de la reparación',
  `diagnostico` LONGTEXT COMMENT 'Diagnóstico técnico del problema',
  `costo_repuestos` DECIMAL(10, 2) DEFAULT 0.00 COMMENT 'Costo total de los repuestos utilizados',
  `precio_reparacion` DECIMAL(10, 2) NOT NULL COMMENT 'Precio del servicio técnico',
  `comentarios` LONGTEXT COMMENT 'Notas adicionales sobre la reparación',
  `fecha_completacion` DATE COMMENT 'Fecha cuando se completó la reparación',
  `fecha_entrega` DATE COMMENT 'Fecha cuando se entregó el dispositivo',
  
  CONSTRAINT `fk_reparaciones_dispositivo` 
    FOREIGN KEY (`id_dispositivo`) REFERENCES `dispositivos`(`id_dispositivo`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  
  INDEX `idx_id_dispositivo` (`id_dispositivo`) COMMENT 'Índice para búsqueda por dispositivo',
  INDEX `idx_estado` (`estado`) COMMENT 'Índice para filtrar por estado',
  INDEX `idx_fecha_ingreso` (`fecha_ingreso`) COMMENT 'Índice para búsqueda por fecha de ingreso'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de reparaciones realizadas';

-- ============================================================================
-- TABLA: facturas
-- Descripción: Facturas emitidas basadas en reparaciones completadas
-- ============================================================================
CREATE TABLE IF NOT EXISTS `facturas` (
  `id_factura` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único de la factura',
  `id_reparacion` INT NOT NULL UNIQUE COMMENT 'Referencia a la reparación facturada',
  `fecha` DATE NOT NULL COMMENT 'Fecha de emisión de la factura',
  `subtotal` DECIMAL(10, 2) NOT NULL COMMENT 'Subtotal (repuestos + servicio)',
  `impuesto` DECIMAL(10, 2) DEFAULT 0.00 COMMENT 'Monto de impuestos',
  `total` DECIMAL(10, 2) NOT NULL COMMENT 'Total a pagar',
  `estado_pago` ENUM('Pendiente', 'Pagada', 'Cancelada') DEFAULT 'Pendiente' 
    COMMENT 'Estado del pago de la factura',
  `fecha_pago` DATE COMMENT 'Fecha cuando se realizó el pago',
  `comentarios` LONGTEXT COMMENT 'Notas adicionales sobre la factura',
  
  CONSTRAINT `fk_facturas_reparacion` 
    FOREIGN KEY (`id_reparacion`) REFERENCES `reparaciones`(`id_reparacion`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  
  INDEX `idx_id_reparacion` (`id_reparacion`) COMMENT 'Índice para búsqueda por reparación',
  INDEX `idx_fecha` (`fecha`) COMMENT 'Índice para búsqueda por fecha',
  INDEX `idx_estado_pago` (`estado_pago`) COMMENT 'Índice para filtrar por estado de pago'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de facturas emitidas';

-- ============================================================================
-- TABLA: garantias
-- Descripción: Gestión de garantías de reparaciones
-- ============================================================================
CREATE TABLE IF NOT EXISTS `garantias` (
  `id_garantia` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único de la garantía',
  `id_reparacion` INT NOT NULL COMMENT 'Referencia a la reparación que tiene garantía',
  `fecha_inicio` DATE NOT NULL COMMENT 'Fecha de inicio de la garantía',
  `fecha_fin` DATE NOT NULL COMMENT 'Fecha de vencimiento de la garantía',
  `estado` ENUM('En Garantía', 'Completada', 'Rechazada') DEFAULT 'En Garantía' 
    COMMENT 'Estado actual de la garantía',
  `observaciones` LONGTEXT COMMENT 'Observaciones sobre la falla cubierta por garantía',
  `precio_insumos` DECIMAL(10, 2) DEFAULT 0.00 COMMENT 'Costo de insumos para reparación en garantía',
  `comentarios_finales` LONGTEXT COMMENT 'Comentarios finales al cierre de la garantía',
  `fecha_cierre` DATE COMMENT 'Fecha cuando se cierre la garantía',
  
  CONSTRAINT `fk_garantias_reparacion` 
    FOREIGN KEY (`id_reparacion`) REFERENCES `reparaciones`(`id_reparacion`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  
  INDEX `idx_id_reparacion` (`id_reparacion`) COMMENT 'Índice para búsqueda por reparación',
  INDEX `idx_estado` (`estado`) COMMENT 'Índice para filtrar por estado',
  INDEX `idx_fecha_inicio` (`fecha_inicio`) COMMENT 'Índice para búsqueda por fecha de inicio',
  INDEX `idx_fecha_fin` (`fecha_fin`) COMMENT 'Índice para búsqueda por fecha de vencimiento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de garantías de reparaciones';

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================
-- Nota: Este script crea la estructura completa de la base de datos.
-- Para ejecutar: mysql -u usuario -p < pcelmedic_database.sql
-- ============================================================================
