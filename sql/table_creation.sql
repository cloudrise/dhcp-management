SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `clients` (
`id` int(11) NOT NULL,
`first_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`last_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`ip` int(10) unsigned NOT NULL,
`mac` binary(6) NOT NULL,
`is_active` BOOLEAN NOT NULL DEFAULT true,
`room` int(11) DEFAULT 0,
`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
`last_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


ALTER TABLE `clients` ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `mac` (`mac`), ADD UNIQUE KEY `ip` (`ip`);

ALTER TABLE `clients` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;