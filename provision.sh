#!/bin/bash

# add mirrors for faster download
cat >/tmp/sources.list <<EOL
deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted universe multiverse
EOL

cat /etc/apt/sources.list >> /tmp/sources.list
mv /tmp/sources.list /etc/apt/sources.list

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
apt-get -y install phpmyadmin libapache2-mod-php5 php5-curl php5-memcached git python-pip

# install tailon, retry 4 times, pip has a bug
pip install tailon
pip install tailon
pip install tailon
pip install tailon

cat >/etc/init/tailon.conf <<EOL
description	"Tailon Service"
author		"Mladen Mijatov <mladen@way2cu.com>"

start on runlevel [2345]
stop on starting rc RUNLEVEL=[016]

exec /usr/local/bin/tailon \
-b :8080 \
-f /var/log/apache2/error.log /var/log/apache2/access.log
EOL

service tailon start

# fix broken sendfile support in VBox
cd /etc/apache2/sites-enabled
sed -i '/ServerAdmin/a EnableSendfile off' 000-default
sed -i '0,/AllowOverride/! s/AllowOverride None/AllowOverride All/' 000-default

# load additional apache modules
cd /etc/apache2/mods-enabled
ln -s ../mods-available/headers.load
ln -s ../mods-available/rewrite.load

# apply apache changes
service apache2 restart

# clone caracal repository
cd /var/www
rm -Rf *
git clone --recursive https://github.com/Way2CU/Caracal.git .
git checkout master

# link directories
ln -s /vagrant /var/www/site
