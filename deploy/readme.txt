This is configuration for Ansible deployment tool. Site specific configuration
is located in "group_vars/all" under "site" dictionary. Deployment script expects
hosts.txt file to exist. This file contains list of destination servers to deploy
site to.

To deploy a site type execute script called `deploy.sh` in root of this repostiory.

Please note this deployment script assumes it will be used for deployment of single
domain or subdomain. If you wish to have more than one subdomain on single subscription
multiple repositories and deployment scripts are required.
