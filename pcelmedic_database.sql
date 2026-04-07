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
-- TABLA: auditoria_cambios (Opcional - para tracking de cambios)
-- Descripción: Registro de auditoría de cambios importantes en el sistema
-- ============================================================================
CREATE TABLE IF NOT EXISTS `auditoria_cambios` (
  `id_auditoria` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único del registro de auditoría',
  `tabla` VARCHAR(50) NOT NULL COMMENT 'Tabla afectada',
  `tipo_operacion` ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL COMMENT 'Tipo de operación realizada',
  `id_registro` INT NOT NULL COMMENT 'ID del registro afectado',
  `datos_anteriores` LONGTEXT COMMENT 'Datos antes del cambio (JSON)',
  `datos_nuevos` LONGTEXT COMMENT 'Datos después del cambio (JSON)',
  `fecha_cambio` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha y hora del cambio',
  `usuario` VARCHAR(100) COMMENT 'Usuario que realizó el cambio',
  
  INDEX `idx_tabla` (`tabla`) COMMENT 'Índice para búsqueda por tabla',
  INDEX `idx_fecha_cambio` (`fecha_cambio`) COMMENT 'Índice para búsqueda por fecha'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
COMMENT='Registro de auditoría de cambios en el sistema';

-- ============================================================================
-- VISTAS ÚTILES
-- ============================================================================

-- Vista: Resumen de reparaciones activas
CREATE OR REPLACE VIEW `v_reparaciones_activas` AS
SELECT 
  r.id_reparacion,
  c.nombre AS nombre_cliente,
  c.cedula,
  d.marca,
  d.modelo,
  d.tipo_reparacion,
  r.fecha_ingreso,
  r.estado,
  r.precio_reparacion,
  r.costo_repuestos,
  (r.precio_reparacion + r.costo_repuestos) AS total_reparacion
FROM reparaciones r
JOIN dispositivos d ON r.id_dispositivo = d.id_dispositivo
JOIN clientes c ON d.id_cliente = c.id_cliente
WHERE r.estado IN ('En Proceso', 'Completada')
ORDER BY r.fecha_ingreso DESC;

-- Vista: Resumen financiero por fecha
CREATE OR REPLACE VIEW `v_resumen_financiero` AS
SELECT 
  CAST(f.fecha AS CHAR(10)) AS fecha,
  COUNT(DISTINCT f.id_factura) AS cantidad_facturas,
  SUM(f.subtotal) AS ingresos_repuestos,
  SUM(CASE WHEN r.costo_repuestos > 0 THEN r.costo_repuestos ELSE 0 END) AS costos_repuestos,
  SUM(f.total) AS total_ingresos,
  SUM(f.total) - SUM(CASE WHEN r.costo_repuestos > 0 THEN r.costo_repuestos ELSE 0 END) AS ganancia_neta
FROM facturas f
JOIN reparaciones r ON f.id_reparacion = r.id_reparacion
WHERE CAST(f.fecha AS CHAR(10)) >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY fecha
ORDER BY fecha DESC;

-- Vista: Garantías pendientes por vencer
CREATE OR REPLACE VIEW `v_garantias_por_vencer` AS
SELECT 
  g.id_garantia,
  c.nombre AS nombre_cliente,
  c.cedula,
  d.marca,
  r.fecha_completacion,
  g.fecha_fin,
  DATEDIFF(g.fecha_fin, CURDATE()) AS dias_restantes,
  g.estado
FROM garantias g
JOIN reparaciones r ON g.id_reparacion = r.id_reparacion
JOIN dispositivos d ON r.id_dispositivo = d.id_dispositivo
JOIN clientes c ON d.id_cliente = c.id_cliente
WHERE g.estado = 'En Garantía' 
  AND g.fecha_fin >= CURDATE()
  AND g.fecha_fin <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
ORDER BY g.fecha_fin ASC;

-- ============================================================================
-- PROCEDIMIENTOS ALMACENADOS
-- ============================================================================

-- Procedimiento: Finalizar reparación y crear factura
DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS `sp_completar_reparacion`(
  IN p_id_reparacion INT,
  IN p_precio_reparacion DECIMAL(10,2),
  IN p_costo_repuestos DECIMAL(10,2)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al completar la reparación';
  END;
  
  START TRANSACTION;
  
  -- Actualizar estado de reparación
  UPDATE reparaciones 
  SET estado = 'Completada', 
      fecha_completacion = CURDATE(),
      precio_reparacion = p_precio_reparacion,
      costo_repuestos = p_costo_repuestos
  WHERE id_reparacion = p_id_reparacion;
  
  -- Crear factura automática
  INSERT INTO facturas (id_reparacion, fecha, subtotal, total, estado_pago)
  VALUES (
    p_id_reparacion, 
    CURDATE(), 
    p_precio_reparacion + p_costo_repuestos,
    p_precio_reparacion + p_costo_repuestos,
    'Pendiente'
  );
  
  COMMIT;
END$$

DELIMITER ;

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================
-- Nota: Este script crea la estructura completa de la base de datos.
-- Para ejecutar: mysql -u usuario -p < pcelmedic_database.sql
-- ============================================================================
