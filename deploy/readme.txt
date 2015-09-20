This is configuration for Ansible deployment tool. Site specific configuration
is located in "group_vars/all" under "site" dictionary. By default site is deployed
to all "web-servers" group.

To deploy a site type:
ansible-playbook -i path/to/inventory deploy.yml

Please note this deployment script assumes it will be used for deployment of single
domain or subdomain. If you wish to have more than one subdomain on single subscription
multiple repositories and deployment scripts are required.
