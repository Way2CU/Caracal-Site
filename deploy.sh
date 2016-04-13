#!/bin/bash
cd deploy

if [ -f "hosts.txt" ]; then
	ansible-playbook --limit @hosts.txt deploy.yml
else
	echo 'Missing "hosts" file.'
fi
