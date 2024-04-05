-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2024 at 08:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `did` int(11) NOT NULL,
  `dname` varchar(30) NOT NULL,
  `ddob` varchar(50) NOT NULL,
  `dnum` varchar(50) NOT NULL,
  `dspe` varchar(100) NOT NULL,
  `dsalary` int(11) NOT NULL,
  `dexp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`did`, `dname`, `ddob`, `dnum`, `dspe`, `dsalary`, `dexp`) VALUES
(1, 'CHIRAG', '13/04/2004', '7567062405', 'CARDIO', 100000, 4),
(2, 'YASVI', '11/09/2005', '9988774455', 'MBBS', 25000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `paitent`
--

CREATE TABLE `paitent` (
  `id` int(11) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pdob` varchar(50) NOT NULL,
  `pnum` bigint(20) NOT NULL,
  `pd` varchar(100) NOT NULL,
  `dname` varchar(50) NOT NULL,
  `pf` bigint(20) NOT NULL,
  `ppa` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paitent`
--

INSERT INTO `paitent` (`id`, `pname`, `pdob`, `pnum`, `pd`, `dname`, `pf`, `ppa`) VALUES
(6, 'Yasvi', '11/09/2005', 123456789, 'hdg', 'Dr.HENIL SUTARIYA', 100, 0),
(7, 'Kavya Gosalia', '21/05/2004', 1122334455, 'Headache', 'Dr.YASVI VAGHASIYA', 1000, 500),
(8, 'Henil ', '12/11/2004', 1122334455, 'Headache', 'Dr.EKALKUMAR SORATHIYA', 500, 400),
(9, 'Chirag', '13/04/2004', 9879094180, 'Stomachahce', 'Dr.KAVYA GOSALIA', 1000, 0),
(10, 'Ekal', '12/12/1221', 9879094180, 'Fever', 'Dr.YASVI VAGHASIYA', 1000, 770);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `paitent`
--
ALTER TABLE `paitent`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `paitent`
--
ALTER TABLE `paitent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
