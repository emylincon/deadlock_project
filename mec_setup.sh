#!/bin/bash

clear
echo '============ Preparing your MEC Platform =============='
sleep 3
apk update && apk upgrade
apk add busybox-static apk-tools-static
apk add make
cd
apk add git
apk add wget
apk add nano
apk add net-tools
apk add nmap
clear


echo "upgrading to alpine 3.10"
sleep 2
git clone https://github.com/alpinelinux/alpine-conf.git
cd alpine-conf
make
mv libalpine.sh /lib/
sh setup-apkrepos
r
apk update
sed -i -e 's/v3\.3/v3.10/g' /etc/apk/repositories
apk.static update
apk.static upgrade --no-self-upgrade --available --simulate
clear

echo "installing python3"
sleep 2
apk add python3
apk add pkgconf build-base python3-dev
apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev
python3.7 -m ensurepip
python3.7 -m pip install --upgrade pip

pip3 install psutil
pip3 install paramiko
pip3 install numpy

apk add openssh-client
apk add openssh
apk add acf-openssh




/etc/init.d/ssh start
clear
echo '============= All done.. Ready to use! ==============='

