USE `arpaconda`;

DROP TABLE IF EXISTS `client`;

CREATE TABLE `client` (
  `mac` varchar(18) NOT NULL,
  `hostname` varchar(50),
  PRIMARY KEY (`mac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO client VALUES ("37-FE-00-EE-CC-A4", "drucker1");
INSERT INTO client VALUES ("AD-E7-EE-5D-AF-2B", "drucker1"); 