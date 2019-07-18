#!/bin/bash

clear
echo '============ Preparing your MEC Platform =============='
sleep 3
echo -e "\nupdating repository...\n"
apt update && apt upgrade -y >> /dev/null0

apt install python3 -y >> /dev/null0
apt install python3-pip -y >> /dev/null0
pip3 install drawnow -y >> /dev/null0
apt install python3-psutil -y >> /dev/null0
apt install python3-matplotlib -y >> /dev/null0
apt install python3-paramiko -y >> /dev/null0
apt install python3-pyfiglet -y >> /dev/null0
apt install openssh-client -y >> /dev/null0
apt install openssh-server -y >> /dev/null0
apt install wget -y >> /dev/null0
apt install apt-utils -y >> /dev/null0
apt install iputils-ping -y >> /dev/null0
apt install net-tools -y >> /dev/null0
apt install nano -y >> /dev/null0
apt install python3-numpy -y >> /dev/null0
apt install nmap -y >> /dev/null0

/etc/init.d/ssh start
clear
echo '============= All done.. Ready to use! ==============='
