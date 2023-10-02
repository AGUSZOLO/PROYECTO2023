-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SALUDTEST333
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SALUDTEST333
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SALUDTEST333` DEFAULT CHARACTER SET utf8 ;
USE `SALUDTEST333` ;

-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Usuario` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Contraseña` VARCHAR(45) NULL,
  `Correo_elec` VARCHAR(45) NULL,
  `Direccion` VARCHAR(45) NULL,
  `Fecha_regis` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Carrito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Carrito` (
  `cart_id` INT NOT NULL AUTO_INCREMENT,
  `Usuario_user_id` INT NOT NULL,
  `Fecha_creacion` VARCHAR(45) NULL,
  `Estado` VARCHAR(45) NULL,
  PRIMARY KEY (`cart_id`, `Usuario_user_id`),
  INDEX `fk_Carrtio_Usuario_idx` (`Usuario_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Carrtio_Usuario`
    FOREIGN KEY (`Usuario_user_id`)
    REFERENCES `SALUDTEST333`.`Usuario` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Producto` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Precio` INT NULL,
  `Descripcion` VARCHAR(45) NULL,
  `Estado` VARCHAR(45) NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Categoria` (
  `categoria_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`categoria_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Compra` (
  `compra_id` INT NOT NULL AUTO_INCREMENT,
  `Usuario_user_id` INT NOT NULL,
  `Fecha_compra` VARCHAR(45) NULL,
  `Total` INT NULL,
  `Cantidad` INT NULL,
  PRIMARY KEY (`compra_id`, `Usuario_user_id`),
  INDEX `fk_Compra_Usuario1_idx` (`Usuario_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Compra_Usuario1`
    FOREIGN KEY (`Usuario_user_id`)
    REFERENCES `SALUDTEST333`.`Usuario` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Valoracion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Valoracion` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `Usuario_user_id` INT NOT NULL,
  `Producto_product_id` INT NOT NULL,
  `Puntuacion` VARCHAR(45) NULL,
  `Fecha` VARCHAR(45) NULL,
  PRIMARY KEY (`rating_id`, `Usuario_user_id`, `Producto_product_id`),
  INDEX `fk_Valoracion_Usuario1_idx` (`Usuario_user_id` ASC) VISIBLE,
  INDEX `fk_Valoracion_Producto1_idx` (`Producto_product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Valoracion_Usuario1`
    FOREIGN KEY (`Usuario_user_id`)
    REFERENCES `SALUDTEST333`.`Usuario` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Valoracion_Producto1`
    FOREIGN KEY (`Producto_product_id`)
    REFERENCES `SALUDTEST333`.`Producto` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Comentarios` (
  `comentario_id` INT NOT NULL AUTO_INCREMENT,
  `Usuario_user_id` INT NOT NULL,
  `Producto_product_id` INT NOT NULL,
  `Fecha_comen` VARCHAR(45) NULL,
  `Puntuacion_comen` VARCHAR(45) NULL,
  PRIMARY KEY (`comentario_id`, `Usuario_user_id`, `Producto_product_id`),
  INDEX `fk_Comentarios_Usuario1_idx` (`Usuario_user_id` ASC) VISIBLE,
  INDEX `fk_Comentarios_Producto1_idx` (`Producto_product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Comentarios_Usuario1`
    FOREIGN KEY (`Usuario_user_id`)
    REFERENCES `SALUDTEST333`.`Usuario` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comentarios_Producto1`
    FOREIGN KEY (`Producto_product_id`)
    REFERENCES `SALUDTEST333`.`Producto` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Categoria_has_Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Categoria_has_Producto` (
  `Categoria_categoria_id` INT NOT NULL AUTO_INCREMENT,
  `Producto_product_id` INT NOT NULL,
  PRIMARY KEY (`Categoria_categoria_id`, `Producto_product_id`),
  INDEX `fk_Categoria_has_Producto_Producto1_idx` (`Producto_product_id` ASC) VISIBLE,
  INDEX `fk_Categoria_has_Producto_Categoria1_idx` (`Categoria_categoria_id` ASC) VISIBLE,
  CONSTRAINT `fk_Categoria_has_Producto_Categoria1`
    FOREIGN KEY (`Categoria_categoria_id`)
    REFERENCES `SALUDTEST333`.`Categoria` (`categoria_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Categoria_has_Producto_Producto1`
    FOREIGN KEY (`Producto_product_id`)
    REFERENCES `SALUDTEST333`.`Producto` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SALUDTEST333`.`Carrito_has_Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SALUDTEST333`.`Carrito_has_Producto` (
  `Carrtio_cart_id` INT NOT NULL AUTO_INCREMENT,
  `Carrtio_Usuario_user_id` INT NOT NULL,
  `Producto_product_id` INT NOT NULL,
  PRIMARY KEY (`Carrtio_cart_id`, `Carrtio_Usuario_user_id`, `Producto_product_id`),
  INDEX `fk_Carrtio_has_Producto_Producto1_idx` (`Producto_product_id` ASC) VISIBLE,
  INDEX `fk_Carrtio_has_Producto_Carrtio1_idx` (`Carrtio_cart_id` ASC, `Carrtio_Usuario_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Carrtio_has_Producto_Carrtio1`
    FOREIGN KEY (`Carrtio_cart_id` , `Carrtio_Usuario_user_id`)
    REFERENCES `SALUDTEST333`.`Carrito` (`cart_id` , `Usuario_user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Carrtio_has_Producto_Producto1`
    FOREIGN KEY (`Producto_product_id`)
    REFERENCES `SALUDTEST333`.`Producto` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
