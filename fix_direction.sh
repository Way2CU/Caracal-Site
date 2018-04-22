#!/bin/bash
#
#	This script fixes old style of RTL support done through body class `rtl` with
#	new way of doing things where we assign `dir` attribute to `html` tag.

find -type f -iname '*.css' -print -exec sed -i 's/body.rtl/html[dir=rtl]/g' {} \;
find -type f -iname '*.less' -print -exec sed -i 's/body.rtl/html[dir=rtl]/g' {} \;

find -type f -iname '*.xml' -print -exec sed -i "s/<html[^>]*>/<html lang=\"\$language\" dir=\"\$language_rtl ? 'rtl' : 'ltr'\" cms:eval=\"lang,dir\">/g" {} \;
find -type f -iname '*.xml' -print -exec sed -i "s/<body[^>]*>/<body>/g" {} \;
