USE `arpaconda`;

DROP TABLE IF EXISTS `log`;

CREATE TABLE `log` (
  `logEvent` longtext,
  `date` date
) ENGINE=InnoDB DEFAULT CHARSET=latin1;