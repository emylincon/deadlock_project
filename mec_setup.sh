#!/bin/bash

clear
echo '============ Preparing your MEC Platform =============='
sleep 3
apk update
apk upgrade
apk add busybox-static apk-tools-static
apk add make
apk add sudo
cd
apk add git
apk add wget
apk add nano
apk add net-tools
apk add nmap
apk add libpng
apk add freetype
apk add gcc
apk add g++
clear


echo "upgrading to alpine 3.10"
sleep 2
git clone https://github.com/alpinelinux/alpine-conf.git
cd alpine-conf
make
cp libalpine.sh /lib/
sh setup-apkrepos
r
apk update
sed -i -e 's/v3\.3/v3.8/g' /etc/apk/repositories
apk update
apk upgrade
apk.static update
apk.static upgrade --no-self-upgrade --available --simulate
clear

echo "installing python3"
sleep 2
apk add python3
apk add pkgconf build-base python3-dev
apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev
python3.6 -m ensurepip
python3.6 -m pip install --upgrade pip
pip3 install --upgrade pip setuptools
pip3 install freetype-py pypng
pip3 install docwriter
clear

echo "Setting up environment for python packages"
sleep 2
cd
wget http://www.zlib.net/zlib-1.2.11.tar.gz
tar -xvzf zlib-1.2.11.tar.gz
cd zlib-1.2.11/
./configure
make
make install

cd
wget http://prdownloads.sourceforge.net/libpng/libpng-1.6.37.tar.gz?download
tar -xvzf libpng-1.6.37.tar.gz?download
cd libpng-1.6.37
./configure
make
make install

cd
wget https://sourceforge.net/projects/freetype/files/freetype2/2.10.1/freetype-2.10.1.tar.gz
tar -xvzf freetype-2.10.1.tar.gz
cd freetype-2.10.1/
./configure
make
make install


echo "installing python3 packages"
sleep 2
pip3 install psutil
pip3 install paramiko
pip3 install numpy
pip3 install matplotlib
pip3 install drawnow
clear

echo "installing openssh "
sleep 2
apk upgrade
apk add --upgrade busybox
apk add openssh-client
apk add openssh
apk add acf-openssh
apk add --no-cache openrc
rc-update add sshd
apk add --update openssh
rm  -rf /tmp/* /var/cache/apk/*
rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key
touch /run/openrc/softlevel
/etc/init.d/sshd start


/etc/init.d/ssh start
clear
echo '============= All done.. Ready to use! ==============='


## updating an installing ssh
 git clone https://github.com/alpinelinux/alpine-conf.git
 cd alpine-conf/
 make
 cp libalpine.sh /lib/
 sh setup-apkrepos
 apk update
 sed -i -e 's/v3\.3/v3.8/g' /etc/apk/repositories
 apk.static update
 apk.static upgrade --no-self-upgrade --available --simulate
 apk update
 apk upgrade
 apk.static upgrade --no-self-upgrade --available --simulate
 apk upgrade
 apk add --upgrade busybox
 apk add openssh
 apk add openrc
 apk update
 apk upgrade
 rc-update add sshd
 rc-status
 apk add acf-openssh
 rc-status
 /etc/init.d/sshd status
 touch /run/openrc/softlevel
 /etc/init.d/sshd status
 /etc/init.d/sshd start
