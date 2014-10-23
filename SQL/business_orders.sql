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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `cust_id` smallint(5) unsigned DEFAULT NULL,
  `product_id` smallint(5) unsigned DEFAULT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_type` varchar(50) DEFAULT NULL,
  `price` float(10,2) unsigned DEFAULT NULL,
  `quantity` smallint(5) unsigned DEFAULT NULL,
  `date_submit` varchar(30) DEFAULT NULL,
  `paid` enum('YES','NO') DEFAULT NULL,
  KEY `cust_id` (`cust_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `users` (`cust_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (9,5,'1GB DDR3 Ram','COMPUTER MEMORIES',20.00,1,'10-30-2011 at 12:07AM','YES'),(9,3,'32gb SanDisk usb flash drive','USB FLASH DRIVE',30.00,2,'10-30-2011 at 12:19AM','YES'),(2,3,'32gb SanDisk usb flash drive','USB FLASH DRIVE',30.00,1,'10-30-2011 at 06:20PM','NO'),(2,1,'32gb HP usb flash drive','USB FLASH DRIVE',30.00,10,'10-30-2011 at 07:37PM','NO'),(9,6,'Razor Optical Mouse','KEYBOARD & MICE',22.50,10,'11-02-2011 at 11:36AM','YES'),(9,5,'1GB DDR3 Ram','COMPUTER MEMORIES',20.00,2,'11-02-2011 at 11:43AM','YES'),(9,31,'32gb ipod touch','APPLE',299.99,1,'12-07-2011 at 07:03PM','YES');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-01-07 19:25:12
