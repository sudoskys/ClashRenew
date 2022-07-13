# ClashRenew

Linux clash or crash-meta configuration-config.yaml automatically updates the small script, please audit the code before use.


**The user is responsible for the consequences of using this item.**


## Install

After cloning the project, please move the files to the ````～/```` (HOME) directory

#### dependencies

```pip install pyyaml==5.4.1```

>Because of the compatibility of the yaml library, you need to use 5.4.1, if not you can use ```pip uninstall```



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
After=network.target

[Service]
Type=simple
Restart=on-abort
ExecStart=sh usr/local/bin/cron.sh

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


*Partial reference to this tutorial*
https://blog.linioi.com/posts/clash-on-arch/





### Program configuration file example

Note the spaces
````
RenewConfig: True
RenewTargetKey: cloud22
content:
   cloud1:
       - https://
   cloud22:
       - https://

````

```RenewConfig``` refers to whether to replace the running dependent config, ```RenewTargetKey``` refers to the replacement target (must be in the list)




Edit the python script and configure the config file name and data directory as noted.
