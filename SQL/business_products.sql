CREATE DATABASE  IF NOT EXISTS `business` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `business`;
-- MySQL dump 10.13  Distrib 5.5.9, for Win32 (x86)
--
-- Host: localhost    Database: business
-- ------------------------------------------------------
-- Server version	5.5.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `product_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) DEFAULT NULL,
  `item_type` varchar(50) DEFAULT NULL,
  `price` float(10,2) unsigned DEFAULT NULL,
  `quantity` smallint(6) DEFAULT NULL,
  `in_stock` enum('yes','no') DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'32gb HP usb flash drive','USB FLASH DRIVE',30.00,10,'yes'),(2,'32gb Kingston usb flash drive','USB FLASH DRIVE',25.00,20,'yes'),(3,'32gb SanDisk usb flash drive','USB FLASH DRIVE',30.00,12,'yes'),(4,'Tenda 10/100/1000Mbps Gigabit Ethernet PCI Card','NETWORKING MODEM',10.00,3,'yes'),(5,'1GB DDR3 Ram','COMPUTER MEMORIES',20.00,11,'yes'),(6,'Razor Optical Mouse','KEYBOARD & MICE',22.50,40,'yes'),(7,'12MP Sony CyberShot','DIGITAL CAMERAS',122.50,38,'yes'),(13,'14MP Sony CyberShot','DIGITAL CAMERAS',150.50,12,'yes'),(14,'14MP Canon','DIGITAL CAMERAS',100.00,30,'yes'),(15,'12MP Olympus','DIGITAL CAMERAS',90.25,30,'yes'),(16,'12MP FujiFilm X10 Digital Cam','DIGITAL CAMERAS',110.00,10,'yes'),(17,'18MP Nikon Black Camera','DIGITAL CAMERAS',399.99,5,'yes'),(18,'HP Photosmart 5510','PRINTERS',119.20,50,'yes'),(19,'HP Officejet 6000','PRINTERS',100.10,25,'yes'),(20,'HP DeskJet Wireless Printer','PRINTERS',130.00,30,'yes'),(21,'HP Officejet 4500','PRINTERS',125.99,10,'yes'),(22,'Lexmark X2670','PRINTERS',140.00,5,'yes'),(23,'Lexmark All-in-One Printer','PRINTERS',150.00,20,'yes'),(24,'Lexmark E206D Laser Printer','PRINTERS',299.99,15,'yes'),(25,'Canon MX410','PRINTERS',130.00,24,'yes'),(26,'Canon MG5320','PRINTERS',130.00,25,'yes'),(27,'Optoma Pico Projector','PROJECTORS',200.00,10,'yes'),(28,'Vivitek Projector','PROJECTORS',299.99,10,'yes'),(29,'Eptoma Home Theater Projector','PROJECTORS',299.99,10,'yes'),(30,'Vivitek HD Projector','PROJECTORS',350.10,10,'yes'),(31,'32gb ipod touch','APPLE',299.99,3,'yes');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-01-07 19:25:13
