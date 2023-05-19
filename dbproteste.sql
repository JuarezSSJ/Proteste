-- MySQL Script generated by MySQL Workbench
-- Wed May 10 20:18:22 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema db_proteste
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_proteste
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_proteste` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_proteste` ;

-- -----------------------------------------------------
-- Table `db_proteste`.`tb_login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_login` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `login` VARCHAR(45) NULL DEFAULT NULL,
  `senha` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `cpf` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `login` (`login` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_plano`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_plano` (
  `create_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `update_at` TIMESTAMP NULL DEFAULT NULL,
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `id_login` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_login` (`id_login` ASC) VISIBLE,
  CONSTRAINT `id_login`
    FOREIGN KEY (`id_login`)
    REFERENCES `db_proteste`.`tb_login` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_casoteste`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_casoteste` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `fase_desenvolvimento` VARCHAR(255) NULL DEFAULT NULL,
  `fase_teste` VARCHAR(255) NULL DEFAULT NULL,
  `id_plano` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_plano` (`id_plano` ASC) VISIBLE,
  CONSTRAINT `tb_casoteste_ibfk_1`
    FOREIGN KEY (`id_plano`)
    REFERENCES `db_proteste`.`tb_plano` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_abordagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_abordagem` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descrição` VARCHAR(255) NULL DEFAULT NULL,
  `id_caso` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_caso` (`id_caso` ASC) VISIBLE,
  CONSTRAINT `tb_abordagem_ibfk_1`
    FOREIGN KEY (`id_caso`)
    REFERENCES `db_proteste`.`tb_casoteste` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_artefatos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_artefatos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `entrada` VARCHAR(255) NOT NULL,
  `saida` VARCHAR(255) NOT NULL,
  `id_caso` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_caso` (`id_caso` ASC) VISIBLE,
  CONSTRAINT `tb_artefatos_ibfk_1`
    FOREIGN KEY (`id_caso`)
    REFERENCES `db_proteste`.`tb_casoteste` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_projeto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_projeto` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `requisitante` VARCHAR(45) NOT NULL,
  `gerente_projeto` VARCHAR(45) NOT NULL,
  `id_plano` INT(11) NOT NULL,
  `cenario_operacional` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_plano` (`id_plano` ASC) VISIBLE,
  CONSTRAINT `id_plano`
    FOREIGN KEY (`id_plano`)
    REFERENCES `db_proteste`.`tb_plano` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_marcos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_marcos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descrição` VARCHAR(255) NOT NULL,
  `id_projeto` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_marco_projeto` (`id_projeto` ASC) VISIBLE,
  CONSTRAINT `fk_marco_projeto`
    FOREIGN KEY (`id_projeto`)
    REFERENCES `db_proteste`.`tb_projeto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_premissas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_premissas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descrição` VARCHAR(255) NOT NULL,
  `id_plano` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tb_premissas_tb_plano` (`id_plano` ASC) VISIBLE,
  CONSTRAINT `fk_tb_premissas_tb_plano`
    FOREIGN KEY (`id_plano`)
    REFERENCES `db_proteste`.`tb_plano` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_recursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_recursos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `tipo_recurso` INT(11) NOT NULL,
  `quantidade` INT(11) NOT NULL,
  `descricao` VARCHAR(255) NULL DEFAULT NULL,
  `id_projeto` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Id_projeto` (`id_projeto` ASC) VISIBLE,
  CONSTRAINT `Id_projeto`
    FOREIGN KEY (`id_projeto`)
    REFERENCES `db_proteste`.`tb_projeto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_recursoshumanos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_recursoshumanos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `papel` VARCHAR(45) NOT NULL,
  `responsabilidade` VARCHAR(255) NULL DEFAULT NULL,
  `id_projeto` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Id_projeto_recursoshumanos` (`id_projeto` ASC) VISIBLE,
  CONSTRAINT `Id_projeto_recursoshumanos`
    FOREIGN KEY (`id_projeto`)
    REFERENCES `db_proteste`.`tb_projeto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_relatorios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_relatorios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `tipo_relatorio` VARCHAR(45) NOT NULL,
  `objetivo` VARCHAR(100) NOT NULL,
  `destinatario` VARCHAR(45) NOT NULL,
  `periodicidade` VARCHAR(45) NOT NULL,
  `id_projeto` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_relatorios_projeto` (`id_projeto` ASC) VISIBLE,
  CONSTRAINT `fk_relatorios_projeto`
    FOREIGN KEY (`id_projeto`)
    REFERENCES `db_proteste`.`tb_projeto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_restricoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_restricoes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descrição` VARCHAR(255) NULL DEFAULT NULL,
  `id_plano` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_plano` (`id_plano` ASC) VISIBLE,
  CONSTRAINT `tb_restricoes_ibfk_1`
    FOREIGN KEY (`id_plano`)
    REFERENCES `db_proteste`.`tb_plano` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `db_proteste`.`tb_riscos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_proteste`.`tb_riscos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descrição` VARCHAR(255) NOT NULL,
  `id_projeto` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_risco_projeto` (`id_projeto` ASC) VISIBLE,
  CONSTRAINT `fk_risco_projeto`
    FOREIGN KEY (`id_projeto`)
    REFERENCES `db_proteste`.`tb_projeto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
