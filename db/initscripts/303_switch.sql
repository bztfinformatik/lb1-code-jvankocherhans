
USE `classicmodels`;

DROP TABLE IF EXISTS `switch`;

CREATE TABLE `switch` (
  `hostname` varchar(50) NOT NULL,
  `ip` varchar(16) NOT NULL,
  `switchType` varchar(50),
  PRIMARY KEY (`hostname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO switch VALUES ("ac-sw-p01", "10.128.250.253", "Catalyst 3560"); 