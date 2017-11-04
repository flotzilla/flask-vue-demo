-- Adminer 4.3.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `ticket_booking`;
CREATE DATABASE `ticket_booking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `ticket_booking`;

DROP TABLE IF EXISTS `genre`;
CREATE TABLE `genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `poster_url` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float NOT NULL,
  `duration` int(11) NOT NULL,
  `session_start` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `session_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `movie` (`id`, `name`, `description`, `poster_url`, `price`, `duration`, `session_start`, `session_date`) VALUES
(1,	'Pulp Fiction',	'Vincent Vega (John Travolta) and Jules Winnfield (Samuel L. Jackson) are hitmen with a penchant for philosophical discussions. In this ultra-hip, multi-strand crime movie, their storyline is interwoven with those of their boss, gangster Marsellus Wallace (Ving Rhames) ; his actress wife, Mia (Uma Thurman) ; struggling boxer Butch Coolidge (Bruce Willis) ; master fixer Winston Wolfe (Harvey Keitel) and a nervous pair of armed robbers, \"Pumpkin\" (Tim Roth) and \"Honey Bunny\" (Amanda Plummer).',	'pulp.jpeg',	12.5,	120,	'2017-11-04 06:10:50',	'0000-00-00 00:00:00'),
(2,	'The Shawshank Redemption ',	' Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. ',	'shaw.jpg',	0,	140,	'2017-11-04 06:33:07',	'2017-11-04 03:08:27'),
(3,	'The Godfather',	' The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. ',	'godfather.jpg',	12,	180,	'2017-11-04 06:11:26',	'0000-00-00 00:00:00'),
(4,	'The Dark Knigh',	' When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice. ',	'batman.jpg',	10,	160,	'2017-11-04 06:11:38',	'0000-00-00 00:00:00'),
(5,	'Fight Club',	' An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more. ',	'fight.jpg',	8,	140,	'2017-11-04 06:11:50',	'0000-00-00 00:00:00'),
(6,	'Forrest Gump',	' JFK, LBJ, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75. ',	'forest.jpg',	10,	180,	'2017-11-04 06:11:59',	'0000-00-00 00:00:00');

DROP TABLE IF EXISTS `movie_genre`;
CREATE TABLE `movie_genre` (
  `movie_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  KEY `genre_id` (`genre_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `movie_genre_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`),
  CONSTRAINT `movie_genre_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- 2017-11-04 13:16:24