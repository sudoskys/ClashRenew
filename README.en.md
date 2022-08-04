# ClashRenew

Linux clash or crash-meta configuration-config.yaml automatically updates the small script, please audit the code before use.


Ps: You can also use Clash proxy-provider, but it is better to isolate and update stable separately.

When the proxy-provider directly uses the http type to subscribe to the source, if the URL cannot be accessed, Clash cannot be started at this time.



**Users are responsible for all consequences of using this project.**


## Install

After cloning the project, please move the files to the ````～/```` (HOME) directory

#### dependencies

```pip install requirements.txt```


>Because of the compatibility problem of the yaml library, the configuration needs to use 5.4.1



### Configure automatic startup

-------

It's best not to use ```.zshrc``` or ```.bashrc```, it will cause the problem of executing when the terminal is opened...

**Run as follows to automatically start crash**
````
systemctl --user enable clash.service
systemctl --user start clash.service
systemctl --user status clash.service
````

**copy cron.sh**
````
sudo cp ~/cron.sh /usr/local/bin
````

The misleading tutorial is corrected here, using **login account** instead of full system crash.

````
cd /usr/lib/systemd/user/
sudo vim clashrenew.service


````


**fill in**
````
[Unit]
Description=clashRenew
After=network-online.target

[Service]
Type=simple
Restart=on-abort
ExecStart=sh /usr/local/bin/cron.sh
ExecStartPre=/bin/sleep 10

[Install]
WantedBy=default.target

````

**Start clashrenew program**
````
systemctl --user enable clashrenew.service
systemctl --user start clashrenew.service
systemctl --user status clashrenew.service
````

In this way, the user-defined service can be run.

PS: ExecStartPre=/bin/sleep 20 represents a delay of 20 seconds, you can also modify the crash service to delay the start (if you are a wireless link)

I clash.service for example! (applicable to successful startup but io timeout)

````
[Unit]
Description=A rule based proxy in Go.
After=network-online.target

[Service]
Type=exec
Restart=on-abort
ExecStart=/usr/bin/clash
ExecStartPre=/bin/sleep 15

[Install]
WantedBy=default.target
````

**Note: ```After=network-online.target``` has adaptation problems, please pay attention!**

Ps: As for network , see https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/systemd-network-targets-and-services_configuring-and-managing-networking

*Partial reference to this tutorial*
https://blog.linioi.com/posts/clash-on-arch/


Reload configuration ```systemctl --user daemon-reload```


### Program configuration file example

Note the spaces

````
RenewConfig: True
RenewNotify: True
# If you don't want to be notified, please fill False in the above line
RenewTargetKey: cloud22
content:
   cloud1:
       - https://
   cloud22:
       - https://

````

```RenewConfig``` refers to whether to replace the running dependent config, ```RenewTargetKey``` refers to the replacement target (must be in the list)




Edit the python script and configure the config file name and data directory as noted.

#### Barrier-free feeding

[![s](https://img.shields.io/badge/Become-sponsor-DB94A2)](https://dun.mianbaoduo.com/@Sky0717)