CREATE DATABASE gestionempresarial;
USE gestionempresarial;

CREATE USER 'gestionempresarial'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'gestionempresarial'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON `gestionempresarial`.* TO 'gestionempresarial'@'localhost';

CREATE TABLE `gestionempresarial`.`clientes` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , `telefono` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

INSERT INTO `clientes` (`Identificador`, `nombre`, `email`, `telefono`) VALUES (NULL, 'Jose Vicente', 'info@josevicente.com', '64566');
INSERT INTO `clientes` (`Identificador`, `nombre`, `email`, `telefono`) VALUES (NULL, 'Juan', 'info@juan.com', '2345325');
INSERT INTO `clientes` (`Identificador`, `nombre`, `email`, `telefono`) VALUES (NULL, 'Jorge', 'info@jorge.com', '52345');

CREATE TABLE `gestionempresarial`.`productos` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `descripcion` VARCHAR(255) NOT NULL , `precio` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

CREATE TABLE `gestionempresarial`.`pedidos` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `fecha` DATE NOT NULL , `clientes_nombre` INT(255) NOT NULL , `productos_nombre` INT(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

CREATE TABLE `gestionempresarial`.`categorias` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;