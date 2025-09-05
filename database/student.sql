-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: face_recognizer
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Dep` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Dob` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Teacher` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','03','Akshay kumar','G','23B81A05BZ','MALE','11/12/2006','akshay@gmail.com','7330998484','Warangal','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','05','Ahmed Jilani','G','23B81A05CB','MALE','14/08/2004','ahmed@gmail.com','8688774623','khammam','Dr. S.Srinivasulu','No'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','06','Balaji','G','23B81A05CC','MALE','11/01/2003','balaji@gmail.com','6301077524','Khammam','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','09','Charan','G','23B81A05CF','MALE','23/05/2005','charan@gmail.com','6307776612','Hyderabad','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','29','Praveen','G','23B81A05DB','MALE','11/12/2005','praveen@gmail.com','7330123484','Warangal','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','30','Rakshith reddy','G','23B81A05DC','MALE','18/12/2004','rakshith@gmail.com','9000123456','Warangal','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','34','Rishith','G','23B81A05DG','MALE','04/08/2004','rishith@gmail.com','9871235671','Hyderabad','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','35','Rohitash kumar','G','23B81A05DH','MALE','11/01/2004','rohit@gmail.com','6301057524','Hyderabad','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','48','CNU','G','23B81A05DW','MALE','24/08/2005','cnu@gmail.com','9871235878','Kurnool','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','55','Tharun patnayak','G','23B81A05EE','MALE','10/02/2005','tharun@gmail.com','9390375756','Mahabubabad','Dr. S.Srinivasulu','Yes'),('Computer Science and Enginnering','B-Tech','2024-2025','Semester-2','59','Viduran Reddy','G','23B81A05EJ','MALE','01/01/2000','svr@gmail.com','8019321408','Hyderabad','Dr. S.Srinivasulu','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-23 22:37:24
