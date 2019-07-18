#!/bin/bash

clear
echo '============ Preparing your MEC Platform =============='
sleep 3
apk update && apk upgrade
apk add python3

pip3 install psutil
pip3 install paramiko
pip3 install numpy

apk add openssh-client
apk add openssh

apk add wget
apk add nano
apk add net-tools
apk add nmap

/etc/init.d/ssh start
clear
echo '============= All done.. Ready to use! ==============='

