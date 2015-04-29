<?php

/**
 * Site Configuration File
 *
 * This file overrides properties defined in main configuration
 * file for Caracal located in `units/config.php`.
 */

use Core\Cache\Type as CacheType;

// document standard
define('_STANDARD', 'html5');
define('_TIMEZONE', '{{ timezone }}');

define('DEBUG', 1);
// define('SQL_DEBUG', 1);

// site language configuration
$available_languages = array('en');
$default_language = 'en';

// default session options
$session_type = Session::TYPE_BROWSER;

// database
$db_use = true;
$db_type = DatabaseType::MYSQL;
$db_config = array(
		'host' => '{{ database.host }}',
		'user' => '{{ database.username }}',
		'pass' => '{{ database.password }}',
		'name' => '{{ database.name }}'
	);

// configure code generation
$cache_method = CacheType::NONE;
$optimize_code = false;
$url_rewrite = true;

?>
