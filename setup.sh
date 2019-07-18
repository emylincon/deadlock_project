#!/bin/bash

clear
echo '============ Preparing your MEC Platform =============='
sleep 3
echo -e "\nupdating repository...\n"
apt update && apt upgrade -y >> /dev/null

echo -e "installing python3...\n"
apt install python3 -y >> /dev/null
apt install python3-pip -y >> /dev/null

echo "installing required python3 packages..."
echo -e "(drawnow, psutil, matplotlib, paramiko, pyfiglet, numpy)\n"
pip3 install drawnow >> /dev/null
apt install python3-psutil -y >> /dev/null
apt install python3-matplotlib -y >> /dev/null
apt install python3-paramiko -y >> /dev/null
apt install python3-pyfiglet -y >> /dev/null
apt install python3-numpy -y >> /dev/null

echo -e "installing openssh...\n"
apt install openssh-client -y >> /dev/null
apt install openssh-server -y >> /dev/null

echo "installing network tools..."
echo -e "(wget, apt-utils, iputils-ping, net-tools, nmap)\n"
apt install wget -y >> /dev/null
apt install apt-utils -y >> /dev/null
apt install iputils-ping -y >> /dev/null
apt install net-tools -y >> /dev/null
apt install nano -y >> /dev/null
apt install nmap -y >> /dev/null

echo -e "starting ssh server..\n"
sleep 1.5
/etc/init.d/ssh start
echo '============= All done.. Ready to use! ==============='
