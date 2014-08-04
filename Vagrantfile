# Caracal Site - Development Environment
#
# Copyright © 2014. Way2CU. All Rights Reserved.
# Author: Mladen Mijatov

Vagrant.configure('2') do |config|
	config.vm.box = 'Caracal'
	config.vm.box_url = 'hashicorp/precise32'

	# directories to synchronize
	config.vm.synced_folder './data', '/var/www/data', create:true
	config.vm.synced_folder './images', '/var/www/images', create:true
	config.vm.synced_folder './styles', '/var/www/styles', create:true
	config.vm.synced_folder './site', '/var/www/site', create:true

	# configure network
	config.vm.network :forwarded_port, host:8080, guest:80
end
