#!/usr/bin/env python
#
#	Username Generation
#	Copyright (c) 2015. by Way2CU, http://way2cu.com
#	Author: Mladen Mijatov
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import hashlib

from base64 import b64encode as encode

USERNAME_SIZE = 16


def get_username(domain, subdomain=None):
	"""Generate username based on provided data."""
	hash_function = hashlib.new('md5')  # safe to use, we are not using it for security

	# add content for hash generation
	if subdomain is not None:
		hash_function.update(subdomain)
	hash_function.update(domain)

	return encode(hash_function.digest(), '-_')[:USERNAME_SIZE]


if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(2)

	# get data
	if len(sys.argv) == 3:
		subdomain, domain = sys.argv[1:]

	else:
		domain = sys.argv[1]
		subdomain = None

	sys.stdout.write(get_username(domain, subdomain))
	sys.stdout.flush()
	sys.exit(0)
