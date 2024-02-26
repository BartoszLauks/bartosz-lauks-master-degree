-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: bartosz-lauks-master-degree_dev
-- ------------------------------------------------------
-- Server version	5.7.42

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
-- Table structure for table `chat_messages`
--

DROP TABLE IF EXISTS `chat_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `body` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `updated_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `uuid` binary(16) NOT NULL COMMENT '(DC2Type:uuid)',
  PRIMARY KEY (`id`),
  KEY `IDX_EF20C9A6A76ED395` (`user_id`),
  KEY `IDX_EF20C9A61E5D0459` (`test_id`),
  CONSTRAINT `FK_EF20C9A61E5D0459` FOREIGN KEY (`test_id`) REFERENCES `test` (`id`),
  CONSTRAINT `FK_EF20C9A6A76ED395` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_messages`
--

LOCK TABLES `chat_messages` WRITE;
/*!40000 ALTER TABLE `chat_messages` DISABLE KEYS */;
INSERT INTO `chat_messages` VALUES (2,8,276,'test chat','2024-02-26 07:49:50','2024-02-26 07:49:50',_binary 'ç\‰d9ÅsÈî†\ÿ4üîS\n');
/*!40000 ALTER TABLE `chat_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `computational_complexity`
--

DROP TABLE IF EXISTS `computational_complexity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `computational_complexity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `algorithm` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `language` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `time_complexity` double NOT NULL,
  `memory_complexity` int(11) NOT NULL,
  `created_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `updated_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computational_complexity`
--

LOCK TABLES `computational_complexity` WRITE;
/*!40000 ALTER TABLE `computational_complexity` DISABLE KEYS */;
/*!40000 ALTER TABLE `computational_complexity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctrine_migration_versions`
--

DROP TABLE IF EXISTS `doctrine_migration_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctrine_migration_versions` (
  `version` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  `executed_at` datetime DEFAULT NULL,
  `execution_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctrine_migration_versions`
--

LOCK TABLES `doctrine_migration_versions` WRITE;
/*!40000 ALTER TABLE `doctrine_migration_versions` DISABLE KEYS */;
INSERT INTO `doctrine_migration_versions` VALUES ('DoctrineMigrations\\Version20230908085054','2023-09-08 09:30:37',9),('DoctrineMigrations\\Version20230912121508','2023-09-12 12:15:16',47),('DoctrineMigrations\\Version20231103203635','2023-11-03 20:36:47',28),('DoctrineMigrations\\Version20231103205632','2023-11-03 20:57:00',48),('DoctrineMigrations\\Version20231122111111','2023-11-22 11:14:01',40),('DoctrineMigrations\\Version20231218173913','2023-12-18 17:40:46',133),('DoctrineMigrations\\Version20231219100513','2023-12-19 10:05:39',45),('DoctrineMigrations\\Version20231222153608','2023-12-22 15:37:15',35),('DoctrineMigrations\\Version20231229172843','2023-12-29 17:29:35',50),('DoctrineMigrations\\Version20240106212641','2024-01-06 21:28:42',50),('DoctrineMigrations\\Version20240106232431','2024-01-06 23:25:05',99),('DoctrineMigrations\\Version20240110134204','2024-01-10 13:43:19',11);
/*!40000 ALTER TABLE `doctrine_migration_versions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender`
--

DROP TABLE IF EXISTS `gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gender` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `updated_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
INSERT INTO `gender` VALUES (1,'Man','2023-12-18 18:54:20','2023-12-18 18:54:20'),(2,'Female','2023-12-18 18:54:20','2023-12-18 18:54:20');
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reset_password_request`
--

DROP TABLE IF EXISTS `reset_password_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reset_password_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `selector` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hashed_token` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `requested_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `expires_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  PRIMARY KEY (`id`),
  KEY `IDX_7CE748AA76ED395` (`user_id`),
  CONSTRAINT `FK_7CE748AA76ED395` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reset_password_request`
--

