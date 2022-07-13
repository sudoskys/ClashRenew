# ClashRenew

Linux clash or crash-meta configuration-config.yaml automatically updates the small script, please audit the code before use.


**The user is responsible for the consequences of using this item. **


## Install

After cloning the project, please move the files to the ````～/```` (HOME) directory

#### dependencies

```pip install pyyaml==5.4.1```

>Because of the compatibility of the yaml library, you need to use 5.4.1, if not you can use ```pip uninstall```



### Method 1: Configure automatic startup

-------

It's best not to use ````.zshrc`` or ```.bashrc```, it will cause the problem of executing when the terminal is opened...

Specific method reference

https://www.cnblogs.com/downey-blog/p/10473939.html

https://blog.51cto.com/u_14442495/2905438

https://codeantenna.com/a/wOxb6ZVNrJ


### Method 2: Configure timing operation

------

````
EDITOR=vim crontab -e
````

**Enter a scheduled task**
Do it every five hours (because you're unlikely to have the machine on)
 ````0 */5 * * * /bin/sh ~/cron.sh```

**View scheduled tasks**
````
crontab -l
````



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
