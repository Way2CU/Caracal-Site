#!/bin/bash

# change working directory
cd deploy

# check if all the tasks are marked as done
tasks=`grep "\[ \]" ../Checklist.md | wc -l`
if [ "$tasks" -ne 0 ]; then
	echo 'Checklist is not complete! Aborting deployment.'
	exit 1
fi

# make sure target hosts are defined
if [ ! -f "hosts.txt" ]; then
	echo 'Missing "hosts" file. Aborting deployment.'
	exit 2
fi

ansible-playbook --limit @hosts.txt deploy.yml &
