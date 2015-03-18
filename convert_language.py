#!/usr/bin/env python
#
# Language Conversion Script
#
# Copyright (c) 2015. Way2CU. All Rights Reserved.
# Author: Mladen Mijatov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from xml.dom import minidom as xml
from json.encoder import JSONEncoder


encoder_options = {
			'skipkeys': True,
			'check_circular': True,
			'sort_keys': True,
			'indent': 4,
			'ensure_ascii': False,
			'encoding': 'utf8'
		}

# load original language file
if len(sys.argv) > 1:
	language_path = os.path.dirname(sys.argv[1])
	language_file = xml.parse(sys.argv[1])

else:
	language_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'site', 'data')
	language_file = xml.parse(os.path.join(language_path, 'language.xml'))

# get all languages
output = {}
for language in language_file.getElementsByTagName('language'):
	code = language.attributes['short'].value
	output[code] = {}

	for constant in language.getElementsByTagName('constant'):
		constant_name = constant.attributes['name'].value

		if constant.firstChild:
			output[code][constant_name] = constant.firstChild.data

		else:
			output[code][constant_name] = ''

# save output files
encoder = JSONEncoder(**encoder_options)

for code, language in output.items():
	with open(os.path.join(language_path, 'language_{0}.json'.format(code)), 'w') as raw_file:
		raw_file.write(encoder.encode(language).encode('utf8'))
