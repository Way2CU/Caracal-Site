#!/usr/bin/env python
#
#	Password Store Integration
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

import os
import sys
import user

from subprocess import Popen, PIPE

PASSWORD_SIZE = 20
REPOSITORY_PATH = os.path.join(user.home, '.password-store', 'Way2CU')

# prepare environment
PASS_ENVIRONMENT = os.environ.copy()
PASS_ENVIRONMENT.update({
		'PASSWORD_STORE_DIR': REPOSITORY_PATH,
		'TERM': 'vt220'
	})

if 'LS_COLORS' in PASS_ENVIRONMENT:
	del PASS_ENVIRONMENT['LS_COLORS']


def pull_repository_passwords():
	"""Pull password repository and merge changes if needed."""
	# create process and wait for it to end
	try:
		process = Popen(['git', 'pull', '--commit', 'origin'], cwd=REPOSITORY_PATH, stdout=PIPE)
		process.wait()

	except OSError:
		sys.exit(1)

def push_passwords_repository():
	"""Push changes to password repository."""
	# create process and wait for it to end
	try:
		process = Popen(['git', 'push', 'origin'], cwd=REPOSITORY_PATH, stdout=PIPE)
		process.wait()

	except OSError:
		sys.exit(1)

def generate_password(path):
	"""Generate new password for specified domain."""
	result = ''

	# create and communicate with process
	try:
		process = Popen(['pass', 'generate', '-n', path, str(PASSWORD_SIZE)], env=PASS_ENVIRONMENT, stdout=PIPE)
		output = process.communicate()

	except OSError:
		sys.exit(1)

	# We have to do this since password store prints color codes regardless of
	# terminal configuration, thus causing problems with storing password.
	#
	# else:
	# 	data = output[0].splitlines()
	# 	if len(data) >= 2:
	# 		result = data[-1]

	# 	else:
	# 		sys.exit(1)

	# temporary fix with getting right password
	return retrieve_password(path)

def retrieve_password(path):
	"""Retrieve password for specified domain."""
	result = ''

	# create and communicate with process
	try:
		process = Popen(['pass', 'show', path], env=PASS_ENVIRONMENT, stdout=PIPE)
		output = process.communicate()

	except OSError:
		sys.exit(1)

	else:
		result = output[0]

	return result

def get_password(domain, file_name, subdomain):
	"""Create new or retrieve existing password from storage."""
	if subdomain is not None and file_name != 'System':
		# generate path with subdomain
		path = os.path.join('Domains', '{0}.{1}'.format(subdomain, domain), file_name)

	else:
		# generate regular path with only domain
		path = os.path.join('Domains', domain, file_name)

	# make sure repository is up to date
	pull_repository_passwords()

	# get password
	if os.path.exists(os.path.join(REPOSITORY_PATH, '{0}.gpg'.format(path))):
		# get exsiting password
		result = retrieve_password(path)

	else:
		# generate new password
		result = generate_password(path)
		push_passwords_repository()

	return result


if __name__ == '__main__':
	if len(sys.argv) < 3:
		sys.exit(2)

	# get existing or generate new password
	if len(sys.argv) == 3:
		subdomain = None
		domain, file_name = sys.argv[1:]

	else:
		subdomain, domain, file_name = sys.argv[1:4]

	sys.stdout.write(get_password(domain, file_name, subdomain))
	sys.stdout.flush()
	sys.exit(0)
