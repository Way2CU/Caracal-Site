# Caracal Site - Development Environment
#
# Copyright © 2014. Way2CU. All Rights Reserved.
# Author: Mladen Mijatov

Vagrant.configure('2') do |config|
	config.vm.box = 'hashicorp/precise32'

	# install web server and required components
	config.vm.provision :shell, :path => 'bootstrap.sh', run:'once'

	config.vm.synced_folder './data', '/var/www/data', create:true

	# configure network
	config.vm.network :forwarded_port, host:8080, guest:80
end
