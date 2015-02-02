/**
 * Main JavaScript
 * Site Name
 *
 * Copyright (c) 2015. by Way2CU, http://way2cu.com
 * Authors:
 */

var Caracal = Caracal || {};


/**
 * Check if site is being displayed on mobile.
 * @return boolean
 */
Caracal.is_mobile = function() {
	// make sure variable cache exists
	Caracal.variable_cache = Caracal.variable_cache || {};

	// check for cached value
	if ('mobile_version' in Caracal.variable_cache) {
		var result = Caracal.variable_cache['mobile_version'];

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
		Caracal.variable_cache['mobile_version'] = result;
	}

	return result;
};

/**
 * Function called when document and images have been completely loaded.
 */
Caracal.on_site_load = function() {
};


// connect document `load` event with handler function
$(Caracal.on_site_load);
