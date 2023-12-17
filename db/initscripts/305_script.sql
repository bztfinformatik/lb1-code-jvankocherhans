USE `arpaconda`;

DROP TABLE IF EXISTS `script`;

CREATE TABLE `script` (
  `scriptID` int NOT NULL AUTO_INCREMENT,
  `scriptName` varchar(50),
  `scriptContent` longtext,
  PRIMARY KEY (`scriptID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;