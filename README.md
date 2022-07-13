# ClashRenew

Linux clash或clash-meta 配置-config.yaml 自动更新小脚本，使用前请审计代码。


**使用本项目造成的后果需使用者负责。**



克隆本项目后请移动文件到 ```～/``` （HOME）目录

### 依赖

```pip install pyyaml==5.4.1```

>因为 yaml 库的兼容问题，需要使用 5.4.1，如果不是可以使用 ```pip unstall```

### 方式一: 配置开机自动

使用```.zshrc```或者```.bashrc```即可


### 方式二: 配置定时运行

```
EDITOR=vim crontab -e
```

**输入定时任务**
每五小时执行一次（因为你不太可能开着机）
 ```0 */5 * * *  /bin/sh ～/cron.sh```

**查看定时任务**
```
crontab -l
```



### 程序配置文件示例

注意空格
```
RenewConfig: True
RenewTargetKey: cloud22
content:
   cloud1:
       - https://
   cloud22:
       - https://

```

```RenewConfig``` 指是否替换运行依赖的config,```RenewTargetKey```指替换的目标（必须在列表里）




编辑 python 脚本，按照注释配置 配置文件名称 和 数据目录。