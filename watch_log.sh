#!/bin/bash
clear
vagrant ssh -c "sudo tail -n0 -f /var/log/apache2/error.log"
