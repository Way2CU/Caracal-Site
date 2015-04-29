This is configuration for Ansible deployment tool. Site specific configuration
is located in "group_vars/all" under "site" dictionary. By default site is deployed
to all "web-servers" group.

To deploy a site type:
ansible-playbook -i path/to/inventory deploy.yml
