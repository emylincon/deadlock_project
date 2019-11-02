# Deadlock project for MEC

##### This is a property of London South Bank University licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
##### Please get permission before use
@Author: Emeka Emmanuel Ugwuanyi ugwuanye@lsbu.ac.uk with contributions from Saptarshi Ghosh

### The distribution of tasks used 
`g/g/1 (((23**r.randrange(1, 1331)) % r.randrange(1, 1777)) % 5)`

```
homogenous experiment done. still on progress!
```

#### SET UP Commands
```
apt update  
passwd   
password   
password   
apt install git sudo -y  
adduser mec  
password  
password  
usermod -aG sudo mec  
su - mec  
git clone https://github.com/emylincon/deadlock_project.git  
cd deadlock_project  
sudo bash set_up.sh  
password
```

## How To Use The System
###### Run instrutions for heterogenous environment
The following are the steps for running and setup of the system. The files for heterogenous are located in 2algo folder

##### Broker:
* start the mosquitto server first. 
* it is usually located on the first MEC node 
```bash
/etc/init.d/mosquitto start
```

##### cloud node:
* start the cloud nodes.
```bash
python3 deadlock_project/2algo/0_cloud.py
```
* then enter the brokers ip (ip address on eth0)


##### MEC nodes:
navigate to the MEC user. that is where the deadlock_project is sitting
```bash
cd /deadlock_project/2algo/
```
run any of the desired algorithm
* the speak .py runs only on the brokers
* the gui.py runs only on a gui not a server
* the np.py runs on any other node


##### Clients:
* each client(o_gui_user.py) have a prepared data they have to read and run from {user3, user4 and user5}
* each correspond to a respective client node
* the corresponding python file have to be renamed to record.py in the user node.
* there are 3 official client/user files:
* 1.) 0.0_user.py : this is for the server 
* 2.) gui_user.py : this is for the desktop. it shows a live plot of the results obtained. Run this file if you dont want to use a predefined data. it automtically generates data using GG1 distribution
* 3.) o_gui_user.py : This is also to be used on a desktop because it shows a live plot of the result obtained. the difference between this and gui_user is that the this is used when you already have a predefined data. the data should be named record.py and placed on each of the client node




