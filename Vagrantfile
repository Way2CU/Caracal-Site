# Caracal Site - Development Environment
#
# Copyright © 2014. Way2CU. All Rights Reserved.
# Author: Mladen Mijatov

Vagrant.configure('2') do |config|
	config.vm.box = 'hashicorp/precise32'

	# customize virtual machine
	config.vm.provider 'virtualbox' do |vm|
		# name our machine for easier management
		path = File.dirname(__FILE__)
		name = File.basename(path)

		if name == 'Site' or name == 'Web'
			vm.name = File.basename(File.dirname(path))
		else
			vm.name = name
		end

		# configure virtual machine resources
		vm.memory = 256
		vm.cpus = 1
	end

	# install web server and required components
	config.vm.provision :shell, :path => 'provision.sh', keep_color: true, run:'once'

	# make sure caracal is up to date
	config.vm.provision :shell, :inline => 'cd /var/www; git pull origin', keep_color: true, run:'always'

	# configure shared directories
	config.vm.synced_folder 'site', '/vagrant', owner: 'www-data', group: 'www-data'

	# configure network
	config.vm.network :forwarded_port, host:8080, guest:80
	config.vm.network :forwarded_port, host:8085, guest:8080
end
