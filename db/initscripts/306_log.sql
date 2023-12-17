USE `arpaconda`;

DROP TABLE IF EXISTS `log`;

CREATE TABLE `log` (
  `logEvent` longtext,
  `date` date
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO log VALUES ("random event", "2023-12-08");
INSERT INTO log VALUES ("random event", "2023-11-08"); 