LOCK TABLES `reset_password_request` WRITE;
/*!40000 ALTER TABLE `reset_password_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `reset_password_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `algorithm` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `result` int(11) NOT NULL,
  `response` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `language` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `uuid` binary(16) NOT NULL COMMENT '(DC2Type:uuid)',
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `updated_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  PRIMARY KEY (`id`),
  KEY `IDX_D87F7E0CA76ED395` (`user_id`),
  CONSTRAINT `FK_D87F7E0CA76ED395` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=278 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (264,8,'DFS','Main & Computational complexity','VERIFIED',3744,'Testing completed successfully.','PYTHON',_binary 'çGˇùê•∂Ω#˝\“\Î`','OrUPLQxE8aYkk1xHwZGErliguhRzkZ1C','2024-01-26 18:29:48','2024-01-26 18:32:09'),(265,8,'Dijkstra','Main & Computational complexity','VERIFIED',5536,'Testing completed successfully.','PYTHON',_binary 'çG®èvÃí\›XΩÄE˛\‰','0bHampZQPRxS6tvWJVX8I7FawKw7Dgu5','2024-01-26 18:35:59','2024-01-26 18:36:48'),(268,8,'Kruskal','Main & Computational complexity','VERIFIED',21256,'Testing completed successfully.','PYTHON',_binary 'çG˘µsÓ¥•π}x¥∫∞','5QM0wyHjLA6oLJ9a1r7Wk43kk843zTro','2024-01-26 18:53:48','2024-01-26 18:54:27'),(269,8,'Prim','Main & Computational complexity','VERIFIED',23192,'Testing completed successfully.','PYTHON',_binary 'çG%\\r7èT!ïq\»)','J5D0kryDNSYqqfguGphWpdCMebqbA3Mc','2024-01-26 19:00:31','2024-01-26 19:00:44'),(271,8,'TopologicalSorting','Main & Computational complexity','VERIFIED',28144,'Testing completed successfully.','PYTHON',_binary 'çG.ò\Ãr€Æ\‘p!±¡µ','iMTQTJSzxnFvY3p3N02BfcJH0YRBHZpr','2024-01-26 19:10:52','2024-01-26 19:11:10'),(272,8,'BellmanFord','Main & Computational complexity','VERIFIED',1304,'Testing completed successfully.','PYTHON',_binary 'çG4XDzg¨ˆGH;mm','z4cCkt55xXxfk2zFkRtxf2sIS4xAsIwC','2024-01-26 19:17:09','2024-01-26 19:19:42'),(273,8,'FloydWarshall','Main & Computational complexity','VERIFIED',3944,'Testing completed successfully.','PYTHON',_binary 'çGÆ\„q\Ì®:Mc\…\r\Ê','dOosulj6R9b98cOoDMABixLwQL2Pwkfs','2024-01-26 21:31:00','2024-01-26 21:32:55'),(274,8,'Johnson','Main & Computational complexity','VERIFIED',36592,'Testing completed successfully.','PYTHON',_binary 'çGπFu0¨é3åÒcÚ','1mDaafzH7UgmgD5U36dgD3jJeuEdDJGQ','2024-01-26 21:42:20','2024-01-26 21:44:24'),(275,8,'Fleury','Main & Computational complexity','VERIFIED',1232,'Testing completed successfully.','PYTHON',_binary 'çGø~3t]ê\0â\ÁΩM/','b986wtnrhcgHlXyoQ4xvkwELCvF2kdh0','2024-01-26 21:49:08','2024-01-26 21:49:57'),(276,8,'BFS','Main & Computational complexity','VERIFIED',1936,'Testing completed successfully.','PYTHON',_binary 'ç\‹Aåhvıì†\·\0\€H','veKDsjCEbmVFjWdsvaktGIiRIb2T15Sg','2024-02-24 17:54:59','2024-02-24 17:57:44');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(180) COLLATE utf8mb4_unicode_ci NOT NULL,
  `roles` json NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `uuid` binary(16) NOT NULL COMMENT '(DC2Type:uuid)',
  `gender_id` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `updated_at` datetime NOT NULL COMMENT '(DC2Type:datetime_immutable)',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `surname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNIQ_8D93D649E7927C74` (`email`),
  KEY `IDX_8D93D649708A0E0` (`gender_id`),
  CONSTRAINT `FK_8D93D649708A0E0` FOREIGN KEY (`gender_id`) REFERENCES `gender` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (8,'cruzonek@gmail.com','[\"ROLE_ADMIN\"]','$2y$13$2DiBxvGUTcq99wsviIeDI.bPplRZ66QuiJ5G/f7qpO6ThonAsdAmK',1,_binary 'ãñ˛Û@|ßÑíIï6\Õ',1,'0000-00-00 00:00:00','2024-01-26 22:50:03','Bartosz','Lauks'),(12,'bartosz.lauks@interia.pl','[]','$2y$13$HMHRelmnx44iPumw.B8qg.7X4IicmlBE27EQjC2kxeAwEaDDoTVmG',1,_binary 'å∂™6\œz€í›æ\'\»@',2,'2023-12-29 17:40:57','2023-12-29 17:41:09','Bartosz','Lauks');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-26  7:55:50
