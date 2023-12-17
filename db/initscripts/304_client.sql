USE `arpaconda`;

DROP TABLE IF EXISTS `client`;

CREATE TABLE `client` (
  `mac` varchar(18) NOT NULL,
  `hostname` varchar(50),
  PRIMARY KEY (`mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
