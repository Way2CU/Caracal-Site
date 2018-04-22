#!/bin/bash

# make sure we are not asked any questions
export DEBIAN_FRONTEND=noninteractive

# update repository information
apt-get -y update

# prepare answers for prompts
echo mysql-server-5.5 mysql-server/root_password password caracal | debconf-set-selections
echo mysql-server-5.5 mysql-server/root_password_again password caracal | debconf-set-selections
echo phpmyadmin phpmyadmin/dbconfig-install boolean true | debconf-set-selections
echo phpmyadmin phpmyadmin/mysql/admin-pass password caracal | debconf-set-selections
echo phpmyadmin phpmyadmin/mysql/app-pass password caracal | debconf-set-selections
echo phpmyadmin phpmyadmin/app-password-confirm password caracal | debconf-set-selections
echo phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2 | debconf-set-selections

# install database server first
apt-get -y install mysql-server memcached

# install the remaining part of the server stack
apt-get -y install phpmyadmin libapache2-mod-php5 php5-curl php5-memcached git

# clone caracal repository
rm -f /var/www/html/index.html
git clone --recursive https://github.com/Way2CU/Caracal.git /var/www/html
git checkout master

# link directories
ln -s /vagrant /var/www/html/site
