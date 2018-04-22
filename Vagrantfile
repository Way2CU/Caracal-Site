# Caracal Site - Development Environment
#
# Copyright © 2014. Way2CU. All Rights Reserved.
# Author: Mladen Mijatov

Vagrant.configure('2') do |config|
	config.vm.box = 'debian/contrib-jessie64'

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

		# configure virtualization options
		vm.customize [ 'modifyvm', :id, '--paravirtprovider', 'kvm' ]

		# configure virtual machine resources
		vm.memory = 256
		vm.cpus = 1
	end

	# install web server and required components
	config.vm.provision :ansible do |ansible|
		ansible.compatibility_mode = '2.0'
		ansible.playbook = 'provision/playbook.yml'
		ansible.limit = 'all'
		ansible.groups = {
			'all' => ['caracal']
		}
	end

	# configure synchronized folder to specific user
	config.vm.synced_folder 'site', '/vagrant', owner: 'www-data', group: 'www-data'

	# configure network
	config.vm.network :forwarded_port, host:8080, guest:80
end
