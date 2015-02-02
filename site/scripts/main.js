/**
 * Main JavaScript
 * Site Name
 *
 * Copyright (c) 2015. by Way2CU, http://way2cu.com
 * Authors:
 */

var Site = Site || {};


/**
 * Check if site is being displayed on mobile.
 * @return boolean
 */
Site.is_mobile = function() {
	// make sure variable cache exists
	Site.variable_cache = Site.variable_cache || {};

	// check for cached value
	if ('mobile_version' in Site.variable_cache) {
		var result = Site.variable_cache['mobile_version'];

	} else {
		// detect if site is mobile
		var result = false;
		var elements = document.getElementsByName('viewport');

		// check all tags and find `meta`
		for (var i=0, count=elements.length; i<count; i++) {
			var tag = elements[i];

			if (tag.tagName == 'META') {
				result = true;
				break;
			}
		}

		// cache value so next time we are faster
		Site.variable_cache['mobile_version'] = result;
	}

	return result;
};

/**
 * Function called when document and images have been completely loaded.
 */
Site.on_load = function() {
};


// connect document `load` event with handler function
$(Site.on_load);
