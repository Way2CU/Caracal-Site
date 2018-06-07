<?php

/**
 * Site Configuration File
 *
 * This file overrides properties defined in main configuration
 * file for Caracal located in `units/config.php`.
 */

use Core\CSP;
use Core\CORS\Manager as CORS;
use Core\Cache\Type as CacheType;
use Core\Session\Type as SessionType;

// document standard
define('_TIMEZONE', 'America/New_York');

define('DEBUG', 1);
// define('SQL_DEBUG', 1);

// site language configuration
$available_languages = array('en');
$default_language = 'en';

// default session options
$session_type = SessionType::BROWSER;

// database
$db_type = DatabaseType::MYSQL;
$db_config = array(
		'host' => 'localhost',
		'user' => 'root',
		'pass' => 'caracal',
		'name' => 'web_engine'
	);

// allow loading scripts from different domain
/* CSP\Parser::add_value(CSP\Element::SCRIPTS, 'domain.com'); */

// allow cross-domain resource sharing
/* $domain = CORS::add_domain('*'); */
/* CORS::allow_methods($domain, array('GET')); */

// configure code generation
$cache_method = CacheType::NONE;
$optimize_code = false;
$include_styles = true;
$url_rewrite = true;

?>
